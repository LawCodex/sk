#!/usr/bin/env python3
"""Convert cached Slov-Lex consolidated HTML (see sk_fetch.py) to LawCodex Markdown.

Usage: python sk_convert.py [--raw DIR] [--out REPO_DIR] [--retrieved YYYY-MM-DD]
"""
import argparse
import datetime as dt
import gzip
import json
import os
import re
import sys
import unicodedata
from urllib.parse import urljoin

from lxml import html as LH

STATIC = "https://static.slov-lex.sk/static"
PORTAL = "https://www.slov-lex.sk/ezbierky/pravne-predpisy"

# structural groups rendered as headings (outer -> inner)
GROUPS = {"cast", "hlava", "diel", "oddiel", "pododdiel", "kapitola", "podkapitola",
          "skupinaParagrafov", "skupinaElementov", "skupinaClankov", "priloha", "clanokUvod"}
ARTICLES = {"paragraf", "clanok", "ustavnyclanok"}
TEXTUAL = {"text", "text2", "blokTextu", "predpisText", "text1"}
HEADER = ["predpisOznacenie", "predpisTyp", "predpisPodnadpis", "predpisDatum", "predpisNadpis"]
IMG_NOTE = "*[obrázok – pozri pôvodný text na Slov-Lex]({})*"

TYPE_MAP = {
    "UstavnyZakon": ("constitutional_act", "ustavne-zakony"),
    "Zakon": ("act", "zakony"),
    "NariadenieVlady": ("government_regulation", "nariadenia-vlady"),
    "Vyhlaska": ("decree", "vyhlasky"),
}


def norm_ws(s):
    return re.sub(r"[ \t\r\n ]+", " ", s)


def classes(el):
    return (el.get("class") or "").split()


def base_class(el):
    c = classes(el)
    return c[0] if c else ""


class Ctx:
    def __init__(self, page_url, portal_url=""):
        self.page_url = page_url
        self.portal_url = portal_url


# ---------------------------------------------------------------- inline

def inline(el, ctx, parts):
    """Render inline content of el into list `parts`; "\x00" marks a paragraph break,
    tuples ('block', text) are block-level items (tables)."""
    if el.text:
        parts.append(norm_ws(el.text))
    for ch in el:
        tag = ch.tag if isinstance(ch.tag, str) else ""
        if tag == "br":
            parts.append("\x00")
        elif tag == "table":
            parts.append(("block", table(ch, ctx)))
        elif tag == "img":
            parts.append(IMG_NOTE.format(ctx.portal_url))
        elif tag in ("sup", "sub"):
            t = norm_ws(ch.text_content()).strip()
            if t:
                parts.append(f"<{tag}>{t}</{tag}>")
        elif tag in ("b", "strong"):
            t = norm_ws(ch.text_content())
            if t.strip():
                lead = " " if t[:1] == " " else ""
                trail = " " if t[-1:] == " " else ""
                parts.append(f"{lead}**{t.strip()}**{trail}")
        elif tag in ("i", "em"):
            t = norm_ws(ch.text_content())
            if t.strip():
                lead = " " if t[:1] == " " else ""
                trail = " " if t[-1:] == " " else ""
                parts.append(f"{lead}*{t.strip()}*{trail}")
        elif tag == "a" and "predpis-pdf-priloha" in classes(ch):
            t = norm_ws(ch.text_content()).strip() or "príloha (PDF)"
            parts.append(f"[{t}]({urljoin(ctx.page_url, ch.get('href', ''))})")
        elif tag in ("div", "p", "ul", "ol", "li"):
            parts.append("\x00")
            inline(ch, ctx, parts)
            parts.append("\x00")
        elif tag:
            inline(ch, ctx, parts)
        if ch.tail:
            parts.append(norm_ws(ch.tail))


def esc_line(s):
    s = s.strip()
    if re.match(r"^(#|>|\+ |=+$|-{3,}$|\*\s)", s):
        s = "\\" + s
    return s


