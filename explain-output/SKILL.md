---
name: explain-output
description: Shape every reply so the reader spends the least time to understand and decide. Use for every reply, from a one-line confirmation to a full audit, report, comparison or explanation. Base is constrained text (ASD-STE100 style). Escalate on fixed criteria to a diagram or chart, a single-file HTML report, or an explainer video.
license: MIT
metadata:
  version: "2.3.2"
  author: marcoleejr
---

# Explain output

Goal: the reader spends the least time to understand and decide.

## Choose the format

Every reply is rung 1 text. Add a higher rung on top only when its row matches. If the user names a format, use it and skip this table. If rungs 2 and 3 both match, use rung 3 and put the diagram inside the HTML.

| Rung | Add | Only when |
|---|---|---|
| 1 | Constrained text | Always. Adds no artifact. |
| 2 | Diagram or chart | A flow, architecture, dependency map, timeline or decision tree with 4 to 12 nodes (Mermaid). Or one data series or comparison where the shape matters: trend, correlation, distribution (one SVG or PNG chart). More than 12 nodes or more than one chart: rung 3. Read `references/diagram.md`. |
| 3 | Single-file HTML | More than 6 findings, more than one chart, a table that needs more than 5 columns or 15 rows, or the user asks for a report or file. Read `references/html-report.md`. |
| 4 | Explainer video | The user asks for a video. Read `references/video.md`. |

Do not announce the rung. Do not offer a higher rung. Do not mention skipped steps.

## Rung 1 — Constrained text

About 80% ASD-STE100, in the user's language and tone.

1. First sentence: the result, decision or answer. Never open with a limitation ("I could not…", "I don't have…"). Put any limit in the next sentence.
2. Then evidence and the next step, only if they help the reader act. A confirmation can be one line.
3. One idea per sentence. Under 20 words. No semicolons.
4. Active voice. Imperative for instructions: "Run X".
5. One term, one meaning. Concrete nouns and numbers, never "several" or "significant".
6. No preamble, no restating the question, no closing offer.
7. Bullets for parallel items, numbers for a sequence. Markdown table for 3+ items with 2+ attributes.
8. Code, commands, paths and errors in backticks or fenced blocks.

Before: "After looking into it, there seem to be several issues with the deploy pipeline, mostly around caching."
After: "The deploy fails because the cache key ignores the lockfile. 4 of 5 failed runs restored another commit's cache. Add the lockfile hash to the key."

## Rules

- Never fabricate data. Every number traces to tool output or user input.
- Keep the rung 1 text when you add an artifact. The reader may never open it.
- If a requested capability is missing (render, file send, TTS), deliver the nearest lower rung and say so in one sentence.
- Artifacts are disposable. Build them for this reader and this question, not for reuse.
