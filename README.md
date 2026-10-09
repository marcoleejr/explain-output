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

## Examples

Real replies, not edited. Claude Opus 5.5 in Pi, clean context.

### 1. Text

Plain questions get plain text: result first, no extra format.

#### When to leave for the airport

**You ask:** My flight to Madrid leaves at 7:10 am from JFK. I live 45 minutes away, I have a checked bag, and it's international. What time should I leave home?

**With the skill** (38% shorter)

> **Leave home by 3:15 am.** That gets you to JFK around 4:10 am, 3 hours before your 7:10 am departure.
>
> How the time works out:
>
> 1. **3:15 am:** Leave home. You said the drive takes 45 minutes.
> 2. **~4:00 am:** Arrive at JFK. Allow 10 minutes to park or get to the terminal.
> 3. **~4:10 am:** Start check-in and drop your bag. Most airlines stop taking checked bags on international flights 60 minutes before departure. Check your airline's exact cutoff.
> 4. **~4:45 am:** Go through security. JFK has a busy early wave of morning departures, so lines can be long.
> 5. **~6:20–6:40 am:** Boarding starts.
>
> If you want less stress, leave at 3:00 am. Don't leave later than 3:45 am, because that only leaves about 2.5 hours at the airport. Checking in online before you go and having TSA PreCheck both save time, but you still need to drop your bag in person.

<details><summary><b>Without the skill</b> (1,380 characters)</summary>

> **Leave home by about 3:15 a.m.**
>
> Here's how I got there:
> - **7:10 a.m.** Departure
> - **6:20–6:40 a.m.** Boarding usually starts 30–50 minutes before departure on international flights
> - **6:10 a.m.** Bag drop usually closes 60 minutes before departure for international flights. If you miss it, you can't check your bag.
> - **4:10 a.m.** Arrive at JFK. The standard advice for international flights is 3 hours early.
> - **~3:15 a.m.** Leave home. That's your 45-minute drive plus about 10–15 minutes extra for parking, the AirTrain, or rideshare drop-off.
>
> Some notes:
> - **Traffic should be light that early,** so 45 minutes is a fair estimate. If you're parking in long-term lots and taking the AirTrain, add another 15–20 minutes and leave around 3:00 a.m.
> - **Check-in counters may not be open yet** if you arrive before about 4:00 a.m., since some airlines open 3 hours before departure. That's another reason not to come much earlier.
> - **You could leave closer to 3:45 a.m.** if you have TSA PreCheck or Global Entry, check in online, and are fine with less buffer. That's cutting it close for an international flight with a checked bag, though, especially if the bag drop line is long.
> - **Look up your airline and terminal.** Iberia, Delta, and American fly JFK–Madrid out of different terminals, and their bag drop cutoffs can vary a bit.
>
> Have a great trip to Madrid! ✈️

</details>

#### Message to a landlord

**You ask:** Write a short message to my landlord. The kitchen sink has leaked for 4 days. I sent a photo on Monday and got no answer.

**With the skill** (34% shorter)

> Hi [Landlord's name],
>
> Our kitchen sink has leaked for 4 days now. I sent you a photo of it on Monday but have not heard back. Please arrange a repair as soon as possible, before the water causes more damage. Can you tell me by [day] when someone can come?
>
> Thanks,<br>
> [Your name]<br>
> [Unit / address]

<details><summary><b>Without the skill</b> (445 characters)</summary>

> Here's a draft:
>
> ---
>
> Hi [Landlord's name],
>
> The kitchen sink has been leaking for 4 days now. I sent you a photo on Monday but haven't heard back. Could you let me know today when someone can come fix it? I'm worried about water damage to the cabinet and floor if it keeps going.
>
> I'm usually available [times/days]. Thanks.
>
> [Your name]
> [Unit/address]
>
> ---
>
> If you want it firmer, you could add: "Please treat this as a formal repair request."

</details>

### 2. Chart

One data series whose shape is the answer, so the skill adds a chart.

**You ask:** My electricity bills in USD for the last 12 months: Jan 92, Feb 88, Mar 71, Apr 64, May 79, Jun 118, Jul 141, Aug 146, Sep 112, Oct 70, Nov 74, Dec 95. Why is it so high some months, and what is my yearly total?

> Your yearly total is **$1,150**, which averages to about $96 a month. Your bills are high in summer. June to September cost $517, which is 45% of the year.
>
> | Season | Months | Average per month |
> |---|---|---|
> | Summer | Jun–Sep | $129 |
> | Winter | Dec–Feb | $92 |
> | Spring and fall | Mar–May, Oct–Nov | $72 |

<img src="assets/ex-chart.webp" alt="Bar chart of 12 monthly electricity bills with June to September in red" width="700">

### 3. HTML report

Six options with 6 attributes each, and a report request, so the skill writes one static HTML file.

**You ask:** Help me pick an apartment and give me a report. A: $1,450, 62 m2, 25 min commute, 3rd floor no elevator, pets ok, no parking. B: $1,620, 70 m2, 15 min, elevator, no pets, parking. C: $1,380, 55 m2, 40 min, ground floor, pets ok, parking. D: $1,700, 80 m2, 20 min, elevator, pets ok, no parking. E: $1,520, 65 m2, 30 min, 2nd floor, no pets, parking. F: $1,410, 58 m2, 35 min, elevator, pets ok, parking. I have a dog and I drive to work.

> I recommend apartment F. It's $1,410 for 58 m², with a 35 min commute, an elevator, pets allowed and parking.

<img src="assets/ex-html.webp" alt="Static HTML report: verdict, filter table and finalist comparison" width="700">

### 4. Video

Only because you ask for one. Narration by ElevenLabs.

**You ask:** Make a 20-second video that shows how saving $200 a month grows over 10 years at 7% a year, compared with keeping it in cash. Use ffmpeg (it is on the PATH) and narrate it. Save the MP4 in this directory.

> The video is ready: `savings-200-month-10-years.mp4`. It runs exactly 20 seconds at 1280×720 and has a voiceover.
>
> **Result:** after 10 years, cash holds $24,000 and the 7% account holds $34,617. That is $10,617 more, from growth alone.

https://github.com/user-attachments/assets/42d58daf-66ba-4430-bd7b-3829e2544818

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