def inline_blocks(el, ctx):
    parts = []
    inline(el, ctx, parts)
    blocks, cur = [], []

    def flush():
        t = re.sub(r" {2,}", " ", "".join(cur)).strip()
        if t:
            blocks.append(esc_line(t))
        cur.clear()

    for p in parts:
        if isinstance(p, tuple):
            flush()
            blocks.append(p[1])
        elif p == "\x00":
            flush()
        else:
            cur.append(p)
    flush()
    return blocks


# ---------------------------------------------------------------- tables

def cell_text(td, ctx):
    bl = inline_blocks(td, ctx)
    return " <br> ".join(b.replace("\n", " ") for b in bl)


def table(tb, ctx):
    rows = tb.xpath(".//tr")
    complex_ = bool(tb.xpath(".//td[@rowspan>1]|.//td[@colspan>1]|.//th[@rowspan>1]|.//th[@colspan>1]"
                             "|.//table//table"))
    grid = []
    for r in rows:
        cells = r.xpath("./td|./th")
        grid.append(cells)
    if not grid:
        return ""
    if not complex_:
        n = max(len(r) for r in grid)
        out = []
        for i, r in enumerate(grid):
            vals = [cell_text(c, ctx).replace("|", "\\|") for c in r] + [""] * (n - len(r))
            out.append("| " + " | ".join(vals) + " |")
            if i == 0:
                out.append("|" + "---|" * n)
        return "\n".join(out)
    # keep as HTML (structure only)
    out = ["<table>"]
    for r in grid:
        out.append("<tr>")
        for c in r:
            attrs = ""
            for a in ("rowspan", "colspan"):
                if c.get(a) and c.get(a) != "1":
                    attrs += f' {a}="{c.get(a)}"'
            t = cell_text(c, ctx)
            out.append(f"<td{attrs}>{t}</td>")
        out.append("</tr>")
    out.append("</table>")
    return "\n".join(out)


# ---------------------------------------------------------------- structure

def child_by_suffix(el, base, suffix):
    for ch in el:
        if isinstance(ch.tag, str) and base_class(ch) == base + suffix:
            return ch
    return None


def heading(level, text):
    text = text.strip()
    if not text:
        return None
    if level <= 6:
        return "#" * level + " " + text
    return f"**{text}**"


def join_label(label, title):
    label, title = (label or "").strip(), (title or "").strip()
    if label and title:
        return f"{label} — {title}"
    return label or title


def render(el, ctx, depth, out):
    """depth = heading level for the next structural heading."""
    for ch in el:
        if not isinstance(ch.tag, str):
            continue
        if ch.tag == "table":
            out.append(table(ch, ctx))
            continue
        if ch.tag != "div":
            bl = inline_blocks(ch, ctx)
            out.extend(bl)
            continue
        bc = base_class(ch)
        cls = classes(ch)
        if bc in TEXTUAL:
            render_mixed(ch, ctx, depth, out)
        elif bc == "citat":
            sub = []
            render(ch, ctx, 7, sub)
            if not sub:
                sub = inline_blocks(ch, ctx)
            q = []
            for b in sub:
                q.append("\n".join("> " + ln if ln else ">" for ln in b.split("\n")))
            out.append("\n>\n".join(q))
        elif bc == "poznamky":
            out.append(heading(2, "Poznámky pod čiarou"))
            render(ch, ctx, 3, out)
        elif bc == "prilohy":
            out.append(heading(2, "Prílohy"))
            render(ch, ctx, 3, out)
        elif "Skupina" in cls or bc in ("neoznacenaPolozka",):
            lab_el = child_by_suffix(ch, bc, "Oznacenie")
            tit_el = child_by_suffix(ch, bc, "Nadpis")
            label = " ".join(inline_blocks(lab_el, ctx)) if lab_el is not None else ""
            title = " ".join(inline_blocks(tit_el, ctx)) if tit_el is not None else ""
            rest = [c for c in ch if c is not lab_el and c is not tit_el]
            if bc in GROUPS or bc in ARTICLES:
                h = heading(depth, join_label(label, title))
                if h:
                    out.append(h)
                sub = []
                for c in rest:
                    render_one(c, ctx, depth + 1, sub)
                out.extend(sub)
            else:
                # paragraph-like (odsek, pismeno, bod, odrazka, poznamka, oznacenaPolozka...)
                sub = []
                for c in rest:
                    render_one(c, ctx, depth, sub)
                if title:
                    t = join_label(label, title)
                    out.append(f"**{t}**")
                    out.extend(sub)
                elif label and len(label) > 12:
                    out.append(f"**{label}**")
                    out.extend(sub)
                elif label:
                    if sub and not sub[0].startswith(("|", "<table", ">", "#", "**")):
                        out.append(esc_line(f"{label} {sub[0]}"))
                        out.extend(sub[1:])
                    else:
                        out.append(esc_line(label))
                        out.extend(sub)
                else:
                    out.extend(sub)
        elif bc.endswith("Oznacenie") or bc.endswith("Nadpis"):
            t = " ".join(inline_blocks(ch, ctx))
            if t:
                out.append(f"**{t}**")
        else:
            sub = []
            render(ch, ctx, depth, sub)
            if sub:
                out.extend(sub)
            else:
                out.extend(inline_blocks(ch, ctx))


