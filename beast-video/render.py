#!/usr/bin/env python3
"""
THIS FUCKING BEAST — lyric video renderer (optional, needs ffmpeg + Pillow).

Renders a simple 1280x720 MP4 from:
  - your audio master (mp3/wav)
  - the beast artwork in assets/
  - the timed lyrics below (same timings as index.html)

Usage:
  pip install Pillow
  python3 beast-video/render.py --audio your-master.mp3 --out beast.mp4

If ffmpeg isn't installed, install it (https://ffmpeg.org/download.html)
or just use the browser prototype (index.html) and screen-record instead.
"""
import argparse, os, subprocess, sys, textwrap

# Keep in sync with CUES in index.html
CUES = [
    (0,   "INTRO", "THIS FUCKING BEAST!"),
    (8,   "VERSE 1", "The iron snaps, the shadows rise"),
    (14,  "VERSE 1", "The hunger grows, it burns the night"),
    (20,  "VERSE 1", "This fucking beast!"),
    (38,  "CHORUS", "Don't mistake my kindness for weakness!"),
    (44,  "CHORUS", "It's awake, it thrives on pain"),
    (50,  "CHORUS", "This fucking beast!"),
    (56,  "VERSE 2", "Your time is gone, the die is cast"),
    (86,  "CHORUS", "Don't mistake my kindness for weakness!"),
    (104, "BRIDGE", "The storm is here, the chains are dust"),
    (116, "GUITAR SOLO", "DUAL GUITAR SOLO"),
    (132, "BREAKDOWN", "You woke the beast!"),
    (150, "FINAL CHORUS", "Don't mistake my kindness for weakness!"),
    (168, "OUTRO", "This... fucking... beast!"),
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audio", required=True, help="path to mp3/wav master")
    ap.add_argument("--out", default="beast.mp4")
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--height", type=int, default=720)
    args = ap.parse_args()

    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        sys.exit("Pillow not installed. Run: pip install Pillow")

    if subprocess.run(["which", "ffmpeg"], capture_output=True).returncode != 0:
        sys.exit("ffmpeg not found. Install it or use the browser prototype instead.")

    here = os.path.dirname(os.path.abspath(__file__))
    assets = os.path.join(here, "assets")
    bg_path = os.path.join(assets, "beast-hero.jpg")
    if not os.path.exists(bg_path):
        sys.exit(f"Artwork not found: {bg_path}")

    # Probe duration
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", args.audio],
        capture_output=True, text=True)
    duration = float(probe.stdout.strip() or 207)  # true master is 3:27

    # Render frames at 10fps (good enough for lyric video, fast to render)
    fps = 10
    frames_dir = os.path.join(here, "_frames")
    os.makedirs(frames_dir, exist_ok=True)

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)
        small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    except Exception:
        font = ImageFont.load_default()
        small = font

    bg = Image.open(bg_path).convert("RGB").resize((args.width, args.height))
    n_frames = int(duration * fps)
    for i in range(n_frames):
        t = i / fps
        cue = max([c for c in CUES if c[0] <= t], key=lambda c: c[0], default=CUES[0])
        frame = bg.copy()
        draw = ImageDraw.Draw(frame, "RGBA")
        draw.rectangle([0, 0, args.width, args.height], fill=(0, 0, 0, 110))
        # section tag
        draw.text((24, 20), cue[1], fill=(255, 179, 71, 255), font=small)
        # lyric (wrapped, centered)
        lines = textwrap.wrap(cue[2].upper(), width=28)
        y = args.height // 2 - (len(lines) * 72) // 2
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font)
            w = bbox[2] - bbox[0]
            draw.text(((args.width - w) // 2, y), line, fill=(255, 255, 255, 255), font=font)
            y += 72
        frame.save(os.path.join(frames_dir, f"f{i:05d}.png"))
        if i % 100 == 0:
            print(f"frame {i}/{n_frames}", flush=True)

    subprocess.run([
        "ffmpeg", "-y", "-framerate", str(fps),
        "-i", os.path.join(frames_dir, "f%05d.png"),
        "-i", args.audio, "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-shortest", args.out
    ], check=True)
    print(f"Done: {args.out}")

if __name__ == "__main__":
    main()
