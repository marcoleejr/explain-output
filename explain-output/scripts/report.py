#!/usr/bin/env python3
"""Rung 3 in under 30 s: JSON spec -> static single-file HTML (no JS, AAA contrast, mobile).

  python3 report.py spec.json [out.html]      # default out: $EXPLAIN_OUTPUT_DIR or ./explain/<slug>.html
  echo '{...}' | python3 report.py - out.html

Spec (every key optional except title):
{"title": "Verdict first", "lead": "1-2 sentences with the numbers that decide",
 "kpis": [{"label": "Passing", "value": "42%", "tone": "bad|warn|ok"}],
 "charts": [{"title": "Takeaway as title", "unit": "%", "max": 100,
             "items": [{"label": "Rule", "value": 53.3, "after": 88, "tone": "bad"}]}],
 "findings": [{"title": "Short claim", "detail": "Evidence / example", "tone": "bad"}],
 "table": {"head": ["Col"], "rows": [["cell"]]},
 "sections": [{"h": "Heading", "html": "<p>trusted inline html</p>"}],
 "evidence": "raw text, shown folded"}
Prints the output path. Charts with "after" draw a before/after pair per row.
"""
from __future__ import annotations
import html, json, os, re, sys

E = html.escape
CSS = """
:root{--bg:#fff;--fg:#111;--mut:#333;--line:#bbb;--bar:#1e3a8a;--bar2:#6b7280;--ok:#0b5a2a;--warn:#6b4400;--bad:#8b0000;--card:#f4f4f5}
@media (prefers-color-scheme:dark){:root{--bg:#0d1117;--fg:#f0f3f6;--mut:#d0d7de;--line:#57606a;--bar:#9ecbff;--bar2:#8b949e;--ok:#7ee2a8;--warn:#ffd479;--bad:#ffaaaa;--card:#161b22}}
*{box-sizing:border-box}html{overflow-x:hidden}body{font:18px/1.55 system-ui,-apple-system,Segoe UI,sans-serif;background:var(--bg);color:var(--fg);max-width:920px;margin:0 auto;padding:1.5rem 1rem 3rem}
h1{font-size:1.75rem;line-height:1.25;margin:.2rem 0 .6rem}h2{font-size:1.25rem;margin:2rem 0 .6rem}
p,li{max-width:70ch}.lead{font-size:1.1rem}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:.75rem;margin:1rem 0}
.kpi{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:.75rem 1rem}
.kpi b{display:block;font-size:1.9rem;line-height:1.1}.kpi span{color:var(--mut);font-size:1rem}
.ok{color:var(--ok)}.warn{color:var(--warn)}.bad{color:var(--bad)}
.chart{margin:.5rem 0 1rem}.row{display:grid;grid-template-columns:minmax(120px,30%) 1fr;gap:.5rem;align-items:center;margin:.35rem 0}
.row .lab{font-size:1rem}.bars{display:flex;flex-direction:column;gap:3px}
.bar{flex:0 0 auto;height:22px;background:var(--bar);border-radius:3px;min-width:2px}.bar.b{background:var(--bar2)}
.val{font-size:.95rem;color:var(--mut);white-space:nowrap;flex:0 0 auto}.track{display:flex;align-items:center;gap:.5rem}.bw{flex:1 1 auto;min-width:0}
.legend{font-size:.95rem;color:var(--mut)}.sw{display:inline-block;width:14px;height:14px;border-radius:2px;vertical-align:-2px;margin:0 .3rem 0 .8rem}
ol.f{padding-left:1.4rem}ol.f li{margin:.6rem 0}ol.f li b{display:block}
table{border-collapse:collapse;width:100%;font-size:1rem}th,td{border:1px solid var(--line);padding:.45rem .6rem;text-align:left;vertical-align:top}
th{background:var(--card)}.tw{overflow-x:auto}
details{margin-top:2rem}pre{white-space:pre-wrap;font-size:.9rem;background:var(--card);padding:1rem;border-radius:8px}
@media (max-width:600px){body{font-size:17px}.row{grid-template-columns:1fr}h1{font-size:1.45rem}}
"""


def slug(s: str) -> str:
    s = re.sub(r"[^\w\s-]", "", s.lower(), flags=re.U)
    return re.sub(r"[\s_]+", "-", s).strip("-")[:60] or "reporte"


