# Slovakia — legislation as Markdown (LawCodex)

Consolidated texts (*aktuálne znenie*, the version effective today) of the legislation of the
Slovak Republic published in the **Zbierka zákonov** (Collection of Laws), converted to
Markdown, one file per act. Source: **Slov-Lex**, the legislative and information portal of the
Ministry of Justice of the Slovak Republic (https://www.slov-lex.sk).

Retrieved: **2026-10-12** (the consolidation date of each act is in its `last_amended`).

## Coverage

All acts of the kinds below that Slov-Lex reports as **effective on 2026-10-12**
(search parameter `ucinnyK=2026-10-12`), plus 22 acts already promulgated but not yet effective
(*vacatio legis*; marked with `effective_from:`):

| Directory | Contents | Files |
|---|---|---:|
| `ustava/` | Ústava Slovenskej republiky (460/1992 Zb.) | 1 |
| `ustavne-zakony/` | constitutional acts (*ústavné zákony*), incl. constitutional amendments and pre-1993 Czechoslovak ones Slov-Lex still lists as effective | 120 |
| `zakony/<year>/` | acts (*zákony*), incl. the codes — Občiansky zákonník 40/1964 Zb., Obchodný zákonník 513/1991 Zb., Trestný zákon 300/2005 Z. z., Trestný poriadok 301/2005 Z. z., Zákonník práce 311/2001 Z. z., Civilný sporový poriadok 160/2015 Z. z., … | 4,030 |
| `nariadenia-vlady/<year>/` | government regulations (*nariadenia vlády*) | 1,654 |
| `vyhlasky/<year>/` | decrees (*vyhlášky*) of ministries and other central authorities published in the Zbierka zákonov (before ~2000 this also includes decrees announcing international treaties) | 3,894 |
| **Total** | | **9,699** |

Notes:

- "In force" follows Slov-Lex's own effectiveness index. Slovak amending acts (*novely*,
  "ktorým sa mení a dopĺňa …") are never formally repealed, so they remain listed as effective
  (≈2,620 of the *zákony*, ≈790 *nariadenia vlády*, ≈1,280 *vyhlášky*); their text is the
  amending text, with quoted new wording rendered as blockquotes. Many old Czechoslovak
  (1918–1992) acts are likewise still formally effective even if obsolete.
- Language: texts are in the language in which they were promulgated. 976 pre-1993 acts
  (mostly federal / Czechoslovak ones) are in **Czech**; these have `language: cs`. All others
  are Slovak (`language: sk`).
- Repealed provisions are omitted by Slov-Lex in the consolidated text and are omitted here.
- Images embedded in the text (scanned formulas, forms, signs) are not copied; a placeholder
  links to the act's page on Slov-Lex. Annexes published only as PDF files are linked to their
  Slov-Lex URL (`https://static.slov-lex.sk/pdf/prilohy/...`).

## Not covered

- Repealed / expired acts and historical versions (only the version effective on the retrieval
  date is included).
- Other contents of the Zbierka zákonov that are not of the four kinds above: *oznámenia*
  (≈5,900 effective, mostly announcements of international treaties and of ministerial
  *opatrenia*), *opatrenia*, *uznesenia*, *nálezy* of the Constitutional Court, *rozhodnutia*,
  *redakčné oznámenia*, republished full texts (*úplné znenia*), presidential decrees of 1945
  (*dekréty*, 67), and other minor types (*nariadenia*, *výnosy*, *zásady*, …).
- Five search-index entries without any document type, and the Slovak-State-era
  *Slovenský zákonník* only insofar as Slov-Lex classifies those acts under the types above.
- Regional/municipal regulations, ministerial journals (*vestníky*), EU law, explanatory
  reports. Cross-reference links inside the text are kept as plain text.

## Format

```yaml
title: "Obchodný zákonník"                 # name of the act as given by Slov-Lex
identifier: "513/1991 Zb."                 # number/year in the Zbierka (Zb. before 1993, Z. z. after)
eli: "https://www.slov-lex.sk/pravne-predpisy/SK/ZZ/1991/513/"
type: act        # constitution | constitutional_act | act | government_regulation | decree
jurisdiction: sk
language: sk     # or cs for Czech-language pre-1993 acts
date: 1991-12-18              # date of promulgation (vyhlásenie) in the Zbierka
last_amended: 2026-01-01      # effective date of the consolidated version
status: in_force
effective_from: 2027-01-01    # only for acts not yet effective
version_effective_until: …    # only when the consolidated version has a known end date
consolidated_version: "/SK/ZZ/1991/513/20260101"
source: "https://www.slov-lex.sk/ezbierky/pravne-predpisy/SK/ZZ/1991/513/20260101"
retrieved: 2026-10-12
---
```

The body starts with the act's header (number, kind, issuing body, date, title, enacting
formula) as bold lines. Structural units — *časť / hlava / diel / oddiel / pododdiel /
kapitola* and titled groups of sections — map to Markdown headings by nesting depth, with their
title appended (`## PRVÁ ČASŤ — VŠEOBECNÉ USTANOVENIA`); sections and articles (`§ 1`, `Čl. 1`)
are the deepest headings (bold lines below `######`). Paragraphs, letters, points and indents are
plain paragraphs keeping their labels (`(1)`, `a)`, `1.`). Text quoted in amending provisions
is a blockquote. Footnotes follow under `## Poznámky pod čiarou`, annexes under `## Prílohy`.
Simple tables are Markdown tables; tables with merged cells are kept as HTML.

File names: `<number>-<year>-<slug>.md`, the slug being the transliterated title without the
leading kind/issuer (e.g. `zakony/2005/300-2005-trestny-zakon.md`).

## Sources

- Act list: the search API behind the Slov-Lex portal,
  `https://api-gateway.slov-lex.sk/vyhladavanie/predpisZbierky/rozsirene` (parameters
  `ucinnyK=<date>`, `rows`, `start`; vacatio-legis acts via `vyhlaseny_zaciatok`/`vyhlaseny_koniec`).
- Texts: the static HTML edition of Slov-Lex, `https://static.slov-lex.sk/static/SK/ZZ/<year>/<number>/<version>.html`
  (one file per consolidated version; the version effective on the retrieval date is used. For
  one act whose index entry pointed at a non-existent version, the version is resolved from the
  act's history page).
- robots.txt of www.slov-lex.sk allows everything and sets no crawl-delay; fetching used ≤ 4
  parallel connections with a descriptive User-Agent.

## Licence

Legislation is not subject to copyright in Slovakia: § 5(a) of the Copyright Act
(zákon č. 185/2015 Z. z., *Autorský zákon*) provides that "the text of a legal regulation,
an official decision or a court decision … including preparatory documentation and their
translation" is not subject of copyright (*Za predmet autorského práva sa nepovažuje … text
právneho predpisu …*). The consolidated texts are produced by the Ministry of Justice and are
provided for information; only the texts published in the Zbierka zákonov are legally binding.

## Regenerating

```sh
pip install -r scripts/requirements.txt
python scripts/sk_fetch.py --raw ../_raw/sk --date 2026-10-12   # list + HTML cache (~9,700 pages, a few hours)
python scripts/sk_convert.py --raw ../_raw/sk --out .            # write Markdown
```

`sk_fetch.py` caches gzipped HTML in the raw directory and skips already downloaded versions;
`--relist` rebuilds the act list.
