# Rung 3 — Single-file HTML

Fast path (< 1 s): write a JSON spec, run the generator, send the file.

```bash
python3 scripts/report.py spec.json
# -> ./explain/<slug>.html, or $EXPLAIN_OUTPUT_DIR/<slug>.html  (prints the path)
```

Spec keys: `title` (the verdict), `lead` (1-2 sentences with the deciding numbers), `kpis`, `charts`
(bars; add `after` for before/after pairs), `findings` (title + detail + tone `ok|warn|bad`),
`table`, `sections` (trusted HTML), `evidence` (folded). Full example in the script docstring.
Set `lang` and the `*_title` / `*_label` keys for a language other than English.

- Output is static: no JS, no network, no external fonts. AAA contrast, light and dark, one column under 600 px.
- Titles state the takeaway: "3 sites return 404", not "SEO report".
- Reply: rung 1 summary (≤ 6 lines), then the path. Attach the file if the environment can send files.
- Do not commit the report unless the user asks.
- Optional review pass: `scripts/render.sh shot out.html out.png 390` (~2 s, needs Playwright). Look at the PNG once; `scrollWidth` must equal the width.
- Hand-written HTML is fine when the spec does not fit. Keep the same rules.
