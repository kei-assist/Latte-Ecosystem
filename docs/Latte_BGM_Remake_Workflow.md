# Latte BGM Remake Workflow v3

参照元: `Kei_Life_OS_v2.md`
更新日: 2026-06-06

---

## ⚡ 次に人間がやること（3ステップ）

```
1. ChatGPTで作った画像を指定フォルダに置く
   → assets/latte_bgm/images/source/[カテゴリ]/[ファイル名].png

2. Sunoで作った音源を指定フォルダに置く
   → assets/latte_bgm/audio/source/[ファイル名].mp3

3. コマンドを実行してMP4を作る（下記参照）
```

---

## これは何のためのドキュメントか

ChatGPT（アーク）で生成した高品質画像と Suno の音源を使って、
Latte BGM の動画を「静止画っぽい動画」から「YouTubeで見ても違和感のない BGM 動画」に作り直す手順書です。

**すべての動画に必ず動きを入れること（静止画のみ禁止）**

- ゆっくりズーム（Ken Burns 効果）
- 横ドリフト（pan）
- 光の揺らぎ（light_flicker）
- カメラ揺れ（camera_shake）— Workout 系

---

## 動作確認済みプリセット一覧

```bash
python3 make_video_from_image.py --list-presets
```

| preset | カテゴリ | 演出 |
|--------|---------|------|
| `workout_beast_mode` | Workout | ズーム + **照明パルス** + **カメラ揺れ** |
| `workout_boxercise` | Workout | ズーム + 横移動 + **照明揺らぎ** + **カメラ揺れ** |
| `workout_running` | Workout | 前進感横ドリフト + **朝の光揺らぎ** |
| `workout_hiit_circuit` | Workout | ズーム + **光点滅** + **カメラ揺れ** |
| `workout_gym_motivation` | Workout | ゆっくりズーム + **静かな照明揺らぎ** |
| `sleep_soft` | Sleep | 遅いズーム + **月明かり揺らぎ** + ソフトフォーカス |
| `sleep_rainy_night` | Sleep | ゆっくりズーム + 霧ぼかし + **窓明かり揺らぎ** ※1 |
| `sleep_deep_night` | Sleep | 最小ズーム + 霧ぼかし（刺激ゼロ） |
| `nature_forest_rain` | Nature | ズーム + 横移動 + 霧ぼかし + **木漏れ日揺らぎ** ※1 |
| `study_focus` | Study | ゆっくりズーム + **ランプ揺らぎ** |
| `cafe_warm` | Cafe | ゆっくりズーム + **暖色ライト揺らぎ** |

※1 rain overlay（雨粒エフェクト）は後で改良予定。現在は霧ぼかしで代替。

---

## 事前チェック（dry-run）

```bash
cd scripts/latte_bgm

python3 make_video_from_image.py \
  --image ../../assets/latte_bgm/images/source/workout/workout_boxercise_female_001.png \
  --audio ../../assets/latte_bgm/audio/source/workout_boxercise_001.mp3 \
  --preset workout_boxercise \
  --duration 3600 \
  --title "1 Hour Boxercise Workout Music 2026 | Female Fitness Motivation BGM | Latte BGM" \
  --output ../../assets/latte_bgm/videos/drafts/workout_boxercise_60min_001.mp4 \
  --dry-run
```

`✅ 準備完了！` が出たら `--dry-run` を外して実行。

---

## パイプライン動作テスト（test-render）

```bash
python3 make_video_from_image.py \
  --image ../../assets/latte_bgm/images/source/workout/workout_boxercise_female_001.png \
  --audio ../../assets/latte_bgm/audio/source/workout_boxercise_001.mp3 \
  --preset workout_boxercise \
  --test-render --test-sec 10
```

---

## ファイルを置く場所

### 画像

```
assets/latte_bgm/images/source/
├── workout/    ← Workout 系の画像
├── sleep/      ← Sleep 系の画像
├── study/
├── nature/
├── cafe/
└── relax/
```

命名規則: `カテゴリ_テーマ_性別_番号.png`

### 音源

```
assets/latte_bgm/audio/source/
└── カテゴリ_テーマ_番号.mp3
```

---

## Workout 動画の作り方

```bash
cd scripts/latte_bgm

# Boxercise（60分）
python3 make_video_from_image.py \
  --image  ../../assets/latte_bgm/images/source/workout/workout_boxercise_female_001.png \
  --audio  ../../assets/latte_bgm/audio/source/workout_boxercise_001.mp3 \
  --preset workout_boxercise \
  --duration 3600 \
  --title "1 Hour Boxercise Workout Music 2026 | Female Fitness Motivation BGM | Latte BGM" \
  --output ../../assets/latte_bgm/videos/drafts/workout_boxercise_60min_001.mp4
```

---

## Sleep 動画の作り方

```bash
# Rainy Night（60分）
python3 make_video_from_image.py \
  --image  ../../assets/latte_bgm/images/source/sleep/sleep_rainy_night_001.png \
  --audio  ../../assets/latte_bgm/audio/source/sleep_rainy_night_001.mp3 \
  --preset sleep_rainy_night \
  --duration 3600 \
  --title "1 Hour Sleep Music 2026 | Rainy Night BGM for Deep Sleep | Latte BGM" \
  --output ../../assets/latte_bgm/videos/drafts/sleep_rainy_night_60min_001.mp4
```

---

## まず60秒テスト動画で確認する

```bash
# 60秒テスト（--encode-speed fast で高速生成）
python3 make_video_from_image.py \
  --image  [画像パス] \
  --audio  [音源パス] \
  --preset [プリセット名] \
  --duration 60 \
  --output ../../assets/latte_bgm/videos/drafts/TEST_60sec.mp4 \
  --encode-speed fast
```

確認OKなら `--duration 3600` に変えて本番生成。

---

## 出力動画の保存場所

```
assets/latte_bgm/videos/
├── drafts/    ← 生成直後・確認用（ここで確認）
└── final/     ← YouTube アップロード確定版
```

---

## YouTubeにアップする前に確認すること

- [ ] 冒頭5秒が自然に始まっているか
- [ ] ループのつなぎ目が不自然でないか
- [ ] ズームと光の揺らぎが自然に見えるか
- [ ] `metadata/titles/` のタイトルを確認したか

---

## TODO: rain overlay の改良

`sleep_rainy_night` と `nature_forest_rain` では現在、
雨粒エフェクト（rain overlay）の代わりに**霧ぼかし（mist）**を使用しています。

将来の改良候補：
- 雨ループ動画素材のオーバーレイ（ffmpeg `-filter_complex` を使用）
- `geq` フィルタの代替実装（ffmpeg バージョン依存の問題を解決後）

---

## シェルスクリプト版

```bash
chmod +x make_video_from_image_ffmpeg.sh

./make_video_from_image_ffmpeg.sh \
  ../../assets/latte_bgm/images/source/workout/workout_boxercise_female_001.png \
  ../../assets/latte_bgm/audio/source/workout_boxercise_001.mp3 \
  workout_boxercise
```

---

## Codex へ引き継ぐときの注意点

```
1. PRESETS 辞書を拡張（既存を削除しない）
2. build_vf() の引数仕様を維持 — build_vf(preset, duration)
3. 新エフェクト: light_flicker(eq eval=frame) / camera_shake(crop sin波)
4. geq フィルタで T（大文字）、crop/eq では t（小文字）
5. rain=False のままコミット — 雨筋実装は別タスクで対応
6. assets/latte_bgm/ のフォルダ構成・命名規則を変えない
7. 音源・動画・画像は Git に入れない（.gitignore 対応済み）
```
