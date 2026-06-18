#!/usr/bin/env python3
"""
Cafe Warm 30分動画生成スクリプト（004 = 003 の改善版）

003 からの変更点:
  - 右上ロゴを「犬アイコン(透過PNG)」と「LATTE BGM 文字(透過PNG)」の
    別レイヤー構成に変更。文字をスマホでも読めるサイズ(50px相当・黒縁付き)に拡大。
  - それ以外のデザイン(Ken Burns / 暖色フリッカー / ビネット / 中央イントロ)
    は 003 を踏襲。

テキストは PIL で生成済みの透過 PNG を overlay で合成する
（このマシンの ffmpeg は drawtext 非対応のため）。

構成:
  - cafe_warm プリセット: ズーム 1.00→1.10 / pan 0.12 / 暖色ライト揺らぎ
  - 冒頭5秒イントロ（中央 "LATTE BGM" + "Music for Every Moment" フェード）
  - 右上常時ロゴ: 犬アイコン + LATTE BGM 文字（別レイヤー）
  - 出力: 1920x1080 / H.264 / AAC / 30分
"""

import subprocess, os, sys, tempfile

# ── パス設定 ──────────────────────────────────────────────
ROOT   = "/Users/khhr/Desktop/latte-ecosystem"
IMAGE  = f"{ROOT}/assets/latte_bgm/images/organized/07_Cafe_Warm/cafe_warm_001.png"
AUDIO  = f"{ROOT}/assets/latte_bgm/audio/source/cafe_warm_morning_001.mp3"
ICON   = f"{ROOT}/assets/latte_bgm/images/brand/latte_dog_icon_circle_v2.png"
BRAND  = f"{ROOT}/assets/latte_bgm/images/brand/latte_brand_text.png"      # 250x80
INTRO  = f"{ROOT}/assets/latte_bgm/images/brand/latte_intro_overlay.png"   # 1920x1080
OUTPUT = f"{ROOT}/assets/latte_bgm/videos/final/cafe_warm_30min_005.mp4"

D    = 1800            # 30分
W, H = 1920, 1080

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

# ── Ken Burns (cafe_warm プリセット) ───────────────────────
z_start, z_end = 1.00, 1.10
z_rng = z_end - z_start                 # 0.10
sw = int(W * z_end); sw += sw % 2       # 2112
sh = int(H * z_end); sh += sh % 2       # 1188

pan      = 0.12
avail_x  = (sw - W) / 2.0               # 96
max_pan  = avail_x * 0.50               # 48
safe_pan = min(pan, max_pan / D)        # ≈0.02667

crop_w = f"{W}*({z_end:.4f}-{z_rng:.4f}*min(t\\,{D})/{D})"
crop_h = f"{H}*({z_end:.4f}-{z_rng:.4f}*min(t\\,{D})/{D})"
pan_e  = f"+{safe_pan:.5f}*t"
crop_x = f"max(0\\,min({sw}-({crop_w})\\,({sw}-({crop_w}))/2{pan_e}))"
crop_y = f"({sh}-({crop_h}))/2"
crop_f = f"crop=w='{crop_w}':h='{crop_h}':x='{crop_x}':y='{crop_y}'"

# ── 暖色ライト揺らぎ (light_flicker) ───────────────────────
brightness, contrast, saturation = 0.03, 1.00, 1.10
flicker_speed, flicker_amp = 0.6, 0.03
spd2 = round(flicker_speed * 1.7321, 4)
bright_expr = f"{brightness:.4f}+{flicker_amp:.4f}*sin(t*{flicker_speed:.3f})*sin(t*{spd2})"
eq_f = (
    f"eq=brightness='{bright_expr}'"
    f":contrast={contrast:.2f}:saturation={saturation:.2f}:eval=frame"
)

vignette = "vignette=angle=PI/4:mode=backward"

# ── 右上ロゴ配置 ───────────────────────────────────────────
ICON_DIAM = 160
ICON_CX   = 1785                          # アイコン中心X（右寄せ）
ICON_X    = ICON_CX - ICON_DIAM // 2      # 1705
ICON_Y    = 22
BRAND_W   = 250                           # latte_brand_text.png の幅
BRAND_X   = ICON_CX - BRAND_W // 2        # 1660（アイコン中心に揃える）
BRAND_Y   = ICON_Y + ICON_DIAM + 2        # アイコン直下

# ── 中央イントロのフェード（0→1s in / 4→5s out, 5s で消える）──
intro_fade = "format=rgba,fade=t=in:st=0:d=1:alpha=1,fade=t=out:st=4:d=1:alpha=1"

# ── filter_complex 組み立て ───────────────────────────────
bg_chain = f"scale={sw}:{sh},{crop_f},scale={W}:{H},{eq_f},{vignette}"
filter_complex = (
    f"[0:v]{bg_chain}[bg];"
    f"[1:v]{intro_fade}[intro];"
    f"[2:v]scale={ICON_DIAM}:{ICON_DIAM}[ic];"
    f"[bg][ic]overlay=x={ICON_X}:y={ICON_Y}[b1];"
    f"[b1][3:v]overlay=x={BRAND_X}:y={BRAND_Y}[b2];"
    f"[b2][intro]overlay=x=0:y=0:enable='lte(t,5)',format=yuv420p[outv]"
)

print("=" * 58)
print("  Latte BGM — Cafe Warm 30min 動画生成 (005 / 新ロゴv2版)")
print("=" * 58)
print(f"  画像  : {IMAGE}")
print(f"  音源  : {AUDIO}")
print(f"  アイコン: {ICON}")
print(f"  文字  : {BRAND}")
print(f"  出力  : {OUTPUT}")
print(f"  長さ  : {D//60}分")
print()

# 素材存在チェック
for p in (IMAGE, AUDIO, ICON, BRAND, INTRO):
    if not os.path.exists(p):
        print(f"[ERROR] 素材が見つかりません: {p}")
        sys.exit(1)

with tempfile.TemporaryDirectory() as tmpdir:
    looped = os.path.join(tmpdir, "loop.aac")

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

    print("[2/2] 動画生成中 (slow encode, 約10〜20分)...")
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", IMAGE,    # [0] 背景
        "-loop", "1", "-i", INTRO,    # [1] 中央イントロ（フェード用に要ループ）
        "-i", ICON,                   # [2] 犬アイコン（静止・eof repeat）
        "-i", BRAND,                  # [3] LATTE BGM 文字（静止・eof repeat）
        "-i", looped,                 # [4] 音声
        "-filter_complex", filter_complex,
        "-map", "[outv]", "-map", "4:a",
        "-c:v", "libx264", "-preset", "slow", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k", "-ar", "44100",
        "-r", "30", "-t", str(D),
        "-movflags", "+faststart",
        "-metadata", "title=Latte BGM | 30 Min Warm Cafe Music | Relaxing Coffee Shop BGM",
        OUTPUT,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)

if result.returncode != 0:
    print(f"[ERROR] ffmpeg 失敗:\n{result.stderr[-1000:]}")
    sys.exit(1)

size_mb = os.path.getsize(OUTPUT) / (1024 * 1024)
print(f"\n[DONE] 生成完了!")
print(f"  出力  : {OUTPUT}")
print(f"  サイズ: {size_mb:.1f} MB")
