<p align="center">
  <img src="assets/hero.webp" alt="explain-output — an Agent Skill that makes your agent answer in the format you understand fastest" width="100%">
</p>

<p align="center">
  <a href="#install"><img alt="Agent Skill" src="https://img.shields.io/badge/Agent%20Skill-SKILL.md-0d0e0b?style=flat-square"></a>
  <a href="#install"><img alt="Claude Code" src="https://img.shields.io/badge/Claude%20Code-%E2%9C%93-0d0e0b?style=flat-square"></a>
  <a href="#codex"><img alt="Codex" src="https://img.shields.io/badge/Codex-%E2%9C%93-0d0e0b?style=flat-square"></a>
  <a href="#pi"><img alt="Pi" src="https://img.shields.io/badge/Pi-%E2%9C%93-0d0e0b?style=flat-square"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-ffb547?style=flat-square"></a>
</p>

## The ladder

Every reply is rung 1. A higher rung is added only when its criterion is met.

| Rung | Format | Use when | Example |
|:--:|---|---|---|
| **1** | **Constrained text**<br><sub>about 80% ASD-STE100</sub> | Always. Result first, then evidence, then next step. | <img src="assets/rung-1.webp" alt="Result, evidence, next step" width="300"> |
| **2** | **Diagram or chart**<br><sub>Mermaid or one SVG</sub> | A flow with 4–12 steps, or one data series where the shape is the answer. | <img src="assets/rung-2.webp" alt="Flowchart that names the failing step" width="300"> |
| **3** | **Static HTML**<br><sub>one file, no JS</sub> | More than 6 findings, more than one chart, a table over 5 columns or 15 rows, or you ask for a report. | <img src="assets/rung-3.webp" alt="Report with verdict, table and status colors" width="300"> |
| **4** | **Explainer video**<br><sub>narrated MP4</sub> | Only when you ask. Uses ElevenLabs if `ELEVENLABS_API_KEY` is set, else local TTS. | <img src="assets/rung-4.webp" alt="Animated explainer with captions" width="300"> |

## Before and after

Real, unedited replies. Same model (Claude Opus 5.5 in Pi), same prompt, clean context. Same answer, less to read.

### Pick a model

**Prompt:** Compare 3 fraud classifiers. A: precision 0.91, recall 0.78, F1 0.84. B: 0.86, 0.88, 0.87. C: 0.93, 0.70, 0.80. Missing a fraud is expensive. Which one should we ship?

<details><summary><b>Without the skill</b> — 2,042 chars (click to open)</summary>

> **Ship B.** It has the highest recall (0.88), and recall is the metric that matters when missing fraud is expensive.
>
> ### How many frauds each model misses
>
> Recall is the share of real frauds that a model catches. Out of every 100 real frauds:
>
> | Model | Frauds caught | Frauds missed | False alarms (≈ caught/precision − caught) |
> |---|---|---|---|
> | A | 78 | 22 | ~7.7 |
> | **B** | **88** | **12** | ~14.3 |
> | C | 70 | **30** | ~5.3 |
>
> - **B vs A:** B catches 10 more frauds and raises about 6.6 more false alarms. That's a good trade unless one false alarm costs more than about 1.5× one missed fraud. If missing fraud is expensive, it almost certainly doesn't.
> - **C is the worst option here.** It has the highest precision (0.93), but it misses 30% of fraud. Its F1 is also the lowest (0.80).
> - B's F1 (0.87) is the best of the three, so it doesn't give up overall balance to get its recall.
>
> ### Checks before shipping
>
> 1. **Threshold tuning.** These numbers come from one decision threshold per model. A's precision is higher, so lowering its threshold might get it to 0.88 recall with better precision than B. Compare the full precision-recall curves, or precision at your target recall, rather than these single points.
> 2. **Put a cost on each error.** If you can estimate the cost of a missed fraud and the cost of a false alarm (like a manual review or a blocked customer), pick the model and threshold that minimize total expected cost. You can also use an F-beta score with β > 1, which weights recall more heavily.
> 3. **Statistical significance.** Make sure all three were evaluated on the same held-out test set and that it contains enough fraud cases. Fraud data is usually highly imbalanced, so a 0.88 vs 0.78 recall gap based on only a few hundred frauds could be noise. Bootstrapped confidence intervals would show this.
> 4. **Review capacity.** B flags about 7% more transactions overall. Check that your review team or downstream process can handle the extra volume.
>
> If none of those checks changes the picture, go with B.

</details>

**With the skill** — 987 chars, 52% shorter

