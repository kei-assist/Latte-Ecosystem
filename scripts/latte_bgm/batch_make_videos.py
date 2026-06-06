#!/usr/bin/env python3
"""
Latte BGM - batch_make_videos.py
==================================
CSVファイルを読み込んで複数の動画を一括生成する。

CSV形式 (batch_config.csv):
    image,audio,category,duration,output,title
    workout_boxercise_female_001.png,boxercise_beat.mp3,workout,3600,,1 Hour Boxercise BGM
    study_deep_focus_female_001.png,focus_beat.mp3,study,3600,,Deep Focus Vol.5

Usage:
    python3 batch_make_videos.py batch_config.csv
    python3 batch_make_videos.py batch_config.csv --dry-run   # 実行せず内容確認
    python3 batch_make_videos.py batch_config.csv --skip-done # 出力済みをスキップ
"""

import argparse
import csv
import os
import sys
import time
from pathlib import Path

# make_video_from_image をインポート
sys.path.insert(0, str(Path(__file__).parent))
try:
    from make_video_from_image import make_video, CATEGORY_EFFECTS
except ImportError:
    print("[ERROR] make_video_from_image.py が同じフォルダにあることを確認してください")
    sys.exit(1)

# デフォルトのベースパス
BASE_IMAGE_DIR = Path(__file__).parent.parent.parent / "assets" / "latte_bgm" / "images" / "source"
BASE_AUDIO_DIR = Path(__file__).parent.parent.parent / "assets" / "latte_bgm" / "audio" / "source"
BASE_VIDEO_DIR = Path(__file__).parent.parent.parent / "assets" / "latte_bgm" / "videos" / "drafts"


def resolve_path(path_str: str, base_dir: Path, category: str = "") -> str:
    """ファイルパスを解決（絶対パス or ベースディレクトリからの相対パス）"""
    p = Path(path_str)
    if p.is_absolute():
        return str(p)
    # カテゴリサブフォルダを含む場合
    candidate = base_dir / category / path_str
    if candidate.exists():
        return str(candidate)
    candidate = base_dir / path_str
    if candidate.exists():
        return str(candidate)
    return str(candidate)  # 存在しなくてもパスを返す


def process_batch(csv_path: str, dry_run: bool = False, skip_done: bool = False):
    """CSVを読み込んで一括処理"""
    results = []
    failed  = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"\n[BATCH] {len(rows)}件を処理します")
    if dry_run:
        print("[DRY RUN] 実際には動画を生成しません\n")

    for i, row in enumerate(rows, 1):
        image_raw    = row.get("image", "").strip()
        audio_raw    = row.get("audio", "").strip()
        category     = row.get("category", "study").strip()
        duration     = int(row.get("duration", "3600").strip() or 3600)
        output_raw   = row.get("output", "").strip()
        title        = row.get("title", "").strip()

        # パス解決
        image_path = resolve_path(image_raw, BASE_IMAGE_DIR, category)
        audio_path = resolve_path(audio_raw, BASE_AUDIO_DIR)

        if not output_raw:
            stem = Path(image_raw).stem
            output_path = str(BASE_VIDEO_DIR / f"{stem}_{duration//60}min.mp4")
        else:
            output_path = resolve_path(output_raw, BASE_VIDEO_DIR)

        print(f"\n[{i}/{len(rows)}] {category.upper()} / {duration//60}min")
        print(f"    画像 : {image_path}")
        print(f"    音源 : {audio_path}")
        print(f"    出力 : {output_path}")
        if title:
            print(f"    タイトル: {title}")

        # スキップ判定
        if skip_done and Path(output_path).exists():
            print(f"    [SKIP] 既に存在します")
            results.append({"status": "skip", "output": output_path})
            continue

        # ファイル存在チェック
        if not dry_run:
            if not Path(image_path).exists():
                print(f"    [ERROR] 画像が見つかりません")
                failed.append({"row": i, "reason": "image not found", "path": image_path})
                continue
            if not Path(audio_path).exists():
                print(f"    [ERROR] 音源が見つかりません")
                failed.append({"row": i, "reason": "audio not found", "path": audio_path})
                continue

        if dry_run:
            print(f"    [DRY] make_video({category}, {duration}sec)")
            results.append({"status": "dry", "output": output_path})
            continue

        # 動画生成
        start_time = time.time()
        try:
            make_video(
                image_path=image_path,
                audio_path=audio_path,
                output_path=output_path,
                category=category,
                duration=duration,
                title=title,
            )
            elapsed = time.time() - start_time
            print(f"    [OK] {elapsed:.0f}秒で完了")
            results.append({"status": "ok", "output": output_path, "time": elapsed})
        except Exception as e:
            print(f"    [FAIL] {e}")
            failed.append({"row": i, "reason": str(e)})

    # ── 結果サマリー ──
    print(f"\n{'='*40}")
    print(f"[BATCH完了]")
    print(f"  成功: {len([r for r in results if r['status']=='ok'])}件")
    print(f"  スキップ: {len([r for r in results if r['status']=='skip'])}件")
    print(f"  失敗: {len(failed)}件")
    if failed:
        print(f"\n[失敗一覧]")
        for f in failed:
            print(f"  Row {f['row']}: {f['reason']} - {f.get('path','')}")
    print(f"{'='*40}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Latte BGM: CSVから複数動画を一括生成"
    )
    parser.add_argument("csv", help="バッチ設定CSVファイル")
    parser.add_argument("--dry-run", action="store_true",
        help="実際には生成せず内容を確認するだけ")
    parser.add_argument("--skip-done", action="store_true",
        help="出力ファイルが既に存在する場合はスキップ")

    args = parser.parse_args()

    if not os.path.exists(args.csv):
        print(f"[ERROR] CSVファイルが見つかりません: {args.csv}")
        sys.exit(1)

    process_batch(args.csv, dry_run=args.dry_run, skip_done=args.skip_done)


if __name__ == "__main__":
    main()
