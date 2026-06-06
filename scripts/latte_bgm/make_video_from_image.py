#!/usr/bin/env python3
"""
Latte BGM - make_video_from_image.py
=====================================
静止画 + 音源 → YouTube用1時間BGM動画（1920x1080 MP4）

Usage:
    python3 make_video_from_image.py <image_path> <audio_path> [options]

Examples:
    python3 make_video_from_image.py \
        ../../assets/latte_bgm/images/source/workout/workout_boxercise_female_001.png \
        ../../assets/latte_bgm/audio/source/boxercise_beat.mp3 \
        --category workout \
        --duration 3600 \
        --output ../../assets/latte_bgm/videos/drafts/workout_boxercise_60min_001.mp4

    # タイトル付き
    python3 make_video_from_image.py image.png audio.mp3 --category study --title "Deep Focus Vol.5"
"""

import argparse
import subprocess
import sys
import os
import tempfile
from pathlib import Path

# ─────────────────────────────────────────────
# カテゴリ別エフェクト設定
# ─────────────────────────────────────────────
CATEGORY_EFFECTS = {
    "workout": {
        "zoom_start": 1.00,
        "zoom_end":   1.25,          # 強めのズーム
        "pan_x":      0.03,          # わずかな横移動
        "brightness": 1.05,          # 明るめ
        "saturation": 1.15,          # 彩度高め
        "vignette":   0.3,           # 周辺減光（弱め）
        "description": "強めのスローズーム + ジム照明感"
    },
    "study": {
        "zoom_start": 1.00,
        "zoom_end":   1.12,          # ゆっくり穏やかなズーム
        "pan_x":      0.01,
        "brightness": 0.95,          # 少し落ち着いた明度
        "saturation": 0.95,
        "vignette":   0.5,           # 周辺減光（強め・集中感）
        "description": "ゆっくりズーム + ランプの揺らぎ感"
    },
    "sleep": {
        "zoom_start": 1.00,
        "zoom_end":   1.08,          # 最もゆっくりなズーム
        "pan_x":      0.005,
        "brightness": 0.75,          # 暗め
        "saturation": 0.80,          # 彩度落とす
        "vignette":   0.7,           # 強い周辺減光
        "description": "超スローズーム + 暗め + 低刺激"
    },
    "nature": {
        "zoom_start": 1.00,
        "zoom_end":   1.15,
        "pan_x":      0.02,
        "brightness": 0.98,
        "saturation": 1.05,          # 自然の緑を少し強調
        "vignette":   0.4,
        "description": "霧・雨・川の流れ感 + ゆっくりズーム"
    },
    "cafe": {
        "zoom_start": 1.00,
        "zoom_end":   1.10,
        "pan_x":      0.015,
        "brightness": 1.02,          # 暖色系
        "saturation": 1.08,
        "vignette":   0.45,
        "description": "暖色の光 + ゆっくりズーム + 落ち着いた動き"
    },
    "relax": {
        "zoom_start": 1.00,
        "zoom_end":   1.10,
        "pan_x":      0.01,
        "brightness": 1.00,
        "saturation": 1.00,
        "vignette":   0.4,
        "description": "夕方の光 + ゆっくりズーム + リラックス感"
    },
}

DEFAULT_EFFECT = CATEGORY_EFFECTS["study"]


def get_audio_duration(audio_path: str) -> float:
    """音源の長さを取得（秒）"""
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", audio_path],
        capture_output=True, text=True
    )
    try:
        return float(result.stdout.strip())
    except ValueError:
        return 0.0


def loop_audio(audio_path: str, target_duration: float, output_path: str) -> str:
    """音源を指定秒数にループして一時ファイルに書き出す"""
    audio_duration = get_audio_duration(audio_path)
    if audio_duration <= 0:
        print(f"[ERROR] 音源の長さを取得できませんでした: {audio_path}")
        sys.exit(1)

    if audio_duration >= target_duration:
        print(f"[INFO] 音源({audio_duration:.0f}秒) >= 目標({target_duration:.0f}秒) → そのまま使用")
        return audio_path

    print(f"[INFO] 音源({audio_duration:.0f}秒)を{target_duration:.0f}秒にループします")

    cmd = [
        "ffmpeg", "-y",
        "-stream_loop", "-1",
        "-i", audio_path,
        "-t", str(target_duration),
        "-c", "copy",
        output_path
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"[INFO] ループ音源作成完了: {output_path}")
    return output_path