> Ship **B**. It has the highest recall (0.88), so it misses the fewest frauds.
>
> | Model | Precision | Recall | F1 | Frauds missed per 100 | False alarms per 100 flags |
> |---|---|---|---|---|---|
> | A | 0.91 | 0.78 | 0.84 | 22 | 9 |
> | **B** | 0.86 | **0.88** | **0.87** | **12** | 14 |
> | C | 0.93 | 0.70 | 0.80 | 30 | 7 |
>
> - **B against A:** B misses 10 fewer frauds per 100. The cost is 5 more false alarms per 100 flags.
> - **C:** do not ship it. It misses 30 of every 100 frauds, which is the worst result. Its high precision does not make up for this when a miss is expensive.
> - **F1:** B also has the best F1. That score weights precision and recall equally, but your costs are not equal. Recall is the deciding number here.
>
> Next step: check that your team can review the extra false alarms. If a missed fraud costs much more than reviewing a false alarm, B is clearly the right choice. You can also lower B's decision threshold to catch more fraud, if the team can handle more alerts.

### Read an A/B test

**Prompt:** Checkout A/B test. Variant A: 213 conversions out of 5,200 visits. Variant B: 235 out of 5,100. Is the difference statistically significant at 95%?

<details><summary><b>Without the skill</b> — 1,244 chars (click to open)</summary>

> **No, the difference is not statistically significant at the 95% level.**
>
> | | Conversions | Visits | Rate |
> |---|---|---|---|
> | A | 213 | 5,200 | 4.10% |
> | B | 235 | 5,100 | 4.61% |
>
> **Two-proportion z-test (two-sided):**
> - Difference: +0.51 percentage points, which is about a 12.5% relative lift for B.
> - Pooled rate: 448 / 10,300 = 4.35%
> - Standard error: √[0.0435 × 0.9565 × (1/5200 + 1/5100)] ≈ 0.00402
> - **z ≈ 1.27, p ≈ 0.20**
>
> To be significant at 95%, z would need to be at least 1.96, or p would need to be 0.05 or lower.
>
> **95% confidence interval for B − A:** −0.28 pp to +1.30 pp. The interval includes zero, so the data fits B being slightly worse, about the same, or meaningfully better than A.
>
> **What to do next:** The test is underpowered for an effect this size. To reliably detect a 12.5% relative lift from a 4.1% baseline (95% confidence, 80% power), you'd need about **25,000 visits per variant**. That's roughly 5 times what you have now.
>
> Decide the total sample size before you continue. Don't stop the test the moment p drops below 0.05, because checking repeatedly and stopping early makes false positives more likely. If you need to make a call now, B looks promising, but this result doesn't show that it's better.

</details>

**With the skill** — 923 chars, 26% shorter

> No, the difference is not statistically significant at 95%. The p-value is 0.20, and the 95% threshold requires p < 0.05.
>
> | | Visits | Conversions | Rate |
> |---|---|---|---|
> | A | 5,200 | 213 | 4.10% |
> | B | 5,100 | 235 | 4.61% |
>
> - **Lift:** B is 0.51 percentage points higher than A, which is +12.5% relative.
> - **Test:** I used a two-proportion z-test with a two-sided alternative. z = 1.27 and p = 0.203.
> - **95% confidence interval for B − A:** −0.28 to +1.30 percentage points. The interval includes 0, so the data does not rule out "no difference" or a small loss.
>
> **Next step:** Keep the test running. To reliably detect a lift of this size (4.1% → 4.6%) at 95% confidence and 80% power, you need about 25,000 visits per variant. That is roughly 5 times the current sample. Set the sample size before you check again. If you stop the test the first time p drops below 0.05, the chance of a false positive goes up.

## Install

Works in any harness that supports [Agent Skills](https://agentskills.io/specification).

```bash
git clone https://github.com/marcoleejr/explain-output.git
```

### Claude Code

```bash
mkdir -p ~/.claude/skills
cp -R explain-output/explain-output ~/.claude/skills/
```

Invoke with `/explain-output`, or let Claude pick it from the description.

### Codex

Codex reads the shared Agent Skills folder.

```bash
mkdir -p ~/.agents/skills
cp -R explain-output/explain-output ~/.agents/skills/
```

Restart Codex. Invoke with `$explain-output`.

### Pi

```bash
pi install git:github.com/marcoleejr/explain-output
```

Invoke with `/skill:explain-output`.

## Tested

10 data scenarios, 2 runs each, clean Pi context: right format 20 of 20 with the skill (v2.3), 12 of 20 without. Replies were 50% shorter and all opened with the result.

## Credit

Idea: [Andrej Karpathy, 2 Oct 2026](https://x.com/karpathy/status/2105819303471976479).

## License

MIT. See [LICENSE](LICENSE).
