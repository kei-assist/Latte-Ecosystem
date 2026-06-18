#!/usr/bin/env python3
"""
Latte BGM — Deep Focus / Night Study & Work  30分動画生成

方針（犬キャラなし・大人向け・集中向け・上品）:
  - 背景: 夜の書斎イラスト（deep_focus_night_001.png / 犬要素なし）
  - 右上ロゴ: 正式統一アイコン（丸い犬＋青ヘッドホン）＋「LATTE BGM」文字
    （過去動画 Cafe 004/005 と同じ配置・サイズ。背景に犬は出さないが
     右上ブランドロゴは必ず統一アイコンを使うのが正式ルール）
  - 中央イントロ(5s): LATTE BGM / Music for Every Moment
  - 動き最小: 極ゆるKen Burns(1.00→1.08) + 微パララックス + 控えめライト揺らぎ + ビネット
  - 音源は既に 30:00 のためループ不要
  - 出力: 1920x1080 / H.264 / AAC / 30:00

ffmpeg は drawtext 非対応のため、テキストは PIL 生成済み透過PNG を overlay。
"""
import subprocess, os, sys

ROOT   = "/Users/khhr/Desktop/latte-ecosystem"
IMAGE  = f"{ROOT}/assets/latte_bgm/images/organized/09_DeepFocus_Night/deep_focus_night_001.png"
AUDIO  = f"{ROOT}/assets/latte_bgm/audio/deep_focus_night_30min.mp3"
ICON   = f"{ROOT}/assets/latte_bgm/images/brand/latte_dog_icon_circle_v2.png"  # 統一アイコン
BRAND  = f"{ROOT}/assets/latte_bgm/images/brand/latte_brand_text.png"      # 250x80
INTRO  = f"{ROOT}/assets/latte_bgm/images/brand/latte_intro_overlay.png"   # 1920x1080（犬なし）
OUTPUT = f"{ROOT}/assets/latte_bgm/videos/final/deep_focus_night_30min_002.mp4"  # 002=統一アイコン版

D    = 1800            # 30:00
W, H = 1920, 1080
os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

# ── Ken Burns（極ゆるズーム 1.00→1.08・動き最小） ──────────
z_start, z_end = 1.00, 1.08
z_rng = z_end - z_start
sw = int(W * z_end); sw += sw % 2
sh = int(H * z_end); sh += sh % 2
pan      = 0.08
avail_x  = (sw - W) / 2.0
max_pan  = avail_x * 0.50
safe_pan = min(pan, max_pan / D)
crop_w = f"{W}*({z_end:.4f}-{z_rng:.4f}*min(t\\,{D})/{D})"
crop_h = f"{H}*({z_end:.4f}-{z_rng:.4f}*min(t\\,{D})/{D})"
pan_e  = f"+{safe_pan:.5f}*t"
crop_x = f"max(0\\,min({sw}-({crop_w})\\,({sw}-({crop_w}))/2{pan_e}))"
crop_y = f"({sh}-({crop_h}))/2"
crop_f = f"crop=w='{crop_w}':h='{crop_h}':x='{crop_x}':y='{crop_y}'"

# ── 控えめなライト揺らぎ（集中を妨げない・navy基調を保つ）──
brightness, contrast, saturation = 0.02, 1.02, 1.05
flicker_speed, flicker_amp = 0.5, 0.025
spd2 = round(flicker_speed * 1.7321, 4)
bright_expr = f"{brightness:.4f}+{flicker_amp:.4f}*sin(t*{flicker_speed:.3f})*sin(t*{spd2})"
eq_f = (f"eq=brightness='{bright_expr}'"
        f":contrast={contrast:.2f}:saturation={saturation:.2f}:eval=frame")
vignette = "vignette=angle=PI/4:mode=backward"

# ── 右上ロゴ（統一アイコン＋文字・過去動画 Cafe 004/005 と同配置） ─
ICON_DIAM = 160
ICON_CX   = 1785                          # アイコン中心X（右寄せ）
ICON_X    = ICON_CX - ICON_DIAM // 2      # 1705
ICON_Y    = 22
BRAND_W   = 250                           # latte_brand_text.png の幅
BRAND_X   = ICON_CX - BRAND_W // 2        # 1660（アイコン中心に揃える）
BRAND_Y   = ICON_Y + ICON_DIAM + 2        # アイコン直下 184

# ── 中央イントロ フェード（0→1s in / 4→5s out） ───────────
intro_fade = "format=rgba,fade=t=in:st=0:d=1:alpha=1,fade=t=out:st=4:d=1:alpha=1"

bg_chain = f"scale={sw}:{sh},{crop_f},scale={W}:{H},{eq_f},{vignette}"
filter_complex = (
    f"[0:v]{bg_chain}[bg];"
    f"[1:v]{intro_fade}[intro];"
    f"[2:v]scale={ICON_DIAM}:{ICON_DIAM}[ic];"
    f"[3:v]scale={BRAND_W}:-1[brand];"
    f"[bg][ic]overlay=x={ICON_X}:y={ICON_Y}[b1];"
    f"[b1][brand]overlay=x={BRAND_X}:y={BRAND_Y}[b2];"
    f"[b2][intro]overlay=x=0:y=0:enable='lte(t,5)',format=yuv420p[outv]"
)

print("=" * 60)
print("  Latte BGM — Deep Focus / Night Study & Work 30min（犬なし）")
print("=" * 60)
for p in (IMAGE, AUDIO, ICON, BRAND, INTRO):
    if not os.path.exists(p):
        sys.exit(f"[ERROR] 素材なし: {p}")

print("[1/1] 動画生成中 (slow encode, 約15〜20分)...")
cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-i", IMAGE,   # [0] 背景
    "-loop", "1", "-i", INTRO,   # [1] 中央イントロ
    "-i", ICON,                  # [2] 統一アイコン（犬＋青ヘッドホン）
    "-i", BRAND,                 # [3] LATTE BGM 文字
    "-i", AUDIO,                 # [4] 音声（既に30:00）
    "-filter_complex", filter_complex,
    "-map", "[outv]", "-map", "4:a",
    "-c:v", "libx264", "-preset", "slow", "-crf", "20",
    "-c:a", "aac", "-b:a", "192k", "-ar", "44100",
    "-r", "30", "-t", str(D),
    "-movflags", "+faststart",
    "-metadata", "title=30 Min Deep Focus BGM | Night Study & Work Music | LATTE BGM",
    OUTPUT,
]
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode != 0:
    print(r.stderr[-1500:]); sys.exit("[ERROR] ffmpeg 失敗")
size_mb = os.path.getsize(OUTPUT) / (1024 * 1024)
print(f"\n[DONE] {OUTPUT}\n  サイズ: {size_mb:.1f} MB")
