# Latte BGM Visual Asset Guide

参照元: `Kei_Life_OS_v2.md`
作成日: 2026-06-06

---

## 命名規則

### 画像ファイル

```
カテゴリ_テーマ_人物性別_番号.png

[カテゴリ] : workout / study / sleep / nature / cafe / relax
[テーマ]   : スネークケース（スペースをアンダースコアに）
[人物性別] : female / male / no_person
[番号]     : 3桁ゼロ埋め（001〜）
```

### 動画ファイル

```
カテゴリ_テーマ_長さ_番号.mp4

[長さ] : 60min / 120min / 3min（Shorts）
```

---

## カテゴリ別 命名例・画像仕様

### workout（筋トレ・ジム・フィットネス）

| ファイル名 | 画像の内容 |
|---------|---------|
| `workout_boxercise_female_001.png` | ジムでボクシングフィットネスをする女性。ドラマチックな側面照明 |
| `workout_boxercise_female_002.png` | 同テーマ・別構図またはポーズ |
| `workout_running_female_001.png` | 朝のランニング。朝焼け・前進感 |
| `workout_beast_mode_male_001.png` | 男性がデッドリフト。強烈な照明・汗 |
| `workout_circuit_female_001.png` | 女性がサーキットトレーニング |
| `workout_gym_motivation_male_001.png` | ジムのダンベルエリア・モチベーション感 |
| `workout_hiit_female_001.png` | HIIT・バーピー・ダイナミックな動き |

**画像仕様:**
- 画面は暗め・スポットライト
- 人物は動感・筋肉感を出す
- 背景はジム・コンクリート・都市夜景
- 16:9横長（1920×1080 or より大きいサイズ）

---

### study（勉強・集中・コーディング）

| ファイル名 | 画像の内容 |
|---------|---------|
| `study_deep_focus_female_001.png` | 暗い部屋でデスクワーク。ランプの光 |
| `study_deep_focus_male_001.png` | 同テーマ・男性 |
| `study_coding_male_001.png` | コーディング。複数モニター・夜 |
| `study_desk_lamp_no_person_001.png` | デスクとランプのみ。人物なし |
| `study_library_female_001.png` | 図書館での読書・勉強 |
| `study_exam_prep_female_001.png` | 試験前の集中した勉強風景 |

**画像仕様:**
- 暖かいランプの光・落ち着いた色調
- 本・PC・ノートなどのディテール
- 背景はぼかしてもOK（集中感）
- 人物は顔を出さない or 横顔・後ろ姿を推奨

---

### sleep（睡眠・深い休息）

| ファイル名 | 画像の内容 |
|---------|---------|
| `sleep_rainy_night_male_001.png` | 夜の窓・雨・暗い室内 |
| `sleep_deep_sleep_no_person_001.png` | ベッド・月光・静寂感 |
| `sleep_midnight_calm_female_001.png` | 月明かりの室内・眠る前の静寂 |
| `sleep_ocean_night_no_person_001.png` | 夜の海・満月・波 |
| `sleep_forest_night_no_person_001.png` | 夜の森・星空・静寂 |

**画像仕様:**
- 非常に暗め・月光・星
- 雨・霧・波などの環境要素
- 刺激を与えない穏やかな構図
- 人物は眠った状態 or なし

---

### nature（自然・森・雨）

| ファイル名 | 画像の内容 |
|---------|---------|
| `nature_forest_rain_no_person_001.png` | 雨の森・霧・苔 |
| `nature_waterfall_no_person_001.png` | 滝・岩・水しぶき |
| `nature_japanese_garden_no_person_001.png` | 和風庭園・枯山水・竹 |
| `nature_mountain_morning_no_person_001.png` | 朝の山・雲海 |
| `nature_river_no_person_001.png` | 川・石・自然の流れ |

**画像仕様:**
- 自然な緑・青・グレーのトーン
- 霧・雨・水の質感を重視
- 人物なしを基本とする
- 日本的・和風の要素を活かす

---

### cafe（カフェ・ Lo-fi・コーヒー）

