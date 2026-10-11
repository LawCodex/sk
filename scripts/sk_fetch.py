#!/usr/bin/env python3
"""Fetch the list of Slovak legislation in force and the consolidated HTML of each act.

Sources (both operated by the Ministry of Justice of the Slovak Republic, Slov-Lex):
  * search API used by the www.slov-lex.sk portal:
      https://api-gateway.slov-lex.sk/vyhladavanie/predpisZbierky/rozsirene
    (Solr-backed; `ucinnyK=<date>` returns the version of each act effective on that date)
  * static HTML of every consolidated version:
      https://static.slov-lex.sk/static/SK/ZZ/<year>/<number>/<yyyymmdd>.html

Output (cache, never committed): <raw>/list.json and <raw>/html/<year>/<number>-<version>.html.gz

Usage: python sk_fetch.py [--raw DIR] [--date YYYY-MM-DD] [--workers 3]
"""
import argparse
import datetime as dt
import gzip
import json
import os
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

UA = "LawCodex/1.0 (+https://github.com/LawCodex)"
API = "https://api-gateway.slov-lex.sk/vyhladavanie/predpisZbierky/rozsirene"
STATIC = "https://static.slov-lex.sk/static"
TYPES = {"Zakon", "UstavnyZakon", "NariadenieVlady", "Vyhlaska"}

_local = threading.local()


def session():
    s = getattr(_local, "s", None)
    if s is None:
        s = requests.Session()
        s.headers["User-Agent"] = UA
        _local.s = s
    return s


def get(url, params=None, tries=6):
    delay = 5
    for i in range(tries):
        try:
            r = session().get(url, params=params, timeout=120)
            if r.status_code == 200:
                return r
            if r.status_code == 404:
                return r
            print(f"HTTP {r.status_code} {url} {params or ''}", file=sys.stderr)
        except requests.RequestException as e:
            print(f"ERR {e} {url}", file=sys.stderr)
        time.sleep(delay)
        delay = min(delay * 2, 120)
    raise RuntimeError(f"giving up on {url}")


def search(params):
    docs, start = [], 0
    while True:
        p = dict(params, rows=1000, start=start)
        d = get(API, p).json()
        docs += d["docs"]
        start += 1000
        if start >= d["numFound"]:
            return docs
        time.sleep(1)


def build_list(raw, today):
    eff = search({"ucinnyK": today})
    for x in eff:
        x["_status"] = "effective"
    seen = {x["iri"].rsplit("/", 1)[0] for x in eff}
    # acts already published but not yet effective (vacatio legis)
    since = (dt.date.fromisoformat(today) - dt.timedelta(days=5 * 365)).isoformat()
    fut = search({"vyhlaseny_zaciatok": since, "vyhlaseny_koniec": today})
    for x in fut:
        base = x["iri"].rsplit("/", 1)[0]
        if base in seen or (x.get("ucinnyOd") or "")[:10] <= today:
            continue
        x["_status"] = "not_yet_effective"
        eff.append(x)
        seen.add(base)
    out = [x for x in eff if x.get("typPredp") in TYPES]
    out.sort(key=lambda x: x["iri"])
    with open(os.path.join(raw, "list.json"), "w", encoding="utf-8") as f:
        json.dump({"date": today, "docs": out}, f, ensure_ascii=False, indent=0)
    return out


def path_for(raw, iri):
    _, _, _, year, num, ver = iri.split("/")
    return os.path.join(raw, "html", year, f"{num}-{ver}.html.gz")


def fetch_one(raw, iri):
    p = path_for(raw, iri)
    if os.path.exists(p):
        return "cached"
    r = get(f"{STATIC}{iri}.html")
    if r.status_code == 404:
        return "404"
    os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = p + ".tmp"
    with gzip.open(tmp, "wb") as f:
        f.write(r.content)
    os.replace(tmp, p)
    time.sleep(0.3)
    return "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=os.path.join(os.path.dirname(__file__), "..", "..", "_raw", "sk"))
    ap.add_argument("--date", default=dt.date.today().isoformat())
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--relist", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.raw, exist_ok=True)
    lp = os.path.join(a.raw, "list.json")
    if a.relist or not os.path.exists(lp):
        docs = build_list(a.raw, a.date)
    else:
        docs = json.load(open(lp, encoding="utf-8"))["docs"]
    print(f"{len(docs)} acts", flush=True)
    stats, missing = {}, []
    with ThreadPoolExecutor(a.workers) as ex:
        futs = {ex.submit(fetch_one, a.raw, d["iri"]): d["iri"] for d in docs}
        for i, f in enumerate(as_completed(futs), 1):
            try:
                st = f.result()
            except Exception as e:  # noqa
                st = "error"
                print(f"FAIL {futs[f]} {e}", file=sys.stderr)
            stats[st] = stats.get(st, 0) + 1
            if st in ("404", "error"):
                missing.append(futs[f])
            if i % 200 == 0:
                print(i, stats, flush=True)
    print("done", stats, flush=True)
    with open(os.path.join(a.raw, "missing.json"), "w") as f:
        json.dump(missing, f, indent=0)


if __name__ == "__main__":
    main()
