# Latte BGM Remake Workflow v2

参照元: `Kei_Life_OS_v2.md`
更新日: 2026-06-06

---

## これは何のためのドキュメントか

ChatGPT（アーク）が生成した高品質画像と Suno の音源を使って、
Latte BGM の動画を「静止画っぽい動画」から「YouTubeで見ても違和感のない BGM 動画」に作り直す手順書です。

**今できること**: 画像と音源を所定フォルダに入れて1コマンドを実行 → 60分動画が生成される

---

## 全体の流れ

```
1. ChatGPTで画像を生成
        ↓
2. 画像を所定フォルダへ保存
        ↓
3. Sunoで音源を生成
        ↓
4. 音源を所定フォルダへ保存
        ↓
5. スクリプト1コマンドで動画生成（15〜20分）
        ↓
6. drafts/ で確認 → OKなら final/ へ移動
        ↓
7. YouTubeアップロード
        ↓
8. 既存動画を差し替え or 新規公開
```

---

## ファイルを置く場所

### 画像

```
assets/latte_bgm/images/source/
├── workout/    ← Workout 系の画像をここへ
├── sleep/      ← Sleep 系の画像をここへ
├── study/
├── nature/
├── cafe/
└── relax/
```

**命名規則**: `カテゴリ_テーマ_性別_番号.png`
```
workout_boxercise_female_001.png
workout_beast_mode_male_001.png
sleep_rainy_night_001.png         ← 人物なしの場合は性別省略
sleep_deep_night_no_person_001.png
```

### 音源

```
assets/latte_bgm/audio/source/
└── ここにMP3を置く（命名規則: カテゴリ_テーマ_番号.mp3）

例:
  workout_boxercise_001.mp3
  sleep_rainy_night_001.mp3
```

---

## Workout 動画の作り方

### Step 1: スクリプトのディレクトリに移動

```bash
cd scripts/latte_bgm
```

### Step 2: Preset を選ぶ

| 作りたい動画 | preset |
|-----------|--------|
| 重い筋トレ・男性 | `workout_beast_mode` |
| ボクシング・女性 | `workout_boxercise` ← 最初のテスト推奨 |
| ランニング・朝焼け | `workout_running` |
| HIIT・サーキット | `workout_hiit_circuit` |
| ジム前の集中 | `workout_gym_motivation` |

### Step 3: コマンド実行

```bash
# Boxercise 動画（60分）
python3 make_video_from_image.py \
  --image ../../assets/latte_bgm/images/source/workout/workout_boxercise_female_001.png \
  --audio ../../assets/latte_bgm/audio/source/workout_boxercise_001.mp3 \
  --preset workout_boxercise \
  --duration 3600 \
  --title "1 Hour Boxercise Workout Music 2026 | Female Fitness Motivation BGM | Latte BGM" \
  --output ../../assets/latte_bgm/videos/drafts/workout_boxercise_60min_001.mp4
```

### Step 4: 出力確認

```
assets/latte_bgm/videos/drafts/workout_boxercise_60min_001.mp4
```

冒頭・中間・末尾を再生して確認。OKなら `videos/final/` に移動。

---

## Sleep 動画の作り方

### Step 1: Preset を選ぶ

| 作りたい動画 | preset |
|-----------|--------|
| 穏やかな睡眠BGM | `sleep_soft` |
| 雨の夜・窓・青系 | `sleep_rainy_night` ← 最初のテスト推奨 |
| 深夜・超暗め・寝落ち用 | `sleep_deep_night` |

### Step 2: コマンド実行

```bash
# Sleep / Rainy Night（60分）
python3 make_video_from_image.py \
  --image ../../assets/latte_bgm/images/source/sleep/sleep_rainy_night_001.png \
  --audio ../../assets/latte_bgm/audio/source/sleep_rainy_night_001.mp3 \
  --preset sleep_rainy_night \
  --duration 3600 \
  --title "1 Hour Sleep Music 2026 | Rainy Night BGM for Deep Sleep | Latte BGM" \
  --output ../../assets/latte_bgm/videos/drafts/sleep_rainy_night_60min_001.mp4
```

> **注意**: `sleep_rainy_night` は雨筋エフェクト (geq) を使用するため、
> 他プリセットより生成時間が長くなる場合があります（+5分程度）。

---

## preset の選び方

```bash
# 一覧を表示
python3 make_video_from_image.py --list-presets
```

