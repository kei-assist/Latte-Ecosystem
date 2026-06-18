#!/usr/bin/env python3
"""
Nature / Forest / Rain / Relaxation 30分 音声マスター生成

過去音源4曲を再利用し、クロスフェードで自然に連結→3周ループ→30分でトリム。
- 各曲を -14 LUFS に正規化（音量差をなくす）
- つなぎ目は 4秒クロスフェード（acrossfade, 三角カーブ）
- 冒頭 3秒フェードイン / 末尾 6秒フェードアウト
- 出力: 44100Hz / stereo / 1800秒ちょうど
"""
import subprocess, os, tempfile

ROOT = "/Users/khhr/Desktop/latte-ecosystem/assets/latte_bgm"
SRC  = f"{ROOT}/audio/source"
OUT  = f"{ROOT}/audio/built/forest_relaxation_30min_master.m4a"

# 1周の曲順（穏やかなアーク: 森雨→ピアノ→集中→雨夜）
CYCLE = [
    "nature_forest_rain_001.mp3",
    "running_morning_piano_001.mp3",
    "study_deep_focus_001.mp3",
    "sleep_rainy_night_001.mp3",
]
CYCLES   = 3            # 3周（約33分）→ 30分でトリム
XFADE    = 4.0          # クロスフェード秒
TARGET   = 1800         # 30分
FADE_IN  = 3.0
FADE_OUT = 6.0
LUFS     = -14.0

os.makedirs(os.path.dirname(OUT), exist_ok=True)

def dur(path):
    return float(subprocess.run(
        ["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",path],
        capture_output=True, text=True).stdout.strip())

with tempfile.TemporaryDirectory() as tmp:
    # ── 1) 各曲を -14 LUFS に正規化して temp WAV 化 ──────────
    norm = {}
    for name in CYCLE:
        src = f"{SRC}/{name}"
        out = os.path.join(tmp, name.replace(".mp3", ".wav"))
        print(f"[norm] {name}")
        r = subprocess.run(
            ["ffmpeg","-y","-i",src,
             "-af", f"loudnorm=I={LUFS}:TP=-1.5:LRA=11,aresample=44100",
             "-ac","2", out], capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stderr[-500:]); raise SystemExit(1)
        norm[name] = out

    # ── 2) 12セグメント（4曲×3周）の acrossfade チェーン構築 ──
    seq = [norm[n] for n in CYCLE] * CYCLES        # 12 本
    inputs = []
    for f in seq:
        inputs += ["-i", f]

    # 各入力を共通フォーマットに、acrossfade を順次チェーン
    parts = []
    for i in range(len(seq)):
        parts.append(f"[{i}:a]aformat=sample_rates=44100:channel_layouts=stereo[a{i}]")
    chain = "[a0]"
    label_prev = "a0"
    fc = ";".join(parts) + ";"
    cur = "a0"
    step = 0
    for i in range(1, len(seq)):
        nxt = f"x{step}"
        fc += f"[{cur}][a{i}]acrossfade=d={XFADE}:c1=tri:c2=tri[{nxt}];"
        cur = nxt
        step += 1
    # トリム + フェード
    fade_out_st = TARGET - FADE_OUT
    fc += (f"[{cur}]atrim=0:{TARGET},"
           f"afade=t=in:st=0:d={FADE_IN},"
           f"afade=t=out:st={fade_out_st}:d={FADE_OUT}[out]")

    print(f"[build] {len(seq)}セグメントを連結中...")
    cmd = ["ffmpeg","-y", *inputs,
           "-filter_complex", fc, "-map","[out]",
           "-c:a","aac","-b:a","192k","-ar","44100", OUT]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-800:]); raise SystemExit(1)

print(f"\n[DONE] {OUT}")
print(f"  長さ: {dur(OUT):.1f}s  サイズ: {os.path.getsize(OUT)/1024/1024:.1f}MB")
