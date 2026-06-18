#!/usr/bin/env python3
"""
Latte BGM - Deep Focus / Night Study & Work  30分音源ビルド
新規Suno音源3曲を -14 LUFS に揃え、10秒クロスフェードで4サイクル連結し、
30:00にトリム、冒頭フェードイン/終盤フェードアウトして書き出す。

再生順（雰囲気アーク: 静か→起伏→平坦着地）:
  ① 02_lamp_by_the_window  (最も静か / 導入)
  ② 03_quiet_night_desk    (最も起伏 / 中盤)
  ③ 01_desk_lamp_window    (最も平坦 / 着地→ループ復帰)
"""
import json, os, subprocess, sys, tempfile

ROOT = "/Users/khhr/Desktop/latte-ecosystem/assets/latte_bgm/audio"
SRC = os.path.join(ROOT, "source")
OUT = os.path.join(ROOT, "deep_focus_night_30min.mp3")
WORK = tempfile.mkdtemp(prefix="dfn_")

PLAY_ORDER = [
    "02_lamp_by_the_window.mp3",
    "03_quiet_night_desk.mp3",
    "01_desk_lamp_window.mp3",
]
TARGET_LUFS = -14.0
XFADE = 10            # 曲間クロスフェード(秒)
CYCLES = 4           # シーケンス繰り返し回数
TOTAL = 1800.0       # 目標尺(秒) 30:00
FADE_IN = 3.0
FADE_OUT = 8.0

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def normalize(src, dst):
    """単一パス loudnorm で -14 LUFS / 48k / stereo の wav を作る"""
    cmd = ["ffmpeg", "-y", "-hide_banner", "-i", src,
           "-af", f"loudnorm=I={TARGET_LUFS}:TP=-1.5:LRA=11",
           "-ar", "48000", "-ac", "2", dst]
    r = run(cmd)
    if r.returncode != 0:
        print(r.stderr[-1500:]); sys.exit("normalize failed: " + src)

def main():
    # 1) 正規化
    norm = []
    for f in PLAY_ORDER:
        d = os.path.join(WORK, "n_" + os.path.splitext(f)[0] + ".wav")
        normalize(os.path.join(SRC, f), d)
        norm.append(d)
        print("normalized:", os.path.basename(d))

    # 2) 12セグメント(4サイクル)を acrossfade で連結
    seq = norm * CYCLES                      # [①②③]×4 = 12本
    inputs = []
    for p in seq:
        inputs += ["-i", p]
    # filter_complex 構築
    parts = []
    prev = "[0]"
    for i in range(1, len(seq)):
        out = f"[a{i}]"
        parts.append(f"{prev}[{i}]acrossfade=d={XFADE}:c1=tri:c2=tri{out}")
        prev = out
    # 3) トリム + フェードイン/アウト
    fade_out_start = TOTAL - FADE_OUT
    parts.append(
        f"{prev}atrim=0:{TOTAL},"
        f"afade=t=in:st=0:d={FADE_IN},"
        f"afade=t=out:st={fade_out_start}:d={FADE_OUT}[out]"
    )
    fc = ";".join(parts)

    cmd = ["ffmpeg", "-y", "-hide_banner"] + inputs + [
        "-filter_complex", fc, "-map", "[out]",
        "-c:a", "libmp3lame", "-b:a", "320k", "-ar", "48000", OUT]
    r = run(cmd)
    if r.returncode != 0:
        print(r.stderr[-2500:]); sys.exit("concat failed")
    print("WROTE:", OUT)

if __name__ == "__main__":
    main()
