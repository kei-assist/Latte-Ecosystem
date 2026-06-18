#!/usr/bin/env python3
"""
Boxercise 30分動画生成スクリプト
- Ken Burns (zoom + pan)
- ジム照明フリッカー
- 冒頭5秒イントロテキスト（フェードイン/アウト）
- 右上常時ブランドマーク "LATTE BGM"
- ビネット
- 出力: 1920x1080 / H.264 / AAC
"""

import subprocess, os, sys, tempfile
from pathlib import Path

# ── パス設定 ──────────────────────────────────────────────
IMAGE  = "/Users/khhr/Desktop/latte-ecosystem/assets/latte_bgm/images/organized/04_Boxercise/boxercise_005.png"
AUDIO  = "/Users/khhr/Desktop/latte-ecosystem/assets/latte_bgm/audio/source/workout_boxercise_001.mp3"
OUTPUT = "/Users/khhr/Desktop/latte-ecosystem/assets/latte_bgm/videos/final/boxercise_30min_001.mp4"
FONT   = "/System/Library/Fonts/Supplemental/Impact.ttf"
D      = 1800   # 30分
W, H   = 1920, 1080

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

# ── Ken Burns (workout_boxercise_long ベース) ──────────────
z_end   = 1.16
z_start = 1.00
z_range = z_end - z_start   # 0.16
sw = int(W * z_end); sw += sw % 2   # 2228
sh = int(H * z_end); sh += sh % 2   # 1252

pan       = 0.38
avail_x   = (sw - W) / 2.0          # 154
max_pan   = avail_x * 0.50          # 77
safe_pan  = min(abs(pan), max_pan / D)   # ≈0.04278

crop_w = f"{W}*({z_end:.4f}-{z_range:.4f}*min(t\\,{D})/{D})"
crop_h = f"{H}*({z_end:.4f}-{z_range:.4f}*min(t\\,{D})/{D})"
pan_e  = f"+{safe_pan:.5f}*t"
crop_x = f"max(0\\,min({sw}-({crop_w})\\,({sw}-({crop_w}))/2{pan_e}))"
crop_y = f"({sh}-({crop_h}))/2"
crop_f = f"crop=w='{crop_w}':h='{crop_h}':x='{crop_x}':y='{crop_y}'"

# ── 照明フリッカー ────────────────────────────────────────
brightness    = 0.02
contrast      = 1.08
saturation    = 1.10
flicker_speed = 1.6
flicker_amp   = 0.035
spd2 = round(flicker_speed * 1.7321, 4)
bright_expr = (
    f"{brightness:.4f}"
    f"+{flicker_amp:.4f}*sin(t*{flicker_speed:.3f})*sin(t*{spd2})"
)
eq_f = (
    f"eq=brightness='{bright_expr}'"
    f":contrast={contrast:.2f}"
    f":saturation={saturation:.2f}"
    f":eval=frame"
)

# ── ビネット ──────────────────────────────────────────────
vignette = "vignette=angle=PI/4:mode=backward"

# ── テキスト alpha 式 (0→1s: フェードイン, 1→4s: 表示, 4→5s: フェードアウト) ─
# ffmpeg 内部のカンマは \, としてエスケープ（Python 文字列では \\,）
a = "if(lt(t\\,1)\\,t\\,if(lt(t\\,4)\\,1\\,if(lt(t\\,5)\\,5-t\\,0)))"

# ── 冒頭イントロ: 中央大テキスト ──────────────────────────
dt_intro_main = (
    f"drawtext=fontfile='{FONT}'"
    f":text='LATTE BGM'"
    f":x=(W-tw)/2:y=H/2-70"
    f":fontsize=110:fontcolor=white"
    f":alpha='{a}'"
    f":shadowx=4:shadowy=4:shadowcolor=black@0.8"
)
dt_intro_sub = (
    f"drawtext=fontfile='{FONT}'"
    f":text='Music for Every Moment'"
    f":x=(W-tw)/2:y=H/2+55"
    f":fontsize=50:fontcolor=white"
    f":alpha='{a}'"
    f":shadowx=2:shadowy=2:shadowcolor=black@0.8"
)

# ── 常時ブランドマーク: 右上 ──────────────────────────────
dt_brand = (
    f"drawtext=fontfile='{FONT}'"
    f":text='LATTE BGM'"
    f":x=W-tw-22:y=18"
    f":fontsize=36:fontcolor=white:alpha=0.90"
    f":shadowx=2:shadowy=2:shadowcolor=black@0.8"
)

# ── フィルタチェーン組み立て ──────────────────────────────
vf = ",".join([
    f"scale={sw}:{sh}",
    crop_f,
    f"scale={W}:{H}",
    eq_f,
    vignette,
    dt_intro_main,
    dt_intro_sub,
    dt_brand,
    "format=yuv420p",
])

print("=" * 55)
print("  Latte BGM — Boxercise 30min 動画生成")
print("=" * 55)
print(f"  画像  : {IMAGE}")
print(f"  音源  : {AUDIO}")
print(f"  出力  : {OUTPUT}")
print(f"  長さ  : {D//60}分")
print(f"  Filter: {vf[:80]}...")
print()

with tempfile.TemporaryDirectory() as tmpdir:
    looped = os.path.join(tmpdir, "loop.aac")

    # 音源を30分にループ
    print(f"[1/2] 音源を{D}秒にループ中...")
    r = subprocess.run(
        ["ffmpeg", "-y", "-stream_loop", "-1", "-i", AUDIO,
         "-t", str(D), "-c:a", "aac", "-b:a", "192k", "-ar", "44100", looped],
        capture_output=True
    )
    if r.returncode != 0:
        print(f"[ERROR] 音源ループ失敗:\n{r.stderr.decode()[-300:]}")
        sys.exit(1)
    print("      完了")

    # 動画生成
    print("[2/2] 動画生成中 (slow encode, 約10〜20分かかります)...")
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", IMAGE,
        "-i", looped,
        "-vf", vf,
        "-c:v", "libx264", "-preset", "slow", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k", "-ar", "44100",
        "-r", "30", "-t", str(D),
        "-movflags", "+faststart",
        "-metadata", "title=Latte BGM | 30 Min Boxercise Workout Music | Boxing Cardio BGM",
        OUTPUT,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)

if result.returncode != 0:
    print(f"[ERROR] ffmpeg 失敗:\n{result.stderr[-600:]}")
    sys.exit(1)

size_mb = os.path.getsize(OUTPUT) / (1024 * 1024)
print(f"\n[DONE] 生成完了!")
print(f"  出力: {OUTPUT}")
print(f"  サイズ: {size_mb:.1f} MB")
