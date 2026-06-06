#!/bin/bash
# ============================================================
# Latte BGM - make_video_from_image_ffmpeg.sh
# 純FFmpegで 画像 + 音源 → 1時間BGM動画
# ============================================================
# Usage:
#   ./make_video_from_image_ffmpeg.sh <image> <audio> <category> [duration_sec] [output]
#
# Examples:
#   ./make_video_from_image_ffmpeg.sh \
#       ../../assets/latte_bgm/images/source/workout/workout_boxercise_female_001.png \
#       ../../assets/latte_bgm/audio/source/boxercise_beat.mp3 \
#       workout
#
#   # カスタム出力先・長さ指定
#   ./make_video_from_image_ffmpeg.sh image.png audio.mp3 study 3600 output.mp4

set -e

IMAGE="$1"
AUDIO="$2"
CATEGORY="${3:-study}"
DURATION="${4:-3600}"
OUTPUT="$5"

# ── 引数チェック ──
if [ -z "$IMAGE" ] || [ -z "$AUDIO" ]; then
  echo "Usage: $0 <image> <audio> [category] [duration_sec] [output]"
  echo "Categories: workout study sleep nature cafe relax"
  exit 1
fi

if [ ! -f "$IMAGE" ]; then
  echo "[ERROR] 画像ファイルが見つかりません: $IMAGE"
  exit 1
fi

if [ ! -f "$AUDIO" ]; then
  echo "[ERROR] 音源ファイルが見つかりません: $AUDIO"
  exit 1
fi

# ── 出力パス自動生成 ──
if [ -z "$OUTPUT" ]; then
  BASENAME=$(basename "$IMAGE" | sed 's/\.[^.]*$//')
  OUTPUT="../../assets/latte_bgm/videos/drafts/${BASENAME}_${DURATION}sec.mp4"
fi

mkdir -p "$(dirname "$OUTPUT")"

echo "=============================="
echo " Latte BGM 動画生成 (FFmpeg)"
echo "=============================="
echo "  カテゴリ : $CATEGORY"
echo "  画像     : $IMAGE"
echo "  音源     : $AUDIO"
echo "  長さ     : $((DURATION / 60))分"
echo "  出力     : $OUTPUT"
echo ""

# ── カテゴリ別エフェクト設定 ──
case "$CATEGORY" in
  workout)
    ZOOM_END=1.25
    ZOOM_RATE=0.00000694   # (1.25-1.00)/(3600*30*0.33)
    PAN_X=0.03
    BRIGHTNESS=0.08
    SATURATION=1.15
    VIGNETTE_ENABLED=1
    ;;
  study)
    ZOOM_END=1.12
    ZOOM_RATE=0.00000370
    PAN_X=0.01
    BRIGHTNESS=-0.05
    SATURATION=0.95
    VIGNETTE_ENABLED=1
    ;;
  sleep)
    ZOOM_END=1.08
    ZOOM_RATE=0.00000247
    PAN_X=0.005
    BRIGHTNESS=-0.25
    SATURATION=0.80
    VIGNETTE_ENABLED=1
    ;;
  nature)
    ZOOM_END=1.15
    ZOOM_RATE=0.00000463
    PAN_X=0.02
    BRIGHTNESS=-0.02
    SATURATION=1.05
    VIGNETTE_ENABLED=1
    ;;
  cafe)
    ZOOM_END=1.10
    ZOOM_RATE=0.00000309
    PAN_X=0.015
    BRIGHTNESS=0.02
    SATURATION=1.08
    VIGNETTE_ENABLED=1
    ;;
  relax)
    ZOOM_END=1.10
    ZOOM_RATE=0.00000309
    PAN_X=0.01
    BRIGHTNESS=0.00
    SATURATION=1.00
    VIGNETTE_ENABLED=1
    ;;
  *)
    echo "[WARN] 未知のカテゴリ: $CATEGORY → study設定を使用"
    ZOOM_END=1.12
    ZOOM_RATE=0.00000370
    PAN_X=0.01
    BRIGHTNESS=-0.05
    SATURATION=0.95
    VIGNETTE_ENABLED=1
    ;;
esac

# ── ビデオフィルタ組み立て ──
ZOOMPAN="zoompan=z='min(zoom+${ZOOM_RATE},${ZOOM_END})':x='iw/2-(iw/zoom/2)+${PAN_X}*iw/zoom':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=30"
EQ="eq=brightness=${BRIGHTNESS}:saturation=${SATURATION}"

if [ "$VIGNETTE_ENABLED" -eq 1 ]; then
  VF="${ZOOMPAN},${EQ},vignette=angle=PI/4:mode=backward,format=yuv420p"
else
  VF="${ZOOMPAN},${EQ},format=yuv420p"
fi

# ── 音源ループ ──
TMPDIR_PATH=$(mktemp -d)
trap "rm -rf $TMPDIR_PATH" EXIT

AUDIO_DURATION=$(ffprobe -v error -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 "$AUDIO" 2>/dev/null || echo "0")

echo "[INFO] 音源長さ: ${AUDIO_DURATION%.*}秒"

LOOPED_AUDIO="$TMPDIR_PATH/looped.aac"
if awk "BEGIN{exit !($AUDIO_DURATION >= $DURATION)}"; then
  echo "[INFO] 音源が十分な長さ → そのまま使用"
  LOOPED_AUDIO="$AUDIO"
else
  echo "[INFO] 音源をループして${DURATION}秒に延長..."
  ffmpeg -y -stream_loop -1 -i "$AUDIO" -t "$DURATION" \
    -c:a aac -b:a 192k -ar 44100 \
    "$LOOPED_AUDIO" -loglevel error
  echo "[INFO] ループ音源作成完了"
fi

# ── メイン動画生成 ──
echo ""
echo "[FFmpeg] 動画生成開始... (${DURATION}秒 / $(( DURATION / 60 ))分)"
echo "  完了まで数分〜数十分かかる場合があります"
echo ""

ffmpeg -y \
  -loop 1 \
  -i "$IMAGE" \
  -i "$LOOPED_AUDIO" \
  -vf "$VF" \
  -c:v libx264 \
  -preset slow \
  -crf 20 \
  -c:a aac \
  -b:a 192k \
  -ar 44100 \
  -t "$DURATION" \
  -movflags +faststart \
  "$OUTPUT"

echo ""
echo "=============================="
echo " [DONE] 生成完了!"
echo "  出力: $OUTPUT"
SIZE=$(du -sh "$OUTPUT" 2>/dev/null | cut -f1)
echo "  サイズ: $SIZE"
echo "=============================="
