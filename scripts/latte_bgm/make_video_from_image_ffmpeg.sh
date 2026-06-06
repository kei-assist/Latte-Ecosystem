#!/bin/bash
# ============================================================
# Latte BGM - make_video_from_image_ffmpeg.sh  v2.0
# 画像 + 音源 → 1時間BGM動画  (純 FFmpeg 版)
# ============================================================
# Usage:
#   ./make_video_from_image_ffmpeg.sh \
#       <image> <audio> <preset> [duration_sec] [output_path]
#
# Workout例:
#   ./make_video_from_image_ffmpeg.sh \
#       ../../assets/latte_bgm/images/source/workout/workout_boxercise_female_001.png \
#       ../../assets/latte_bgm/audio/source/workout_boxercise_001.mp3 \
#       workout_boxercise
#
# Sleep例:
#   ./make_video_from_image_ffmpeg.sh \
#       ../../assets/latte_bgm/images/source/sleep/sleep_rainy_night_001.png \
#       ../../assets/latte_bgm/audio/source/sleep_rainy_night_001.mp3 \
#       sleep_rainy_night
#
# preset一覧:
#   Workout: workout_beast_mode / workout_boxercise / workout_running
#            workout_hiit_circuit / workout_gym_motivation
#   Sleep  : sleep_soft / sleep_rainy_night / sleep_deep_night
#   その他 : study / nature / cafe / relax
# ============================================================

set -e

IMAGE="$1"
AUDIO="$2"
PRESET="${3:-study}"
DURATION="${4:-3600}"
OUTPUT="$5"

# ── 引数チェック ─────────────────────────────────────────────────
if [ -z "$IMAGE" ] || [ -z "$AUDIO" ]; then
    echo "Usage: $0 <image> <audio> [preset] [duration_sec] [output]"
    echo ""
    echo "preset一覧:"
    echo "  Workout: workout_beast_mode, workout_boxercise, workout_running"
    echo "           workout_hiit_circuit, workout_gym_motivation"
    echo "  Sleep  : sleep_soft, sleep_rainy_night, sleep_deep_night"
    echo "  その他 : study, nature, cafe, relax"
    exit 1
fi

if [ ! -f "$IMAGE" ]; then
    echo "[ERROR] 画像ファイルが見つかりません: $IMAGE"
    echo "  → assets/latte_bgm/images/source/[カテゴリ]/ に画像を置いてください"
    exit 1
fi

if [ ! -f "$AUDIO" ]; then
    echo "[ERROR] 音源ファイルが見つかりません: $AUDIO"
    echo "  → assets/latte_bgm/audio/source/ に音源を置いてください"
    exit 1
fi

# ── 出力パス自動生成 ──────────────────────────────────────────────
if [ -z "$OUTPUT" ]; then
    BASENAME=$(basename "$IMAGE" | sed 's/\.[^.]*$//')
    OUTPUT="../../assets/latte_bgm/videos/drafts/${BASENAME}_${DURATION}sec.mp4"
fi
mkdir -p "$(dirname "$OUTPUT")"

echo "=============================="
echo " Latte BGM 動画生成 (FFmpeg)"
echo "=============================="
echo "  Preset  : $PRESET"
echo "  画像    : $IMAGE"
echo "  音源    : $AUDIO"
echo "  長さ    : $((DURATION / 60))分"
echo "  出力    : $OUTPUT"
echo ""

# ── preset 別パラメータ ──────────────────────────────────────────
case "$PRESET" in
    workout_beast_mode)
        Z_END=1.28; PAN=0.28; BRIGHT=0.03; CONT=1.18; SAT=1.20; BLUR=0; RAIN=0 ;;
    workout_boxercise)
        Z_END=1.22; PAN=0.50; BRIGHT=0.05; CONT=1.12; SAT=1.15; BLUR=0; RAIN=0 ;;
    workout_running)
        Z_END=1.18; PAN=0.80; BRIGHT=0.08; CONT=1.06; SAT=1.10; BLUR=0; RAIN=0 ;;
    workout_hiit_circuit)
        Z_END=1.20; PAN=0.40; BRIGHT=0.04; CONT=1.08; SAT=1.12; BLUR=0; RAIN=0 ;;
    workout_gym_motivation|workout)
        Z_END=1.12; PAN=0.15; BRIGHT=-0.02; CONT=1.05; SAT=1.05; BLUR=0; RAIN=0 ;;
    sleep_soft|sleep)
        Z_END=1.06; PAN=0.025; BRIGHT=-0.18; CONT=0.95; SAT=0.80; BLUR=0.6; RAIN=0 ;;
    sleep_rainy_night)
        Z_END=1.08; PAN=0.04; BRIGHT=-0.22; CONT=0.90; SAT=0.72; BLUR=0.9; RAIN=1 ;;
    sleep_deep_night)
        Z_END=1.04; PAN=0.01; BRIGHT=-0.30; CONT=0.88; SAT=0.68; BLUR=1.2; RAIN=0 ;;
    study)
        Z_END=1.12; PAN=0.10; BRIGHT=-0.05; CONT=1.00; SAT=0.95; BLUR=0; RAIN=0 ;;
    nature)
        Z_END=1.15; PAN=0.20; BRIGHT=-0.02; CONT=1.00; SAT=1.05; BLUR=0; RAIN=0 ;;
    cafe)
        Z_END=1.10; PAN=0.15; BRIGHT=0.02;  CONT=1.00; SAT=1.08; BLUR=0; RAIN=0 ;;
    relax)
        Z_END=1.10; PAN=0.10; BRIGHT=0.00;  CONT=1.00; SAT=1.00; BLUR=0; RAIN=0 ;;
    *)
        echo "[WARN] 不明なpreset: $PRESET → study 設定を使用"
        Z_END=1.12; PAN=0.10; BRIGHT=-0.05; CONT=1.00; SAT=0.95; BLUR=0; RAIN=0 ;;