def has_struct(el):
    return any(isinstance(d.tag, str) and d.tag == "div" and d.get("class") for d in el.iterdescendants())


def render_mixed(el, ctx, depth, out):
    """Text container that may also hold structural divs (quoted amendments, nested items)."""
    if not has_struct(el):
        out.extend(inline_blocks(el, ctx))
        return
    tmp = LH.Element("span")
    tmp.text = el.text

    def flush():
        if (tmp.text and tmp.text.strip()) or len(tmp):
            out.extend(inline_blocks(tmp, ctx))
        for c in list(tmp):
            tmp.remove(c)
        tmp.text = None

    for ch in list(el):
        if isinstance(ch.tag, str) and ch.tag == "div" and (ch.get("class") or has_struct(ch)):
            flush()
            tail = ch.tail
            ch.tail = None
            render_one(ch, ctx, depth, out)
            tmp.text = tail
        else:
            tail = ch.tail
            tmp.append(ch)
    flush()


def render_one(el, ctx, depth, out):
    render(_Fake([el]), ctx, depth, out)


class _Fake:
    """Iterable wrapper so render() can process a single element."""
    def __init__(self, els):
        self.els = els

    def __iter__(self):
        return iter(self.els)


# ---------------------------------------------------------------- doc

def slugify(s, maxlen=70):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if len(s) > maxlen:
        s = s[:maxlen]
        if "-" in s[30:]:
            s = s[: s.rfind("-")]
    return s.strip("-")


def short_title(title):
    t = title.strip()
    idx = [i for i in (t.find(" o "), t.find(", ktor"), t.find(" ktor")) if i > 0]
    if idx and min(idx) < 200:
        t = t[min(idx):].lstrip(" ,")
    else:
        t = re.sub(r"^(Ústavný zákon|Zákon|Nariadenie vlády|Vyhláška)\b[\s,]*", "", t)
    return t


CS_CHARS = re.compile(r"[ěřůĚŘŮ]")
SK_CHARS = re.compile(r"[äôľĺŕÄÔĽĹŔ]")


