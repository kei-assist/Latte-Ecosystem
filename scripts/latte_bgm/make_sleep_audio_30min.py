#!/usr/bin/env python3
"""
Sleep / Rainy Night / Calm Sleep 30分 音声マスター生成

過去音源3曲（睡眠向きのみ）を再利用し、クロスフェード連結→4周→30分トリム。
- 各曲を -16 LUFS に正規化（Cafe/Natureより2dB静か＝睡眠向け）
- つなぎ目 6秒クロスフェード（睡眠向けに長め・三角カーブ）
- 冒頭 5秒フェードイン / 末尾 10秒フェードアウト
- 出力: 44100Hz / stereo / 1800秒ちょうど
"""
import subprocess, os, tempfile

ROOT = "/Users/khhr/Desktop/latte-ecosystem/assets/latte_bgm"
SRC  = f"{ROOT}/audio/source"
OUT  = f"{ROOT}/audio/built/sleep_rainy_night_30min_master.m4a"

CYCLE = [
    "sleep_rainy_night_001.mp3",
    "nature_forest_rain_001.mp3",
    "study_deep_focus_001.mp3",
]
CYCLES   = 4
XFADE    = 6.0
TARGET   = 1800
FADE_IN  = 5.0
FADE_OUT = 10.0
LUFS     = -16.0

os.makedirs(os.path.dirname(OUT), exist_ok=True)

def dur(path):
    return float(subprocess.run(
        ["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",path],
        capture_output=True, text=True).stdout.strip())

with tempfile.TemporaryDirectory() as tmp:
    norm = {}
    for name in CYCLE:
        out = os.path.join(tmp, name.replace(".mp3", ".wav"))
        print(f"[norm] {name} -> {LUFS} LUFS")
        r = subprocess.run(
            ["ffmpeg","-y","-i",f"{SRC}/{name}",
             "-af", f"loudnorm=I={LUFS}:TP=-2.0:LRA=9,aresample=44100",
             "-ac","2", out], capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stderr[-500:]); raise SystemExit(1)
        norm[name] = out

    seq = [norm[n] for n in CYCLE] * CYCLES        # 12 本
    inputs = []
    for f in seq:
        inputs += ["-i", f]

    parts = [f"[{i}:a]aformat=sample_rates=44100:channel_layouts=stereo[a{i}]"
             for i in range(len(seq))]
    fc = ";".join(parts) + ";"
    cur = "a0"
    for i in range(1, len(seq)):
        nxt = f"x{i}"
        fc += f"[{cur}][a{i}]acrossfade=d={XFADE}:c1=tri:c2=tri[{nxt}];"
        cur = nxt
    fc += (f"[{cur}]atrim=0:{TARGET},"
           f"afade=t=in:st=0:d={FADE_IN},"
           f"afade=t=out:st={TARGET-FADE_OUT}:d={FADE_OUT}[out]")

    print(f"[build] {len(seq)}セグメントを連結中...")
    r = subprocess.run(
        ["ffmpeg","-y", *inputs, "-filter_complex", fc, "-map","[out]",
         "-c:a","aac","-b:a","192k","-ar","44100", OUT],
        capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-800:]); raise SystemExit(1)

print(f"\n[DONE] {OUT}")
print(f"  長さ: {dur(OUT):.1f}s  サイズ: {os.path.getsize(OUT)/1024/1024:.1f}MB")
