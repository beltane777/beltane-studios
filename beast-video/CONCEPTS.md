# THE BEAST UNCHAINED — Music Video Concepts

**Track:** "The Beast Unchained" by DeathPiggy • 3:27 • C# 80s galloping twin-guitar metal (Slayer vocals, Maiden/Priest power) • Suno: https://suno.com/s/i0pvQoQsCjuWwhFT
**Built in this repo:** `beast-video/index.html` (playable lyric-video v2) + `assets/` (7 artworks)
**Status:** Full lyrics confirmed from Suno (`LYRICS.md`). Timings rescaled to true 3:27 — nudge with −0.5s/+0.5s once you load the master. Posting copy: `POSTING.md`. Thumbnail: `thumbnail.html`.

---

## What "we can do in here" actually means

This repo has **no camera, no ffmpeg, no audio file yet** — but it has Python, Node, ImageMagick, and a browser. So the honest tiers are:

| Tier | What | Where it happens | Cost / time |
|---|---|---|---|
| **A. In-repo lyric video** ✅ BUILT | Synced lyrics + beast art + embers + visualizer, screen-recordable | This repo, right now | $0, today |
| **B. AI-visual video** | Generated beast/performance clips cut to the track | Generate images → animate in browser/editor | Low, this week |
| **C. Real shoot** | Band performance + beast creature in a real space | Garage / warehouse / forest at night | Needs people + gear |

Everything below is written so you can pick **A today, B next, C when you're ready** — same song structure, same lyric sync.

---

## The 6 concepts (ranked by "can we actually do it")

### 1. 🔥 "BEAST UNCHAINED" — Lyric Video (Tier A — DONE, playable now)
**The one you can watch in this repo.**
- Full-screen beast artwork (Ken Burns drift), ember particles rising, galloping bar visualizer.
- Lyrics slam in huge; every **"This fucking beast!"** hits with a screen shake + white flash.
- Verse = beast eyes in the dark. Chorus = fire/stage art. Bridge = chains texture. Solo = "🎸 DUAL GUITAR SOLO 🎸" card. Breakdown = glitchy texture + shake.
- **9:16 vertical toggle** built in for TikTok / Reels / Shorts.
- **How to use:** open `beast-video/index.html` → Play (demo sync) → Fullscreen → record. Or load your Suno MP3 for true sync + real visualizer.
- **Why it wins:** zero shoot, zero edit, looks intentional, and it's the fastest path to a postable video.

### 2. 👹 "WAKE THE BEAST" — AI Creature Lyric Video (Tier B)
- Generate 6–8 beast stills (eyes opening → fangs → chains snapping → full roar) with the image tool, then crossfade/push-in on each chorus.
- Lyrics stay front-and-center; beast grows bigger each chorus (Verse 1 = eyes only, Final Chorus = full beast).
- **Doable in here:** yes — generate art, animate in the HTML prototype (swap `BG_BY_SECTION`), record.
- **Best for:** YouTube + Spotify Canvas. Looks expensive, costs nothing.

### 3. 🎸 "GALLOP" — Performance Lyric Hybrid (Tier B/C)
- Film or AI-generate: two guitarists galloping (down-up-down-up), drummer pounding, singer screaming "THIS FUCKING BEAST!" straight to lens.
- Cut on the gallop: every riff hit = a cut or a punch-in. Breakdown = slow-motion headbang.
- **In-repo version:** use `assets/ember-stage.jpg` as the performance backdrop + visualizer bars synced to the riff.
- **Best for:** Fans who want to *see* the band. Even a phone in a dark room with a red light works.

### 4. ⛓️ "CHAINS ARE DUST" — Narrative Micro-Short (Tier C)
- One location, one night: a figure in a dark room, chains on the wall. Each verse adds a chain breaking. Bridge: "the chains are dust." Breakdown: figure stands, eyes glow.
- No dialogue — just the song + physical acting. Shot on a phone, lit by one red practical + ember light.
- **Shot list:** see `SHOTLIST.md`. ~20 shots, one evening.
- **Best for:** A "real" music video feel on a shoestring. The beast is *you* — the lyric "don't mistake my kindness for weakness" becomes the story.

### 5. 📱 "BEAST! — Vertical Hook Loop" (Tier A/B — 15 seconds)
- Cut the loudest 15s: Intro scream → "THIS FUCKING BEAST!" → chorus hook. Vertical 9:16, captions burned in, beast art pulsing on the beat.
- **In-repo:** toggle 9:16 in the prototype, seek to 0:00, record 15s. Done.
- **Best for:** TikTok/Reels/Shorts discovery. This is the ad for the full video.

### 6. 🎨 "LYRIC POSTER FILM" — Animated Type Video (Tier A)
- No beast face at all — just massive animated type: "DON'T MISTAKE MY KINDNESS FOR WEAKNESS" slamming in word-by-word, ember texture behind, gallop bars underneath.
- **In-repo:** the prototype already does this; push the type bigger, drop the art opacity.
- **Best for:** Spotify / Apple Music canvases, lyric-video purists, and when you want the *words* to be the star.

---

## Recommended path (my pick)

1. **Today:** Play the prototype, load your Suno master, nudge the timings, record the 16:9 + 9:16 versions. You have a video.
2. **This week:** Generate 4 more beast stills (Concept 2), swap them into `BG_BY_SECTION`, re-record. Now it looks like a real production.
3. **When ready:** Shoot Concept 4 (one night, one room) and cut it against the same lyric sync. The prototype's timings become your edit map.

---

## Song-structure → visual map (already wired in the prototype)

| Section | Visual | Lyric treatment |
|---|---|---|
| Intro | Beast hero, slow push-in | "THIS FUCKING BEAST!" — full-screen slam |
| Verse 1/2 | Beast eyes / dark | Lyrics fade in line-by-line |
| Chorus | Ember stage, fire | Shake + flash on every "BEAST!" |
| Bridge | Chains texture, dark | Spoken lines, slower, ominous |
| Guitar Solo | Stage art + solo card | "🎸 DUAL GUITAR SOLO 🎸" |
| Breakdown | Glitch texture | Shake on every hit |
| Final Chorus | Full beast, brightest | Biggest type, max shake |
| Outro | Beast fades to black | "This... fucking... beast!" whisper-out |

---

## What I need from you to finish it

- [ ] **The Suno MP3/WAV export** (drop it in the repo or load it in the player) — so timings are exact, not estimated.
- [ ] **Full lyrics** (the Suno page has them; paste the rest) — so every line is synced.
- [ ] **Your call:** which concept(s) — A only, or A+B, or full shoot?
- [ ] **Band name / logo / socials** — to brand the outro card.

Until then, the prototype runs in **Demo Sync** so you can preview the whole thing with no audio at all.