def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def convert(raw, out_dir, retrieved):
    lst = json.load(open(os.path.join(raw, "list.json"), encoding="utf-8"))
    docs = lst["docs"]
    stats = {}
    problems = []
    written = set()
    for d in docs:
        iri = d["iri"]
        _, _, _, year, num, ver = iri.split("/")
        p = os.path.join(raw, "html", year, f"{num}-{ver}.html.gz")
        if not os.path.exists(p):
            problems.append((iri, "not downloaded"))
            continue
        s = gzip.open(p).read().decode("utf-8", "replace")
        i = s.find('<div class="predpis Skupina')
        j = s.find('<div id="iri"')
        if i < 0:
            problems.append((iri, "no predpis div"))
            continue
        frag = s[i: j if j > i else len(s)]
        root = LH.fromstring("<div>" + frag + "</div>")
        page_url = f"{STATIC}{iri}.html"
        ctx = Ctx(page_url, PORTAL + iri)
        body = []
        # header lines of the act
        pred = root.xpath("./div[contains(concat(' ', @class, ' '), ' predpis ')]")
        hdr = []
        if pred:
            pr = pred[0]
            for hc in HEADER:
                for ch in pr:
                    if isinstance(ch.tag, str) and base_class(ch) == hc:
                        hdr.extend(inline_blocks(ch, ctx))
                        ch.getparent().remove(ch)
                        break
        if hdr:
            body.append("\n\n".join(f"**{h}**" if not h.startswith("**") else h for h in hdr))
        render(root, ctx, 2, body)
        body = [b for b in body if b and b.strip()]
        text = "\n\n".join(body)
        plain = re.sub(r"\W+", "", text)
        typ = d["typPredp"]
        ftype, folder = TYPE_MAP[typ]
        title = norm_ws(d.get("nazov") or d["cislo"]).strip()
        if year == "1992" and num == "460" and typ == "UstavnyZakon":
            ftype, folder = "constitution", "ustava"
            rel = os.path.join(folder, "460-1992-ustava-slovenskej-republiky.md")
        else:
            slug = slugify(short_title(title)) or "predpis"
            fname = f"{num}-{year}-{slug}.md"
            rel = os.path.join(folder, fname) if folder == "ustavne-zakony" else os.path.join(folder, year, fname)
        if rel in written:
            rel = rel[:-3] + f"-{ver}.md"
        written.add(rel)
        ncs, nsk = len(CS_CHARS.findall(text)), len(SK_CHARS.findall(text))
        lang = "cs" if ncs > 20 and ncs > 2 * nsk else "sk"
        fm = [
            "---",
            f"title: {yaml_str(title)}",
            f"identifier: {yaml_str(d['cislo'])}",
            f"eli: {yaml_str('https://www.slov-lex.sk/pravne-predpisy/SK/ZZ/' + year + '/' + num + '/')}",
            f"type: {ftype}",
            "jurisdiction: sk",
            f"language: {lang}",
        ]
        if d.get("vyhlaseny"):
            fm.append(f"date: {d['vyhlaseny'][:10]}")
        if re.fullmatch(r"\d{8}", ver):
            fm.append(f"last_amended: {ver[:4]}-{ver[4:6]}-{ver[6:]}")
        elif d.get("ucinnyOd"):
            fm.append(f"last_amended: {d['ucinnyOd'][:10]}")
        fm.append("status: in_force")
        if d.get("_status") == "not_yet_effective":
            fm.append(f"effective_from: {d['ucinnyOd'][:10]}")
        if d.get("ucinnyDo"):
            fm.append(f"version_effective_until: {d['ucinnyDo'][:10]}")
        fm.append(f"consolidated_version: {yaml_str(iri)}")
        fm.append(f"source: {yaml_str(PORTAL + iri)}")
        fm.append(f"retrieved: {retrieved}")
        fm.append("---")
        md = "\n".join(fm) + "\n\n# " + f"{title}" + "\n\n" + text + "\n"
        md = md.replace("\r", "")
        if len(plain) < 200:
            problems.append((iri, f"short text ({len(plain)} chars)"))
        dest = os.path.join(out_dir, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8", newline="\n") as f:
            f.write(md)
        stats[folder] = stats.get(folder, 0) + 1
    print(json.dumps(stats, indent=1))
    with open(os.path.join(raw, "convert_problems.json"), "w") as f:
        json.dump(problems, f, indent=0, ensure_ascii=False)
    print(len(problems), "problems")
    return stats


def main():
    ap = argparse.ArgumentParser()
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument("--raw", default=os.path.join(here, "..", "..", "_raw", "sk"))
    ap.add_argument("--out", default=os.path.join(here, ".."))
    ap.add_argument("--retrieved", default=dt.date.today().isoformat())
    a = ap.parse_args()
    convert(a.raw, a.out, a.retrieved)


if __name__ == "__main__":
    main()
