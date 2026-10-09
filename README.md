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

<p align="center">
  <b>Your agent writes a wall of text. You asked for one number.</b><br>
  This skill makes the agent pick the format you can read fastest.
</p>

---

<p align="center">
  <img src="assets/ladder.gif" alt="A wall of text becomes constrained text, then a diagram, then an HTML report, then an explainer video" width="100%">
</p>

## The ladder

Every reply is rung 1. A higher rung is added only when its criterion is met.

| Rung | Format | Use when | Example |
|:--:|---|---|---|
| **1** | **Constrained text**<br><sub>about 80% ASD-STE100</sub> | Always. Result first, then evidence, then next step. | <img src="assets/rung-1.webp" alt="Result, evidence, next step" width="300"> |
| **2** | **Diagram or chart**<br><sub>Mermaid or one SVG</sub> | A flow with 4–12 steps, or one data series where the shape is the answer. | <img src="assets/rung-2.webp" alt="Flowchart that names the failing step" width="300"> |
| **3** | **Static HTML**<br><sub>one file, no JS</sub> | More than 6 findings, more than one chart, a large table, or you ask for a report. | <img src="assets/rung-3.webp" alt="Report with verdict, table and status colors" width="300"> |
| **4** | **Explainer video**<br><sub>narrated MP4</sub> | Only when you ask. Uses ElevenLabs if `ELEVENLABS_API_KEY` is set, else local TTS. | <img src="assets/rung-4.webp" alt="Animated explainer with captions" width="300"> |

## Install

The skill is one folder with a `SKILL.md`. Works in any harness that supports [Agent Skills](https://agentskills.io/specification).

```bash
git clone https://github.com/marcoleejr/explain-output.git
```

### Claude Code

```bash
mkdir -p ~/.claude/skills
cp -R explain-output/explain-output ~/.claude/skills/
```

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

10 data scenarios, 2 runs each, clean Pi context: right format 20 of 20 with the skill, 12 of 20 without. Replies were 50% shorter and all opened with the result.

## Credit

Idea: [Andrej Karpathy, 2 Oct 2026](https://x.com/karpathy/status/2105819303471976479).

## License

MIT. See [LICENSE](LICENSE).
