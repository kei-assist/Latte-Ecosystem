#!/usr/bin/env python3
"""
Latte BGM - make_video_from_image.py  v2.0
===========================================
画像 + 音源 → YouTube用BGM動画（1920x1080 MP4・最大60分）

【使い方】
  python3 make_video_from_image.py \\
    --image  ../../assets/latte_bgm/images/source/workout/workout_boxercise_female_001.png \\
    --audio  ../../assets/latte_bgm/audio/source/workout_boxercise_001.mp3 \\
    --preset workout_boxercise \\
    --duration 3600 \\
    --title "1 Hour Boxercise Workout Music 2026 | Female Fitness Motivation BGM | Latte BGM"

【preset 一覧】
  Workout: workout_beast_mode / workout_boxercise / workout_running
           workout_hiit_circuit / workout_gym_motivation
  Sleep  : sleep_soft / sleep_rainy_night / sleep_deep_night
  その他 : study / nature / cafe / relax / workout / sleep  (後方互換)

【仕組み】
  zoompan より大幅に高速な scale+crop(時間変化)+scale で Ken Burns 効果を実現。
  音源が短い場合は自動でループ。雨プリセットは geq フィルタで雨筋を合成。
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# リポジトリルートからの相対パス表示用
_REPO_ROOT = Path(__file__).parent.parent.parent.resolve()

# ─────────────────────────────────────────────────────────────────
#  PRESET 定義
#  brightness / contrast / saturation は ffmpeg eq フィルタの値
#    brightness: オフセット (-1.0 ～ +1.0、0.0=変化なし)
#    contrast  : 乗数 (1.0=変化なし、1.2=コントラスト強め)
#    saturation: 乗数 (1.0=変化なし、0.8=彩度下げ、1.2=上げ)
#  zoom_end: 動画終了時のズーム倍率 (1.0=変化なし、1.2=20%ズームイン)
#  pan_px_per_sec: 横方向のドリフト速度（ピクセル/秒）
#  blur: ソフトフォーカス強度 (0=なし、1.0=弱め、2.0=強め)
#  rain: True のとき geq で雨筋オーバーレイを追加
# ─────────────────────────────────────────────────────────────────

PRESETS: dict[str, dict] = {

    # ── Workout ─────────────────────────────────────────────────
    "workout_beast_mode": {
        "category":      "workout",
        "zoom_start":    1.00,
        "zoom_end":      1.28,   # 強めのズーム
        "pan_px_per_sec": 0.28,
        "brightness":    0.03,
        "contrast":      1.18,
        "saturation":    1.20,
        "vignette":      True,
        "blur":          0.0,
        "rain":          False,
        "description":   "強めのズーム + 高コントラスト + 力強い印象",
    },
    "workout_boxercise": {
        "category":      "workout",
        "zoom_start":    1.00,
        "zoom_end":      1.22,
        "pan_px_per_sec": 0.50,  # 横移動でパンチの勢い感
        "brightness":    0.05,
        "contrast":      1.12,
        "saturation":    1.15,
        "vignette":      True,
        "blur":          0.0,
        "rain":          False,
        "description":   "やや強めのズーム + 軽い横移動 + ジム照明感",
    },
    "workout_running": {
        "category":      "workout",
        "zoom_start":    1.00,
        "zoom_end":      1.18,
        "pan_px_per_sec": 0.80,  # 前進感の強い横ドリフト
        "brightness":    0.08,   # 朝焼けの明るさ
        "contrast":      1.06,
        "saturation":    1.10,
        "vignette":      True,
        "blur":          0.0,
        "rain":          False,
        "description":   "前進感のある横移動 + 朝焼けの明るさ + 疾走感",
    },
    "workout_hiit_circuit": {
        "category":      "workout",
        "zoom_start":    1.00,
        "zoom_end":      1.20,
        "pan_px_per_sec": 0.40,
        "brightness":    0.04,
        "contrast":      1.08,
        "saturation":    1.12,
        "vignette":      True,
        "blur":          0.0,
        "rain":          False,
        "description":   "テンポ感のあるズーム + 高強度感",
    },
    "workout_gym_motivation": {
        "category":      "workout",
        "zoom_start":    1.00,
        "zoom_end":      1.12,
        "pan_px_per_sec": 0.15,
        "brightness":   -0.02,
        "contrast":      1.05,
        "saturation":    1.05,
        "vignette":      True,
        "blur":          0.0,
        "rain":          False,
        "description":   "ゆっくりズーム + 落ち着いた集中感 + 派手すぎない",
    },

    # ── Sleep ───────────────────────────────────────────────────
    "sleep_soft": {
        "category":      "sleep",
        "zoom_start":    1.00,
        "zoom_end":      1.06,   # 非常に遅いズーム
        "pan_px_per_sec": 0.025,
        "brightness":   -0.18,
        "contrast":      0.95,
        "saturation":    0.80,
        "vignette":      True,
        "blur":          0.6,    # ソフトフォーカス（弱いグロー感）
        "rain":          False,
        "description":   "非常に遅いズーム + 低刺激 + ソフトフォーカス",
    },
    "sleep_rainy_night": {
        "category":      "sleep",
        "zoom_start":    1.00,
        "zoom_end":      1.08,
        "pan_px_per_sec": 0.04,
        "brightness":   -0.22,   # 暗め（夜の雰囲気）
        "contrast":      0.90,
        "saturation":    0.72,   # 低彩度（青系にシフト）
        "vignette":      True,
        "blur":          0.9,    # 雨の夜のぼかし感
        "rain":          True,   # 雨筋オーバーレイ有効
        "description":   "雨筋エフェクト + ゆっくりズーム + 暗め + 青系",
    },
    "sleep_deep_night": {
        "category":      "sleep",
        "zoom_start":    1.00,
        "zoom_end":      1.04,   # 動きは最小限
        "pan_px_per_sec": 0.01,
        "brightness":   -0.30,   # かなり暗め
        "contrast":      0.88,
        "saturation":    0.68,
        "vignette":      True,
        "blur":          1.2,    # 霧・ぼかし感
        "rain":          False,
        "description":   "動きは最小限 + 暗め + 霧ぼかし感 + 寝落ち用",
    },

    # ── 後方互換：旧 --category 名 ──────────────────────────────
    "workout": {
        "category": "workout", "zoom_start": 1.00, "zoom_end": 1.18,
        "pan_px_per_sec": 0.30, "brightness": 0.02, "contrast": 1.10,
        "saturation": 1.10, "vignette": True, "blur": 0.0, "rain": False,
        "description": "標準Workout (workout_gym_motivationと同等)",
    },
    "sleep": {
        "category": "sleep", "zoom_start": 1.00, "zoom_end": 1.06,
        "pan_px_per_sec": 0.025, "brightness": -0.18, "contrast": 0.95,
        "saturation": 0.80, "vignette": True, "blur": 0.6, "rain": False,
        "description": "標準Sleep (sleep_softと同等)",
    },
    "study": {
        "category": "study", "zoom_start": 1.00, "zoom_end": 1.12,
        "pan_px_per_sec": 0.10, "brightness": -0.05, "contrast": 1.00,
        "saturation": 0.95, "vignette": True, "blur": 0.0, "rain": False,
        "description": "ゆっくりズーム + 落ち着いた集中感",
    },
    "nature": {
        "category": "nature", "zoom_start": 1.00, "zoom_end": 1.15,
        "pan_px_per_sec": 0.20, "brightness": -0.02, "contrast": 1.00,
        "saturation": 1.05, "vignette": True, "blur": 0.0, "rain": False,
        "description": "霧・雨・川の流れ感 + ゆっくりズーム",
    },
    "cafe": {
        "category": "cafe", "zoom_start": 1.00, "zoom_end": 1.10,
        "pan_px_per_sec": 0.15, "brightness": 0.02, "contrast": 1.00,
        "saturation": 1.08, "vignette": True, "blur": 0.0, "rain": False,
        "description": "暖色の光 + ゆっくりズーム",
    },
    "relax": {
        "category": "relax", "zoom_start": 1.00, "zoom_end": 1.10,
        "pan_px_per_sec": 0.10, "brightness": 0.00, "contrast": 1.00,
        "saturation": 1.00, "vignette": True, "blur": 0.0, "rain": False,
        "description": "夕方の光 + ゆっくりズーム",
    },
}

# デフォルト出力サイズ
OUT_W, OUT_H = 1920, 1080


# ─────────────────────────────────────────────────────────────────
#  エラーメッセージ
# ─────────────────────────────────────────────────────────────────

def check_file(path: str, role: str, hint_dir: str = "") -> bool:
    """
    ファイル存在確認。
    Returns True if file exists, False if not.
    exit_on_fail=True の場合は見つからなければ終了。
    """
    if os.path.isfile(path):
        return True

    # 絶対パスを相対パスに変換して読みやすく表示
    try:
        rel = Path(path).resolve().relative_to(_REPO_ROOT)
        display_path = str(rel)
    except ValueError:
        display_path = path

    print()
    print(f"  ❌  {role}が見つかりません")
    print(f"      置く場所: {display_path}")
    if hint_dir:
        print(f"      フォルダ : {hint_dir}")
    return False


def check_file_or_exit(path: str, role: str, hint_dir: str = "") -> None:
    """ファイルが存在しなければエラーを出して終了"""
    if not check_file(path, role, hint_dir):
        print()
        sys.exit(1)


# ─────────────────────────────────────────────────────────────────
#  音源ループ
# ─────────────────────────────────────────────────────────────────

def get_audio_duration(audio_path: str) -> float:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", audio_path],
        capture_output=True, text=True,
    )
    try:
        return float(result.stdout.strip())
    except ValueError:
        return 0.0


def loop_audio(audio_path: str, target_sec: float, out_path: str) -> str:
    dur = get_audio_duration(audio_path)
    if dur <= 0:
        print(f"[ERROR] 音源の長さを取得できません: {audio_path}")
        sys.exit(1)
    if dur >= target_sec:
        print(f"[INFO] 音源 {dur:.0f}秒 ≥ 目標 {target_sec:.0f}秒 → ループ不要")
        return audio_path
    print(f"[INFO] 音源 {dur:.0f}秒 → {target_sec:.0f}秒にループ中...")
    subprocess.run(
        ["ffmpeg", "-y", "-stream_loop", "-1", "-i", audio_path,
         "-t", str(target_sec), "-c", "copy", out_path],
        check=True, capture_output=True,
    )
    print(f"[INFO] ループ完了: {out_path}")
    return out_path


# ─────────────────────────────────────────────────────────────────
#  フィルタ生成  (scale → crop → scale → eq → blur → rain → vignette)
# ─────────────────────────────────────────────────────────────────

def build_vf(preset: dict, duration: int, w=OUT_W, h=OUT_H) -> str:
    """
    Ken Burns 効果: scale(up) → time-varying crop → scale(out_size)
    ズームイン: t=0 でズーム1x（全体表示）、t=duration で zoom_end x（中央拡大）

    crop_w(t) = w × (zoom_end − zoom_range × min(t,D)/D)
      t=0  → crop_w = w × zoom_end  (全体)
      t=D  → crop_w = w × zoom_start (= w for start=1.0、中央部分)
    """
    z_end  = preset["zoom_end"]
    z_rng  = z_end - preset["zoom_start"]   # zoom_range
    D      = duration
    pan    = preset.get("pan_px_per_sec", 0.0)

    # プリスケールサイズ（偶数に丸める）
    sw = int(w * z_end);  sw += sw % 2
    sh = int(h * z_end);  sh += sh % 2

    # 安全な横ドリフト量: 利用可能スペースの50%以内に収める
    avail_x = (sw - w) / 2.0
    max_pan_total = avail_x * 0.50
    safe_pan = min(abs(pan), max_pan_total / D if D > 0 else 0) * (1 if pan >= 0 else -1)

    crop_w_e = f"{w}*({z_end:.4f}-{z_rng:.4f}*min(t,{D})/{D})"
    crop_h_e = f"{h}*({z_end:.4f}-{z_rng:.4f}*min(t,{D})/{D})"
    pan_e    = f"+{safe_pan:.5f}*t" if abs(safe_pan) > 1e-5 else ""
    crop_x_e = f"max(0,min({sw}-({crop_w_e}),({sw}-({crop_w_e}))/2{pan_e}))"
    crop_y_e = f"({sh}-({crop_h_e}))/2"

    crop_f = f"crop=w='{crop_w_e}':h='{crop_h_e}':x='{crop_x_e}':y='{crop_y_e}'"

    eq_f = (
        f"eq=brightness={preset['brightness']:.3f}"
        f":contrast={preset['contrast']:.2f}"
        f":saturation={preset['saturation']:.2f}"
    )

    chain = [
        f"scale={sw}:{sh}",   # 事前アップスケール
        crop_f,               # 時間変化クロップ（Ken Burns）
        f"scale={w}:{h}",     # 出力サイズに戻す
        eq_f,                 # 色補正
    ]

    # ── ソフトフォーカス（sleep系）──
    blur = preset.get("blur", 0.0)
    if blur > 0:
        chain.append(f"gblur=sigma={blur:.1f}")

    # ── 雨筋オーバーレイ（sleep_rainy_night）──
    # 斜め雨筋: 青みがかった細い縦線が斜めに流れる
    # floor(X/14)*53 で14px幅ごとにランダムな位相を持つ独立した雨筋
    if preset.get("rain"):
        chain.append(
            "geq="
            "r='if(lt(mod(X*0.30+Y+T*480+floor(X/14)*53,58),1.4),min(r+14,255),r)':"
            "g='if(lt(mod(X*0.30+Y+T*480+floor(X/14)*53,58),1.4),min(g+11,255),g)':"
            "b='if(lt(mod(X*0.30+Y+T*480+floor(X/14)*53,58),1.4),min(b+26,255),b)'"
        )

    # ── 周辺減光（vignette）──
    if preset.get("vignette"):
        chain.append("vignette=angle=PI/4:mode=backward")

    chain.append("format=yuv420p")
    return ",".join(chain)


# ─────────────────────────────────────────────────────────────────
#  メイン動画生成
# ─────────────────────────────────────────────────────────────────

def dry_run_check(
    image_path: str,
    audio_path: str,
    output_path: str,
    preset_name: str,
    duration: int,
    title: str,
) -> None:
    """--dry-run: ファイル確認・設定表示のみ（動画は生成しない）"""
    preset = PRESETS.get(preset_name, {})
    category = preset.get("category", "unknown")

    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║          Latte BGM  dry-run チェック                 ║")
    print("╚══════════════════════════════════════════════════════╝")
    print()

    # ── ファイル確認 ──────────────────────────────────────────────
    img_ok  = check_file(image_path, "画像",
                         f"assets/latte_bgm/images/source/{category}/")
    audio_ok = check_file(audio_path, "音源",
                          "assets/latte_bgm/audio/source/")
    print()

    if img_ok:
        img_size = os.path.getsize(image_path) / 1024
        print(f"  ✅  画像: {image_path}  ({img_size:.0f} KB)")
    if audio_ok:
        dur = get_audio_duration(audio_path)
        print(f"  ✅  音源: {audio_path}  ({dur:.0f}秒)")

    print()
    print("─── 生成パラメータ ─────────────────────────────────────")
    print(f"  Preset   : {preset_name}")
    print(f"  演出     : {preset.get('description','')}")
    print(f"  長さ     : {duration // 60}分 ({duration}秒)")
    print(f"  出力先   : {output_path}")
    if title:
        print(f"  タイトル : {title}")

    if preset:
        vf = build_vf(preset, duration)
        print(f"\n─── ffmpeg フィルタ（先頭100文字）─────────────────────")
        print(f"  {vf[:100]}...")

    print()
    all_ok = img_ok and audio_ok
    if all_ok:
        print("  ✅  準備完了！以下のコマンドで動画を生成できます")
        print()
        print("     python3 make_video_from_image.py \\")
        print(f"       --image  {image_path} \\")
        print(f"       --audio  {audio_path} \\")
        print(f"       --preset {preset_name} \\")
        print(f"       --duration {duration} \\")
        if title:
            print(f'       --title  "{title}" \\')
        print(f"       --output {output_path}")
    else:
        print("  ❌  不足ファイルがあります。上記のパスにファイルを置いてから再実行してください。")

    print()


def test_render(
    image_path: str,
    audio_path: str,
    preset_name: str,
    test_sec: int = 10,
) -> None:
    """
    --test-render: 10秒のテスト動画を生成してパイプライン動作を確認する。
    実際のファイル（画像・音源）が必要。
    """
    preset = PRESETS.get(preset_name)
    if preset is None:
        print(f"[ERROR] 未知の preset: {preset_name}")
        sys.exit(1)

    check_file_or_exit(image_path, "画像",
                       f"assets/latte_bgm/images/source/{preset['category']}/")
    check_file_or_exit(audio_path, "音源", "assets/latte_bgm/audio/source/")

    out_path = f"/tmp/latte_bgm_test_{preset_name}_{test_sec}sec.mp4"

    print()
    print(f"[TEST RENDER] {test_sec}秒テスト動画を生成します...")
    print(f"  Preset: {preset_name}")
    print(f"  出力  : {out_path}")
    print()

    vf = build_vf(preset, test_sec)

    with tempfile.TemporaryDirectory() as tmpdir:
        looped = os.path.join(tmpdir, "loop.aac")
        final_audio = loop_audio(audio_path, test_sec, looped)

        cmd = [
            "ffmpeg", "-y",
            "-loop", "1", "-i", image_path,
            "-i", final_audio,
            "-vf", vf,
            "-c:v", "libx264", "-preset", "fast", "-crf", "23",
            "-c:a", "aac", "-b:a", "128k",
            "-r", "30", "-t", str(test_sec),
            "-movflags", "+faststart",
            out_path,
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"[ERROR] テストレンダリング失敗:\n{result.stderr[-400:]}")
        sys.exit(1)

    size_kb = os.path.getsize(out_path) / 1024
    print(f"  ✅  テスト完了! {size_kb:.0f} KB")
    print(f"  再生して確認: open {out_path}")
    print()
    print("  ← 映像・音声が正常なら 60分版を生成できます")
    print()


def make_video(
    image_path: str,
    audio_path: str,
    output_path: str,
    preset_name: str = "study",
    duration: int = 3600,
    title: str = "",
    crf: int = 20,
    preset_override: str = "slow",
) -> None:
    preset = PRESETS.get(preset_name)
    if preset is None:
        print(f"[ERROR] 未知の preset: '{preset_name}'")
        print(f"  利用可能: {', '.join(PRESETS.keys())}")
        sys.exit(1)

    # ファイル確認
    check_file_or_exit(
        image_path, "画像",
        f"assets/latte_bgm/images/source/{preset['category']}/",
    )
    check_file_or_exit(
        audio_path, "音源",
        "assets/latte_bgm/audio/source/",
    )

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    print(f"\n{'='*55}")
    print(f"  Latte BGM 動画生成")
    print(f"{'='*55}")
    print(f"  Preset  : {preset_name}")
    print(f"  演出    : {preset['description']}")
    print(f"  画像    : {image_path}")
    print(f"  音源    : {audio_path}")
    print(f"  出力    : {output_path}")
    print(f"  長さ    : {duration // 60}分")
    print(f"{'='*55}\n")

    with tempfile.TemporaryDirectory() as tmpdir:
        # 音源ループ
        looped = os.path.join(tmpdir, "loop.aac")
        final_audio = loop_audio(audio_path, duration, looped)

        # フィルタ生成
        vf = build_vf(preset, duration)
        print(f"[FILTER] {vf[:90]}{'...' if len(vf)>90 else ''}\n")

        # ffmpeg コマンド組み立て
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1",
            "-i", image_path,
            "-i", final_audio,
            "-vf", vf,
            "-c:v", "libx264",
            "-preset", preset_override,
            "-crf", str(crf),
            "-c:a", "aac",
            "-b:a", "192k",
            "-ar", "44100",
            "-r", "30",
            "-t", str(duration),
            "-movflags", "+faststart",
        ]
        if title:
            cmd += ["-metadata", f"title={title}"]
        cmd.append(output_path)

        print("[FFmpeg] 実行中... (60分動画は数分〜20分程度かかります)")
        print("         rain=True のプリセットはやや時間がかかります\n")

        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"[ERROR] FFmpeg 失敗:\n{result.stderr[-600:]}")
            sys.exit(1)

        size_mb = os.path.getsize(output_path) / (1024 * 1024)
        print(f"\n[DONE] 生成完了!")
        print(f"  出力: {output_path}")
        print(f"  サイズ: {size_mb:.1f} MB\n")


# ─────────────────────────────────────────────────────────────────
#  CLI
# ─────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Latte BGM: 画像 + 音源 → YouTube用BGM動画",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例 (Workout / Boxercise):
  python3 make_video_from_image.py \\
    --image ../../assets/latte_bgm/images/source/workout/workout_boxercise_female_001.png \\
    --audio ../../assets/latte_bgm/audio/source/workout_boxercise_001.mp3 \\
    --preset workout_boxercise \\
    --title "1 Hour Boxercise Workout Music 2026 | Latte BGM"

使用例 (Sleep / Rainy Night):
  python3 make_video_from_image.py \\
    --image ../../assets/latte_bgm/images/source/sleep/sleep_rainy_night_001.png \\
    --audio ../../assets/latte_bgm/audio/source/sleep_rainy_night_001.mp3 \\
    --preset sleep_rainy_night \\
    --title "1 Hour Sleep Music 2026 | Rainy Night BGM | Latte BGM"
        """,
    )
    # --image / --audio (推奨) + 旧来の positional args も受け付ける
    parser.add_argument("--image",  "-i", default=None, help="入力画像 (.png/.jpg)")
    parser.add_argument("--audio",  "-a", default=None, help="入力音源 (.mp3/.wav/.aac)")
    parser.add_argument("--preset", "-p", default=None,
        help=f"演出プリセット ({', '.join(PRESETS.keys())})")
    parser.add_argument("--category", "-c", default=None,
        help="カテゴリ (preset が未指定の場合に使用)")
    parser.add_argument("--duration", "-d", type=int, default=3600,
        help="動画の長さ（秒）[デフォルト: 3600 = 60分]")
    parser.add_argument("--output",  "-o", default=None, help="出力MP4パス")
    parser.add_argument("--title",   "-t", default="",   help="動画タイトル（メタデータ）")
    parser.add_argument("--crf",          type=int, default=20,
        help="映像品質 (18=高品質/大 ～ 28=低品質/小、デフォルト:20)")
    parser.add_argument("--encode-speed", default="slow",
        choices=["ultrafast","fast","medium","slow","veryslow"],
        help="エンコード速度 (drafts→fast, final→slow)")
    parser.add_argument("--list-presets", action="store_true",
        help="利用可能なプリセット一覧を表示して終了")
    parser.add_argument("--dry-run", "-n", action="store_true",
        help="ファイル確認・設定表示のみ。動画は生成しない（事前チェック用）")
    parser.add_argument("--test-render", action="store_true",
        help="10秒のテスト動画を生成してffmpegパイプラインを確認する")
    parser.add_argument("--test-sec", type=int, default=10,
        help="--test-render の動画の長さ（秒）[デフォルト: 10]")
    # 後方互換: 旧 positional args
    parser.add_argument("pos_image", nargs="?", help=argparse.SUPPRESS)
    parser.add_argument("pos_audio", nargs="?", help=argparse.SUPPRESS)

    args = parser.parse_args()

    if args.list_presets:
        print("\n利用可能なプリセット:")
        for name, p in PRESETS.items():
            print(f"  {name:<28} {p['description']}")
        sys.exit(0)

    # image / audio の解決（--image 優先、旧 positional 後方互換）
    image = args.image or args.pos_image
    audio = args.audio or args.pos_audio

    if not image or not audio:
        parser.error(
            "--image と --audio を指定してください\n"
            "  例: --image ../../assets/latte_bgm/images/source/workout/workout_boxercise_female_001.png\n"
            "       --audio ../../assets/latte_bgm/audio/source/workout_boxercise_001.mp3"
        )

    # preset の解決
    preset_name = args.preset or args.category
    if not preset_name:
        for cat in PRESETS:
            if cat in image.lower():
                preset_name = cat
                break
        if not preset_name:
            preset_name = "study"
            print(f"[WARN] --preset 未指定 → デフォルト '{preset_name}' を使用")

    # 出力パス自動生成
    if not args.output:
        stem = Path(image).stem
        args.output = (
            f"../../assets/latte_bgm/videos/drafts/{stem}_{args.duration//60}min.mp4"
        )

    # ── dry-run モード ────────────────────────────────────────────
    if args.dry_run:
        dry_run_check(
            image_path=image,
            audio_path=audio,
            output_path=args.output,
            preset_name=preset_name,
            duration=args.duration,
            title=args.title,
        )
        return

    # ── test-render モード ────────────────────────────────────────
    if args.test_render:
        test_render(
            image_path=image,
            audio_path=audio,
            preset_name=preset_name,
            test_sec=args.test_sec,
        )
        return

    # ── 通常生成 ─────────────────────────────────────────────────
    make_video(
        image_path=image,
        audio_path=audio,
        output_path=args.output,
        preset_name=preset_name,
        duration=args.duration,
        title=args.title,
        crf=args.crf,
        preset_override=args.encode_speed,
    )


if __name__ == "__main__":
    main()