| ファイル名 | 画像の内容 |
|---------|---------|
| `cafe_cozy_cafe_male_001.png` | 窓辺でコーヒー・本・暖かい光 |
| `cafe_rainy_cafe_female_001.png` | 雨の窓越し・カフェ・女性 |
| `cafe_jazz_lounge_no_person_001.png` | バー・ジャズクラブ・夜の照明 |
| `cafe_bookstore_no_person_001.png` | 古書店・本・温かい照明 |
| `cafe_morning_coffee_no_person_001.png` | コーヒーカップ・朝の光・テーブル |

**画像仕様:**
- 暖色（アンバー・ゴールド・茶系）
- コーヒー・本・木材などのディテール
- ボケた背景・温かみのある光
- 商業施設が特定されない構図

---

### relax（リラックス・夕方・瞑想）

| ファイル名 | 画像の内容 |
|---------|---------|
| `relax_evening_chill_male_001.png` | 夕日の窓辺・男性・くつろぎ |
| `relax_meditation_female_001.png` | 瞑想・ヨガ・朝の光 |
| `relax_sunset_no_person_001.png` | 夕焼け・海・空 |
| `relax_reading_evening_female_001.png` | 夕方の読書・柔らかい光 |

**画像仕様:**
- 夕方のオレンジ・ゴールドのトーン
- 穏やか・余白のある構図
- 息を吐くような静けさ

---

## ChatGPT画像生成プロンプト テンプレート

### workout / boxercise / female

```
A powerful female boxer performing boxercise training in a professional
boxing gym. Dramatic cinematic side lighting with dark background and
spotlight effect. She is in a dynamic fighting stance, wearing boxing
gloves and workout gear. Sweat and intensity. Photorealistic, highly
detailed, 16:9 horizontal composition, dark moody atmosphere.
```

### study / deep focus / female

```
A woman studying intensely at a wooden desk late at night. Warm desk
lamp illuminating her face and books. Dark room with bokeh background.
She is focused and calm, surrounded by open books and a notebook.
Photorealistic, warm amber light, cinematic atmosphere, 16:9 ratio.
No face visible (back or side view preferred).
```

### sleep / rainy night / no person

```
A dark rainy night scene viewed through a window. Rain streaking down
the glass, soft city lights blurred in the background. Moody, dark,
cinematic atmosphere. Interior elements like a candle or dim lamp.
No people. Photorealistic, 16:9 ratio, dark blues and purples.
```

### nature / forest rain / no person

```
A misty forest during rain. Ancient trees with moss-covered rocks and
flowing stream. Ethereal fog drifting through the trees. Japanese-style
forest atmosphere. No people. Photorealistic, soft greens and grays,
16:9 horizontal composition, peaceful and serene.
```

### cafe / cozy cafe / male

```
A man sitting by a cafe window on a rainy day, holding a warm coffee
mug. Warm golden bokeh lights in background. Wooden table, book, cozy
atmosphere. Side or back view only (no clear face). Rainy window,
warm amber lighting, photorealistic, 16:9 ratio.
```

---

## サムネイル用仕様

サムネイルは `images/thumbnails/[カテゴリ]/` に保存。

| 項目 | 仕様 |
|------|------|
| サイズ | 1280×720px（最低）/ 1920×1080px（推奨） |
| 形式 | JPG（YouTube要件）または PNG→JPG変換 |
| テキスト | シリーズ名 + Vol.X のみ（重ねる場合） |
| 背景と文字 | 高コントラスト必須（白文字＋暗背景が基本） |

---

## フォルダ構成 早見表

```
assets/latte_bgm/
├── images/
│   ├── source/[カテゴリ]/     ← ChatGPTから受け取った元画像
│   ├── thumbnails/[カテゴリ]/ ← YouTube用サムネイル（JPG変換後）
│   └── backgrounds/[カテゴリ]/← 動画背景専用（トリミング・調整済み）
├── audio/
│   ├── source/                ← Sunoからダウンロードした音源
│   └── looped/                ← ループ済み音源（一時ファイル）
├── videos/
│   ├── drafts/                ← 生成直後の確認用
│   └── final/                 ← アップロード確定後
├── prompts/
│   ├── image_prompts/         ← ChatGPTへのプロンプト（.txt）
│   └── suno_prompts/          ← Sunoへのプロンプト（.txt）
└── metadata/
    ├── titles/                ← YouTubeタイトル（.txt）
    ├── descriptions/          ← YouTube説明文（.txt）
    └── upload_checklists/     ← アップロードチェックリスト（.md）
```
