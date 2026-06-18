#!/usr/bin/env python3
"""
Forest / Nature / Rain Relaxation 30分動画生成（Cafe 004 と同一ブランド仕様）

- 背景: forest_rain_001.png（霧の森＋渓流）
- 音声: forest_relaxation_30min_master.m4a（過去音源4曲をクロスフェード連結・30分済み）
- Ken Burns（nature 向け: ゆっくりズーム+ドリフト）+ 霧の光揺らぎ + ビネット
- 冒頭5秒イントロ（中央 "LATTE BGM" / "Music for Every Moment"）
- 右上ロゴ: 犬アイコン + LATTE BGM 文字（別レイヤー・スマホ可読）
- テキストは PIL生成の透過PNGを overlay 合成（このffmpegは drawtext 非対応）
- 出力: 1920x1080 / H.264 / AAC / 30分
"""
import subprocess, os, sys

ROOT   = "/Users/khhr/Desktop/latte-ecosystem"
IMAGE  = f"{ROOT}/assets/latte_bgm/images/organized/08_Nature_Forest_Rain/forest_rain_001.png"
AUDIO  = f"{ROOT}/assets/latte_bgm/audio/built/forest_relaxation_30min_master.m4a"
ICON   = f"{ROOT}/assets/latte_bgm/images/brand/latte_dog_icon_circle_v2.png"
BRAND  = f"{ROOT}/assets/latte_bgm/images/brand/latte_brand_text.png"      # 250x80
INTRO  = f"{ROOT}/assets/latte_bgm/images/brand/latte_intro_overlay.png"   # 1920x1080
OUTPUT = f"{ROOT}/assets/latte_bgm/videos/final/forest_relaxation_30min_002.mp4"

D    = 1800
W, H = 1920, 1080

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

# ── Ken Burns (nature: ややダイナミックだが穏やか) ─────────
z_start, z_end = 1.00, 1.12
z_rng = z_end - z_start
sw = int(W * z_end); sw += sw % 2        # 2150
sh = int(H * z_end); sh += sh % 2        # 1210

pan      = 0.15
avail_x  = (sw - W) / 2.0
max_pan  = avail_x * 0.50
safe_pan = min(pan, max_pan / D)

crop_w = f"{W}*({z_end:.4f}-{z_rng:.4f}*min(t\\,{D})/{D})"
crop_h = f"{H}*({z_end:.4f}-{z_rng:.4f}*min(t\\,{D})/{D})"
pan_e  = f"+{safe_pan:.5f}*t"
crop_x = f"max(0\\,min({sw}-({crop_w})\\,({sw}-({crop_w}))/2{pan_e}))"
crop_y = f"({sh}-({crop_h}))/2"
crop_f = f"crop=w='{crop_w}':h='{crop_h}':x='{crop_x}':y='{crop_y}'"

# ── 霧の光揺らぎ (gentle light_flicker) ────────────────────
brightness, contrast, saturation = 0.02, 1.00, 1.08
flicker_speed, flicker_amp = 0.5, 0.025
spd2 = round(flicker_speed * 1.7321, 4)
bright_expr = f"{brightness:.4f}+{flicker_amp:.4f}*sin(t*{flicker_speed:.3f})*sin(t*{spd2})"
eq_f = (f"eq=brightness='{bright_expr}'"
        f":contrast={contrast:.2f}:saturation={saturation:.2f}:eval=frame")

vignette = "vignette=angle=PI/4:mode=backward"

# ── 右上ロゴ配置（Cafe 004 と同一）────────────────────────
ICON_DIAM = 160
ICON_CX   = 1785
ICON_X    = ICON_CX - ICON_DIAM // 2
ICON_Y    = 22
BRAND_W   = 250
BRAND_X   = ICON_CX - BRAND_W // 2
BRAND_Y   = ICON_Y + ICON_DIAM + 2

intro_fade = "format=rgba,fade=t=in:st=0:d=1:alpha=1,fade=t=out:st=4:d=1:alpha=1"

bg_chain = f"scale={sw}:{sh},{crop_f},scale={W}:{H},{eq_f},{vignette}"
filter_complex = (
    f"[0:v]{bg_chain}[bg];"
    f"[1:v]{intro_fade}[intro];"
    f"[2:v]scale={ICON_DIAM}:{ICON_DIAM}[ic];"
    f"[bg][ic]overlay=x={ICON_X}:y={ICON_Y}[b1];"
    f"[b1][3:v]overlay=x={BRAND_X}:y={BRAND_Y}[b2];"
    f"[b2][intro]overlay=x=0:y=0:enable='lte(t,5)',format=yuv420p[outv]"
)

print("=" * 60)
print("  Latte BGM — Forest Relaxation 30min 動画生成")
print("=" * 60)
print(f"  画像  : {IMAGE}")
print(f"  音声  : {AUDIO}")
print(f"  出力  : {OUTPUT}")
print()

for p in (IMAGE, AUDIO, ICON, BRAND, INTRO):
    if not os.path.exists(p):
        print(f"[ERROR] 素材が見つかりません: {p}"); sys.exit(1)

print("[1/1] 動画生成中 (slow encode, 約10〜20分)...")
cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-i", IMAGE,   # [0] 背景
    "-loop", "1", "-i", INTRO,   # [1] 中央イントロ
    "-i", ICON,                  # [2] 犬アイコン
    "-i", BRAND,                 # [3] LATTE BGM 文字
    "-i", AUDIO,                 # [4] 音声（既に30分）
    "-filter_complex", filter_complex,
    "-map", "[outv]", "-map", "4:a",
    "-c:v", "libx264", "-preset", "slow", "-crf", "20",
    "-c:a", "aac", "-b:a", "192k", "-ar", "44100",
    "-r", "30", "-t", str(D),
    "-movflags", "+faststart",
    "-metadata", "title=Latte BGM | 30 Min Relaxing Rain & Forest Music | Nature BGM for Focus",
    OUTPUT,
]
result = subprocess.run(cmd, capture_output=True, text=True)
if result.returncode != 0:
    print(f"[ERROR] ffmpeg 失敗:\n{result.stderr[-1000:]}"); sys.exit(1)

size_mb = os.path.getsize(OUTPUT) / (1024 * 1024)
print(f"\n[DONE] 生成完了!")
print(f"  出力  : {OUTPUT}")
print(f"  サイズ: {size_mb:.1f} MB")
