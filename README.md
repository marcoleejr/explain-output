# explain-output

An [Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) that makes an agent pick the clearest output format for a reply.

It uses a 4-rung ladder, inspired by a 2 Oct 2026 post by Andrej Karpathy on X:

1. **Constrained text** (about 80% ASD-STE100): result first, short sentences, active voice, concrete numbers.
2. **Diagram**: Mermaid or rendered image, when the content is relationships.
3. **Single-file HTML**: verdict on top, tables and status colors, for more than 3 findings or any data.
4. **Explainer video**: only for teaching or marketing, or when asked.

The agent always writes the text summary first. It escalates only when a richer format saves the reader time. It never invents data.

## Install

Copy the `explain-output/` folder into your skills directory:

- Claude Code: `~/.claude/skills/explain-output/` (personal) or `.claude/skills/explain-output/` (project)
- Other harnesses: see your harness docs for the skills path.

The folder must contain `SKILL.md`. The folder name must match the `name` field.

## Trigger

The skill activates when a reply explains, reports, summarizes, audits, reviews or compares something, or contains more than 3 findings, data, flows or timelines. You can also invoke it by name.

## Capabilities and fallbacks

The skill adapts to what the environment can do:

- No image rendering: it emits a fenced Mermaid block.
- No file sending: it writes the file and tells you how to open it.
- No screenshot tool: it skips the visual review pass.
- No TTS: it delivers the script and a silent animation.

## License

MIT