def build_ffmpeg_filter(effect: dict, duration: float, width=1920, height=1080) -> str:
    """カテゴリ別のffmpeg filtergraphを生成"""
    zoom_start = effect["zoom_start"]
    zoom_end   = effect["zoom_end"]
    pan_x      = effect["pan_x"]
    brightness = effect["brightness"]
    saturation = effect["saturation"]
    vignette   = effect["vignette"]

    # Ken Burns: ズームレートをフレーム単位で計算（30fps基準）
    fps = 30
    total_frames = int(duration * fps)
    zoom_rate = (zoom_end - zoom_start) / total_frames

    # zoompan: ゆっくりズーム + 中央固定 + わずかな横移動
    pan_expr = f"iw/2-(iw/zoom/2)+{pan_x}*t*iw/zoom"

    zoompan_filter = (
        f"zoompan="
        f"z='min(zoom+{zoom_rate:.8f},{zoom_end})':"
        f"x='{pan_expr}':"
        f"y='ih/2-(ih/zoom/2)':"
        f"d=1:"
        f"s={width}x{height}:"
        f"fps={fps}"
    )

    # 明度・彩度調整
    eq_filter = (
        f"eq=brightness={brightness - 1.0:.3f}:"
        f"saturation={saturation:.2f}"
    )

    # 周辺減光（vignette）
    vignette_filter = f"vignette=angle=PI/4:mode=backward" if vignette > 0 else ""

    # format変換（YouTubeはyuv420p必須）
    format_filter = "format=yuv420p"

    # フィルタチェーン組み立て
    filters = [zoompan_filter, eq_filter]
    if vignette_filter:
        filters.append(vignette_filter)
    filters.append(format_filter)

    return ",".join(filters)


def make_video(
    image_path: str,
    audio_path: str,
    output_path: str,
    category: str = "study",
    duration: int = 3600,
    title: str = "",
    crf: int = 20,
):
    """メイン動画生成関数"""
    effect = CATEGORY_EFFECTS.get(category, DEFAULT_EFFECT)
    print(f"\n[START] Latte BGM 動画生成")
    print(f"  カテゴリ : {category} ({effect['description']})")
    print(f"  画像     : {image_path}")
    print(f"  音源     : {audio_path}")
    print(f"  出力     : {output_path}")
    print(f"  長さ     : {duration // 60}分")

    # 出力ディレクトリ作成
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    with tempfile.TemporaryDirectory() as tmpdir:
        # ── 音源ループ ──
        looped_audio = os.path.join(tmpdir, "looped_audio.aac")
        final_audio  = loop_audio(audio_path, duration, looped_audio)

        # ── ffmpegフィルタ生成 ──
        vf = build_ffmpeg_filter(effect, duration)
        print(f"\n[FILTER] {vf[:80]}...")

        # ── ffmpeg実行 ──
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1",
            "-i", image_path,
            "-i", final_audio,
            "-vf", vf,
            "-c:v", "libx264",
            "-preset", "slow",          # YouTube品質優先
            "-crf", str(crf),
            "-c:a", "aac",
            "-b:a", "192k",
            "-ar", "44100",
            "-t", str(duration),
            "-movflags", "+faststart",   # YouTubeストリーミング対応
            output_path
        ]

        # タイトルメタデータ付与
        if title:
            cmd = cmd[:-1] + ["-metadata", f"title={title}", output_path]

        print(f"\n[FFmpeg] 実行中... ({duration//60}分動画の生成には時間がかかります)")
        print("  ※ 完了まで数分〜数十分かかる場合があります")

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"[ERROR] FFmpeg失敗:\n{result.stderr[-500:]}")
            sys.exit(1)

        print(f"\n[DONE] 生成完了: {output_path}")
        size_mb = os.path.getsize(output_path) / (1024 * 1024)
        print(f"       ファイルサイズ: {size_mb:.1f} MB")


def main():
    parser = argparse.ArgumentParser(
        description="Latte BGM: 画像+音源 → YouTube用BGM動画生成"
    )
    parser.add_argument("image",   help="入力画像ファイル (.png/.jpg)")
    parser.add_argument("audio",   help="入力音源ファイル (.mp3/.wav/.aac)")
    parser.add_argument("--category", "-c",
        choices=list(CATEGORY_EFFECTS.keys()), default="study",
        help="カテゴリ (演出が変わります)")
    parser.add_argument("--duration", "-d", type=int, default=3600,
        help="動画の長さ（秒）デフォルト3600=60分")
    parser.add_argument("--output", "-o", default=None,
        help="出力先MP4パス（省略時: 自動生成）")
    parser.add_argument("--title", "-t", default="",
        help="動画メタデータのタイトル")
    parser.add_argument("--crf", type=int, default=20,
        help="映像品質 (0=最高品質/大容量, 51=最低品質 デフォルト:20)")
    parser.add_argument("--list-categories", action="store_true",
        help="利用可能なカテゴリと演出を表示")

    args = parser.parse_args()

    if args.list_categories:
        print("\n利用可能なカテゴリ:")
        for name, eff in CATEGORY_EFFECTS.items():
            print(f"  {name:10s} → {eff['description']}")
        sys.exit(0)

    # 出力パス自動生成
    if args.output is None:
        stem = Path(args.image).stem
        args.output = f"../../assets/latte_bgm/videos/drafts/{stem}_{args.duration//60}min.mp4"

    make_video(
        image_path=args.image,
        audio_path=args.audio,
        output_path=args.output,
        category=args.category,
        duration=args.duration,
        title=args.title,
        crf=args.crf,
    )


if __name__ == "__main__":
    main()
