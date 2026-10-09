# Rung 3 — Single-file HTML

- One self-contained `.html` file. Inline CSS. No build step, no CDN, no external fonts or images.
- It must render with JavaScript off: chat-app previews, email and iOS Quick Look block scripts and network. Draw charts as inline SVG or CSS bars, never canvas or a chart library. JS only for optional extras such as sorting.
- Top: verdict in 3 lines plus key numbers. Detail below in `<details>`. Green, amber, red status.
- Mobile: one column under 600px, text at least 16px.
- Path: `explain/<slug>.html` under the project root (create the folder). With no project, use the system temp folder. Do not commit it unless the user asks.
- Reply with the rung 1 summary, then the path. Attach the file if the environment can send files.
- Review pass only if a screenshot tool is already available: one pass, layout only, not mentioned in the reply.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Verdict: fix the cache key</title>
<style>
body{font:16px/1.5 system-ui;max-width:900px;margin:2rem auto;padding:0 1rem}
.ok{color:#15803d}.warn{color:#b45309}.bad{color:#b91c1c}
table{border-collapse:collapse;width:100%}td,th{border:1px solid #ddd;padding:.5rem}
</style></head><body>
<h1>Verdict: fix the cache key</h1>
<p><b>4 of 5</b> failed runs used a stale cache. One change fixes it.</p>
<table><tr><th>Finding</th><th>Status</th><th>Action</th></tr>
<tr><td>Cache key ignores lockfile</td><td class="bad">Blocking</td><td>Add lockfile hash</td></tr></table>
<details><summary>Evidence</summary><pre>...tool output...</pre></details>
</body></html>
```
