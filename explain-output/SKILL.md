---
name: explain-output
description: Shape every reply so the reader spends the least time to understand and decide. Use for every reply, from a one-line confirmation to a full audit, report, comparison or explanation. Base is constrained text (ASD-STE100 style). Escalate on fixed counts to a diagram or chart, a single-file HTML report, or an explainer video.
license: MIT
metadata:
  version: "3.0.0"
  author: marcoleejr
---

# Explain output

Goal: the reader understands and decides in the least time.

## Checklist — run it on the draft, right before you send it

1. **Result first.** Sentence 1 = the answer, decision or status. Not "I will…", "I checked…", "I could not…".
2. **Count the list items** (bullets + numbered lines) in the draft. More than 6 → rung 3 HTML. A flow of 4–12 steps or boxes → rung 2 diagram. Otherwise text only.
3. **Longest sentence ≤ 20 words.** Split at "and", "but", "because", ":" and ";". One idea per sentence.
4. **Chat app:** ≤ 12 lines, the user's language, no jargon. Say "change" for PR, "published" for merge, "scheduled task" for cron.
5. **No offer.** Never ask "do you want a report or a diagram?". Do the rung or skip it.

A short reply (≤ 6 items, ≤ 12 lines) stays text. Never escalate it.

## Rungs

| Rung | When | How (≤ 30 s) |
|---|---|---|
| 1 Text | Always | Checklist. Bullets = parallel, numbers = sequence. Code and paths in backticks. |
| 2 Diagram / chart | Flow with 4–12 nodes, or one data series whose shape is the answer | `scripts/render.sh mmd in.mmd out.png` (~5 s). Details: `references/diagram.md`. Concept or mechanism (how or why something works) → 3Blue1Brown style: `render.sh mmd3b`. |
| 3 HTML | > 6 items, > 1 chart, table > 5 columns or > 15 rows, or the user asks for a report | `scripts/report.py spec.json` (< 1 s, static, AAA contrast). Details: `references/html-report.md`. |
| 4 Video | Only when the user asks | `references/video.md`. |

If the user names a format, use it. Rungs 2 and 3 both match → chart inside the HTML.
With an artifact, the text keeps the result + the 2–3 numbers that decide, then the file. Max 6 lines. The reader may never open the file.

An HTML report must carry real KPIs, charts or a table. An HTML of plain text is the same as a message; `report.py` refuses text-only specs. One topic per message; secondary items in 1 line at the end.

## Rung 1 — Constrained text

About 80% ASD-STE100, in the user's language and tone.

1. Evidence and the next step follow the result, only if they help the reader act. A confirmation can be one line.
2. Active voice. Imperative for instructions: "Run X".
3. One term, one meaning. Concrete nouns and numbers, never "several" or "significant".
4. No preamble, no restating the question, no closing offer.
5. Markdown table for 3+ items with 2+ attributes.

## Examples

Bad — 18 items as text, 26 lines:
"**Donor Nearby**: when a family needs blood donors… **Why here:** - Only 3.76%… (17 more bullets)"
Good — 4 lines + file:
"I propose Donor Nearby: it alerts compatible donors near the hospital. Only 3.76% of blood comes from voluntary donors. Sources and plan are in the report: `explain/donor-nearby.html`"

Bad (jargon): "Merged #339 and the news-sitemap is no longer empty."
Good: "I published the fix. The news map for Google is no longer empty."

Before: "After looking into it, there seem to be several issues with the deploy pipeline, mostly around caching."
After: "The deploy fails because the cache key ignores the lockfile. 4 of 5 failed runs restored another commit's cache. Add the lockfile hash to the key."

## Rules

- Never fabricate data. Every number traces to tool output or user input.
- If a render fails or a capability is missing, send the text and say so in one sentence.
- Do not announce the rung. Do not mention skipped steps.
- Artifacts are disposable. Build them for this reader and this question, not for reuse.
