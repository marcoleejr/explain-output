# Rung 4 — Explainer video (on request only)

- Put the script in the reply as rung 1 text, then render.
- Length the user asks for; otherwise as short as the script needs, 20 to 60 seconds. 16:9 for lessons, 9:16 for short-form.
- Animation: Manim, or HTML/SVG captured with ffmpeg. Narration: if `ELEVENLABS_API_KEY` is set, use ElevenLabs. Otherwise use local or free TTS (macOS `say`, Piper). No TTS: script plus silent animation.
- Never print or log an API key. Read it from the environment.
- Sync: generate audio per scene first, measure each clip, then time the visuals to the audio.
- "Teach" or "explain to a class" without the word video gets rung 1, plus rung 2 if there is a flow.