def chart(c: dict) -> str:
    items = c.get("items", [])
    mx = c.get("max") or max([max(i.get("value", 0), i.get("after", 0) or 0) for i in items] or [1]) or 1
    unit = E(str(c.get("unit", "")))
    pair = any("after" in i for i in items)
    out = [f'<h2>{E(c.get("title", ""))}</h2>']
    if pair:
        out.append(f'<p class="legend"><span class="sw" style="background:var(--bar2)"></span>{E(c.get("before_label", "Before"))}'
                   f'<span class="sw" style="background:var(--bar)"></span>{E(c.get("after_label", "After"))}</p>')
    out.append('<div class="chart" role="img" aria-label="' + E(c.get("title", "")) + '">')
    for i in items:
        v = float(i.get("value", 0))
        lab = E(str(i.get("label", "")))
        tone = i.get("tone", "")
        bars = []
        if pair:
            a = float(i.get("after", v))
            bars.append(f'<div class="track"><div class="bar b" style="width:calc((100% - 4.5rem)*{v / mx:.3f})"></div><span class="val">{v:g}{unit}</span></div>')
            bars.append(f'<div class="track"><div class="bar" style="width:calc((100% - 4.5rem)*{a / mx:.3f})"></div><span class="val {tone}"><b>{a:g}{unit}</b></span></div>')
        else:
            bars.append(f'<div class="track"><div class="bar" style="width:calc((100% - 4.5rem)*{v / mx:.3f})"></div><span class="val {tone}">{v:g}{unit}</span></div>')
        out.append(f'<div class="row"><div class="lab">{lab}</div><div class="bars">{"".join(bars)}</div></div>')
    out.append("</div>")
    return "".join(out)


def build(spec: dict) -> str:
    t = spec["title"]
    p = [f'<!doctype html><html lang="{E(spec.get("lang", "en"))}"><head><meta charset="utf-8">'
         '<meta name="viewport" content="width=device-width,initial-scale=1">'
         f'<title>{E(t)}</title><style>{CSS}</style></head><body><main>',
         f"<h1>{E(t)}</h1>"]
    if spec.get("lead"):
        p.append(f'<p class="lead">{E(spec["lead"])}</p>')
    if spec.get("kpis"):
        p.append('<div class="kpis">' + "".join(
            f'<div class="kpi"><b class="{k.get("tone", "")}">{E(str(k["value"]))}</b><span>{E(k["label"])}</span></div>'
            for k in spec["kpis"]) + "</div>")
    for c in spec.get("charts", []):
        p.append(chart(c))
    if spec.get("findings"):
        p.append(f'<h2>{E(spec.get("findings_title", "Findings"))}</h2><ol class="f">' + "".join(
            f'<li><b class="{f.get("tone", "")}">{E(f["title"])}</b>{E(f.get("detail", ""))}</li>'
            for f in spec["findings"]) + "</ol>")
    if spec.get("table"):
        tb = spec["table"]
        p.append(f'<h2>{E(tb.get("title", "Detail"))}</h2><div class="tw"><table><tr>' +
                 "".join(f"<th>{E(str(h))}</th>" for h in tb["head"]) + "</tr>" +
                 "".join("<tr>" + "".join(f"<td>{E(str(x))}</td>" for x in r) + "</tr>" for r in tb["rows"]) +
                 "</table></div>")
    for s in spec.get("sections", []):
        p.append(f'<h2>{E(s["h"])}</h2>{s.get("html", "")}')
    if spec.get("evidence"):
        p.append(f'<details><summary>{E(spec.get("evidence_title", "Evidence"))}</summary><pre>{E(spec["evidence"])}</pre></details>')
    p.append("</main></body></html>")
    return "\n".join(p)


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    spec = json.load(sys.stdin if sys.argv[1] == "-" else open(sys.argv[1]))
    if not (spec.get("kpis") or spec.get("charts") or spec.get("table")):
        # An HTML of plain text is the same as a chat message. Refuse it.
        sys.exit("report.py: spec needs kpis, charts or table (text-only HTML is refused; write a short message instead)")
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
        os.path.expanduser(os.environ.get("EXPLAIN_OUTPUT_DIR", "explain")), f"{slug(spec['title'])}.html")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    open(out, "w").write(build(spec))
    print(out)


if __name__ == "__main__":
    main()
