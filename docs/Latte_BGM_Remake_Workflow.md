# Latte BGM Remake Workflow

参照元: `Kei_Life_OS_v2.md`
作成日: 2026-06-06

---

## 目的

ChatGPT（アーク）で生成した高品質ビジュアル画像を使い、既存Latte BGM動画をより高品質に作り直す。
将来的にはCodexで全自動化するが、現時点ではClaude Code + FFmpegで整備する。

---

## 全体フロー

```
[1] ChatGPTで画像生成
        ↓
[2] 画像をassets/latte_bgm/images/source/[カテゴリ]/ に保存
        ↓
[3] Sunoで音源生成
        ↓
[4] 音源をassets/latte_bgm/audio/source/ に保存
        ↓
[5] make_video_from_image.py で動画生成
        ↓
[6] assets/latte_bgm/videos/drafts/ に出力
        ↓
[7] 確認・OKなら videos/final/ へ移動
        ↓
[8] metadata/ のタイトル・説明文を確認
        ↓
[9] YouTubeアップロード
        ↓
[10] 既存動画をサムネ差し替え or 新動画に置き換え
```

---

## スクリプト一覧

| スクリプト | 用途 | 推奨使用場面 |
|-----------|------|-----------|
| `make_video_from_image.py` | 画像1枚+音源→1時間MP4 | 1本ずつ確認しながら作る |
| `make_video_from_image_ffmpeg.sh` | 同上（シェル版） | ターミナルから直接実行 |
| `batch_make_videos.py` | CSV設定で複数本を一括生成 | まとめて量産するとき |

---

## Step 1: 画像の準備

### ChatGPTへのプロンプト参考

プロンプトは `assets/latte_bgm/prompts/image_prompts/` に保存する。

```
基本構成:
[シーン説明], [雰囲気・光の描写], [スタイル指定], [比率指定]

例（workout / boxercise / female）:
A focused female boxer training in a professional gym with dramatic
side lighting and cinematic atmosphere. Dark background with
spotlight on subject. Photorealistic, high quality, 16:9 ratio.
```

### 保存ルール

```
assets/latte_bgm/images/source/[カテゴリ]/[命名規則].png

命名規則: カテゴリ_テーマ_人物性別_番号.png

例:
  workout_boxercise_female_001.png
  workout_beast_mode_male_001.png
  study_deep_focus_female_001.png
  sleep_rainy_night_male_001.png
  nature_forest_rain_no_person_001.png
  cafe_cozy_cafe_male_001.png
```

---

## Step 2: 動画生成

### 基本コマンド

```bash
cd scripts/latte_bgm

# Boxercise workout動画（60分）
python3 make_video_from_image.py \
  ../../assets/latte_bgm/images/source/workout/workout_boxercise_female_001.png \
  ../../assets/latte_bgm/audio/source/boxercise_beat.mp3 \
  --category workout \
  --duration 3600 \
  --title "1 Hour Boxercise Workout Music 2026 | Latte BGM" \
  --output ../../assets/latte_bgm/videos/drafts/workout_boxercise_60min_001.mp4
```

### カテゴリ別演出一覧

```bash
python3 make_video_from_image.py --list-categories
```

| カテゴリ | 演出 |
|---------|------|
| workout | 強めのスローズーム + ジム照明感 |
| study   | ゆっくりズーム + ランプの揺らぎ感 |
| sleep   | 超スローズーム + 暗め + 低刺激 |
| nature  | 霧・雨・川の流れ感 + ゆっくりズーム |
| cafe    | 暖色の光 + ゆっくりズーム |
| relax   | 夕方の光 + ゆっくりズーム |

### シェル版（ffmpeg直接）

```bash
chmod +x make_video_from_image_ffmpeg.sh

./make_video_from_image_ffmpeg.sh \
  ../../assets/latte_bgm/images/source/workout/workout_boxercise_female_001.png \
  ../../assets/latte_bgm/audio/source/boxercise_beat.mp3 \
  workout
```

### バッチ生成

```bash
python3 batch_make_videos.py batch_config.csv --dry-run   # 確認
python3 batch_make_videos.py batch_config.csv              # 実行
python3 batch_make_videos.py batch_config.csv --skip-done  # 既存スキップ
```

---

## Step 3: 確認・ファイル移動

```bash
# 確認OKなら final/ へ
mv assets/latte_bgm/videos/drafts/workout_boxercise_60min_001.mp4 \
   assets/latte_bgm/videos/final/

# サムネイル用画像もコピー
cp assets/latte_bgm/images/source/workout/workout_boxercise_female_001.png \
   assets/latte_bgm/images/thumbnails/workout/
```

---

## Step 4: YouTubeアップロード

### メタデータ確認

```
assets/latte_bgm/metadata/titles/workout_boxercise_001.txt
assets/latte_bgm/metadata/descriptions/workout_boxercise_001.txt
assets/latte_bgm/metadata/upload_checklists/workout_boxercise_001.md
```

### アップロード手順

1. YouTube Studio を開く
2. `videos/final/` のMP4をアップロード
3. `metadata/titles/` からタイトルをコピー
4. `metadata/descriptions/` から説明文をコピー
5. `images/thumbnails/` からサムネを設定
6. プレイリストに追加
7. 公開

---

## 既存動画の差し替え方針

詳細: `Latte_BGM_Existing_Video_Remake_Map.md`

| 方針 | 判断基準 |
|------|---------|
| サムネのみ差し替え | 動画本体の品質が許容範囲の場合 |
| 動画ごと作り直し | 静止画のみ・画質が低い・ビジュアルが合っていない |
| 新規追加 | Workoutなど新カテゴリ |

---

## Codexへの引き継ぎ注意点

将来Codexで自動化するときの前提:

```
1. このフォルダ構成を変えない
2. 命名規則を変えない
3. CATEGORY_EFFECTS の辞書をベースにカテゴリ追加する
4. batch_make_videos.py の CSV仕様を維持する
5. メタデータは metadata/ に統一する
6. 音源・動画・画像はGitHubに入れない（.gitignore対応済み）
7. scripts/ と docs/ だけGitで管理する
```

自動化候補:
- ChatGPT APIで画像生成 → source/ へ自動保存
- batch_make_videos.py をCronで定期実行
- YouTube Data APIで自動アップロード
- メタデータをCSVから自動生成