```
workout_beast_mode     強めのズーム + 高コントラスト + 力強い印象
workout_boxercise      やや強めのズーム + 軽い横移動 + ジム照明感
workout_running        前進感のある横移動 + 朝焼けの明るさ + 疾走感
workout_hiit_circuit   テンポ感のあるズーム + 高強度感
workout_gym_motivation ゆっくりズーム + 落ち着いた集中感 + 派手すぎない
sleep_soft             非常に遅いズーム + 低刺激 + ソフトフォーカス
sleep_rainy_night      雨筋エフェクト + ゆっくりズーム + 暗め + 青系
sleep_deep_night       動きは最小限 + 暗め + 霧ぼかし感 + 寝落ち用
```

---

## 出力動画の保存場所

```
assets/latte_bgm/videos/
├── drafts/    ← 生成直後の確認用（ここで確認）
└── final/     ← YouTubeアップロード確定版（ここからYTへ）
```

---

## YouTubeにアップする前に確認すること

- [ ] 冒頭5秒が自然に始まっているか（唐突な音量変化がないか）
- [ ] ループのつなぎ目（音源が短い場合）が不自然でないか
- [ ] ズームエフェクトがゆっくり自然に動いているか（急すぎないか）
- [ ] 暗すぎ/明るすぎていないか（SleepはOKでも他はNG）
- [ ] 動画の長さが正確に60分（または設定した時間）か
- [ ] メタデータ（`metadata/titles/`）のタイトルを確認したか

---

## サムネとして使う場合の注意点

- 動画の画像（`images/source/`）をそのままサムネに使う場合、PNG → JPG に変換する
- YouTube サムネは最大 2MB、1280×720 以上を推奨
- テキストをオーバーレイする場合は `images/thumbnails/` に保存
- サムネにEP番号は入れない（Latte BGM の方針）

```bash
# PNG → JPG 変換（macOS/Linux）
convert workout_boxercise_female_001.png \
  -quality 95 \
  ../../assets/latte_bgm/images/thumbnails/workout/workout_boxercise_female_001.jpg
```

---

## シェルスクリプト版（Python なしで使う場合）

```bash
chmod +x make_video_from_image_ffmpeg.sh

# Workout / Boxercise
./make_video_from_image_ffmpeg.sh \
  ../../assets/latte_bgm/images/source/workout/workout_boxercise_female_001.png \
  ../../assets/latte_bgm/audio/source/workout_boxercise_001.mp3 \
  workout_boxercise

# Sleep / Rainy Night
./make_video_from_image_ffmpeg.sh \
  ../../assets/latte_bgm/images/source/sleep/sleep_rainy_night_001.png \
  ../../assets/latte_bgm/audio/source/sleep_rainy_night_001.mp3 \
  sleep_rainy_night
```

---

## バッチ生成（複数本まとめて）

```bash
# CSV（batch_config.csv）を作成:
# image,audio,category,duration,output,title
# workout_boxercise_female_001.png,workout_boxercise_001.mp3,workout,3600,,1 Hour Boxercise...
# sleep_rainy_night_001.png,sleep_rainy_night_001.mp3,sleep,3600,,1 Hour Sleep...

python3 batch_make_videos.py batch_config.csv --dry-run  # 確認
python3 batch_make_videos.py batch_config.csv             # 実行
```

---

## エラーが出たとき

### 「画像ファイルが見つかりません」
→ `assets/latte_bgm/images/source/[カテゴリ]/` に画像ファイルを置いてください

### 「音源ファイルが見つかりません」
→ `assets/latte_bgm/audio/source/` に音源ファイルを置いてください

### 「FFmpeg 失敗」
→ ffmpeg がインストールされているか確認: `which ffmpeg`
→ インストール: `brew install ffmpeg`

---

## Codex へ引き継ぐときの注意点

```
1. フォルダ構成を変えない
   assets/latte_bgm/images/source/[カテゴリ]/[命名規則].png
   assets/latte_bgm/audio/source/[命名規則].mp3

2. 命名規則を変えない
   カテゴリ_テーマ_性別_番号.png

3. PRESETS 辞書を維持しながら拡張する（既存を削除しない）

4. build_vf() 関数の引数仕様を維持する
   build_vf(preset: dict, duration: int) → str

5. batch_make_videos.py の CSV カラム仕様を維持する
   image, audio, category, duration, output, title

6. メタデータは assets/latte_bgm/metadata/ に統一する

7. 音源・動画・画像は Git に入れない（.gitignore 対応済み）
   scripts/ と docs/ と assets/metadata/ だけ Git 管理

8. 自動化候補（Codex実装予定）:
   - ChatGPT API で画像生成 → source/ へ自動保存
   - batch_make_videos.py を Cron/定期実行
   - YouTube Data API で自動アップロード
   - metadata/ から説明文・タグを自動生成
```
