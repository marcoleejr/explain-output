# Rung 4 — Explainer video (on request only)

- Write the script as rung 1 text first. Get approval before rendering.
- Length the user asks for; default 60 to 120 seconds. 16:9 for lessons, 9:16 for short-form.
- Animation: Manim, or HTML/SVG captured with ffmpeg. Narration: if `ELEVENLABS_API_KEY` is set, use ElevenLabs. Otherwise use local or free TTS (macOS `say`, Piper). No TTS: script plus silent animation.
- Never print or log an API key. Read it from the environment.
- Sync: generate audio per scene first, measure each clip, then time the visuals to the audio.
- "Teach" or "explain to a class" without the word video gets rung 1, plus rung 2 if there is a flow.