esac

# ── プリスケールサイズ計算 ────────────────────────────────────────
W=1920; H=1080
SW=$(python3 -c "v=int(${W}*${Z_END}); print(v+v%2)")
SH=$(python3 -c "v=int(${H}*${Z_END}); print(v+v%2)")

# 安全なpan (利用可能スペースの50%以内)
SAFE_PAN=$(python3 -c "
avail=(${SW}-${W})/2.0
mx=avail*0.50/${DURATION}
print(min(${PAN}, mx))
")

# ── フィルタ組み立て ─────────────────────────────────────────────
Z_RNG=$(python3 -c "print(round(${Z_END}-1.0, 4))")
CROP_W_E="${W}*(${Z_END}-${Z_RNG}*min(t,${DURATION})/${DURATION})"
CROP_H_E="${H}*(${Z_END}-${Z_RNG}*min(t,${DURATION})/${DURATION})"
CROP_X_E="max(0,min(${SW}-(${CROP_W_E}),(${SW}-(${CROP_W_E}))/2+${SAFE_PAN}*t))"
CROP_Y_E="(${SH}-(${CROP_H_E}))/2"

EQ_FILTER="eq=brightness=${BRIGHT}:contrast=${CONT}:saturation=${SAT}"
VIGNETTE="vignette=angle=PI/4:mode=backward"

VF="scale=${SW}:${SH},crop=w='${CROP_W_E}':h='${CROP_H_E}':x='${CROP_X_E}':y='${CROP_Y_E}',scale=${W}:${H},${EQ_FILTER}"

if [ "$BLUR" != "0" ]; then
    VF="${VF},gblur=sigma=${BLUR}"
fi

if [ "$RAIN" = "1" ]; then
    RAIN_F="geq=r='if(lt(mod(X*0.30+Y+T*480+floor(X/14)*53,58),1.4),min(r+14,255),r)':g='if(lt(mod(X*0.30+Y+T*480+floor(X/14)*53,58),1.4),min(g+11,255),g)':b='if(lt(mod(X*0.30+Y+T*480+floor(X/14)*53,58),1.4),min(b+26,255),b)'"
    VF="${VF},${RAIN_F}"
    echo "[INFO] 雨筋エフェクト有効 (geq filter)"
fi
VF="${VF},${VIGNETTE},format=yuv420p"

# ── 音源ループ ──────────────────────────────────────────────────
TMPDIR_PATH=$(mktemp -d)
trap "rm -rf $TMPDIR_PATH" EXIT

AUDIO_DUR=$(ffprobe -v error -show_entries format=duration \
    -of default=noprint_wrappers=1:nokey=1 "$AUDIO" 2>/dev/null || echo "0")
LOOPED="$TMPDIR_PATH/looped.aac"

if awk "BEGIN{exit !($AUDIO_DUR >= $DURATION)}"; then
    echo "[INFO] 音源: ${AUDIO_DUR%.*}秒 → ループ不要"
    LOOPED="$AUDIO"
else
    echo "[INFO] 音源: ${AUDIO_DUR%.*}秒 → ${DURATION}秒にループ中..."
    ffmpeg -y -stream_loop -1 -i "$AUDIO" -t "$DURATION" \
        -c:a aac -b:a 192k -ar 44100 "$LOOPED" -loglevel error
fi

# ── 動画生成 ────────────────────────────────────────────────────
echo ""
echo "[FFmpeg] 動画生成開始 (${DURATION}秒 / $((DURATION/60))分)..."
echo "  完了まで数分〜20分程度かかります"
echo ""

ffmpeg -y \
    -loop 1 -i "$IMAGE" \
    -i "$LOOPED" \
    -vf "$VF" \
    -c:v libx264 -preset slow -crf 20 \
    -c:a aac -b:a 192k -ar 44100 \
    -r 30 -t "$DURATION" \
    -movflags +faststart \
    "$OUTPUT"

echo ""
echo "=============================="
echo " [DONE] 完了!"
echo "  出力: $OUTPUT"
echo "  サイズ: $(du -sh "$OUTPUT" 2>/dev/null | cut -f1)"
echo "=============================="
