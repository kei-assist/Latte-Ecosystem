# Latte BGM Visual Asset Guide v2

参照元: `Kei_Life_OS_v2.md`
更新日: 2026-06-06

---

## 命名規則

### 画像ファイル

```
カテゴリ_テーマ_人物性別_番号.png

[カテゴリ] : workout / sleep / study / nature / cafe / relax
[テーマ]   : スネークケース
[人物性別] : female / male / no_person（人物なし）
[番号]     : 3桁ゼロ埋め（001〜）
```

### 動画ファイル

```
カテゴリ_テーマ_長さ_番号.mp4

例: workout_boxercise_60min_001.mp4
    sleep_rainy_night_60min_001.mp4
```

---

## Workout ビジュアルルール

### 大原則

- **黒×金** を基本カラーとする（高級感・プロ感）
- 人物は画面の中心に大きく配置する
- 動画を見た瞬間（1秒以内）に「何のBGMか」が分かること
- **subtype ごとに絵柄を必ず変える**（同じ筋肉画像を使い回さない）
- チープな図形・棒人間・ストックフォト感のある素材は禁止
- 高級ジムのような洗練された雰囲気を維持する

### subtype 別ルール

#### 1. beast_mode（重い筋トレ・男性）

```
人物:   男性アスリート（上半身・筋肉）
道具:   ダンベル / バーベル
背景:   高級ジム・黒×金の照明・ガレージジム
色調:   ダーク・強いコントラスト・ゴールドのハイライト
雰囲気: 力強さ・鋼の意志・重量を扱う緊張感
禁止:   かわいい系・明るいパステル・カジュアルな服装
```

**ChatGPT プロンプト例:**
```
A powerful male athlete lifting heavy dumbbells in a premium dark gym.
Dramatic golden spotlight from above. Intense focused expression.
Dark background with subtle gold reflections. Cinematic, photorealistic.
16:9, no text, high contrast.
```

#### 2. boxercise（ボクシング・女性）

```
人物:   女性アスリート（ボクシングポーズ）
道具:   ボクシンググローブ・サンドバッグ
背景:   ボクシングジム・ロープ・スポットライト
色調:   黒×金・強いスポット照明・汗の質感
雰囲気: HIIT・脂肪燃焼・格闘技フィットネスの迫力
禁止:   かわいい系・柔らかい光・実戦格闘技感が強すぎる
```

**ChatGPT プロンプト例:**
```
A fierce female athlete in a boxing stance, wearing gold boxing gloves,
training in a professional boxing gym. Dramatic side lighting from the
right. Dark moody atmosphere. Sweat, power, focus. Cinematic, 16:9.
No text, photorealistic, high quality.
```

#### 3. running（ランニング・女性）

```
人物:   女性ランナー（走行中・疾走感）
背景:   屋外・朝焼け・公園・橋・都市
色調:   明るめ・オレンジ〜ゴールドの朝焼け
雰囲気: 疾走感・朝の爽快感・cardio boost
禁止:   暗い・室内・ジム内
```

**ChatGPT プロンプト例:**
```
A female runner sprinting on an outdoor path at sunrise. Golden morning
light from behind. Motion blur on legs, hair flowing. Bright, energetic,
cinematic. Orange and gold sky. 16:9, photorealistic, no text.
```

#### 4. hiit_circuit（HIIT・サーキット）

```
人物:   女性（複数種目感のあるポーズ）
背景:   明るいジム全体・タイマー的な強い光
色調:   明るめ・高コントラスト・白〜銀
雰囲気: 高強度・複数種目・短時間で燃やす
禁止:   単一種目のみの画像・暗すぎる・重すぎる
```

**ChatGPT プロンプト例:**
```
A fit female athlete in the middle of a HIIT circuit training session.
Bright professional gym lighting. Dynamic action pose. Energy, power,
movement. Cinematic, 16:9, no text, photorealistic.
```

#### 5. gym_motivation（ジム前の集中）

```
人物:   男性（ヘッドホン・ロッカー前・鏡前）
背景:   ロッカールーム・ジムエントランス・集中している様子
色調:   ダーク・落ち着いたコントラスト
雰囲気: これから始める緊張感・静かな強さ・集中
禁止:   派手すぎる・激しい動き・大声で叫ぶ表情
```

**ChatGPT プロンプト例:**
```
A focused male athlete in a gym locker room, wearing headphones, looking
in the mirror before training. Calm intensity, pre-workout focus.
Dark moody lighting. Cinematic, 16:9, photorealistic, no text.
```

---

## Sleep ビジュアルルール

### 大原則

- **低刺激・眠りを邪魔しない** ことが最優先
- 夜・雨・月明かり・窓・ベッド・ソファ を基本シーンとする
- 動きは**ゆっくり** — ズームは zoom_end 1.04〜1.08 の範囲のみ
- 明るすぎない（眠れなくなる）
- 目が疲れない（点滅・急な明暗変化は禁止）
- やわらかいアニメーション感を重視する（*夏風ペダル*のような空気感）
- **抽象図形だけ・テキストだけの背景は禁止**
- 何のBGMか（睡眠用）が一瞬で分かること

### subtype 別ルール

#### 1. sleep_soft（穏やかな睡眠）

```
シーン: 月明かりの窓・ベッド・カーテン・静かな室内
色調:   深い紺・濃いグレー・月光のブルー
雰囲気: 静寂・安心・やわらかい光
禁止:   明るい・カラフル・動きのある人物
```

**ChatGPT プロンプト例:**
```
A quiet bedroom at night lit only by moonlight through curtains.
Soft blue moonlight on white bedding. Peaceful, serene, dreamy.
No people. Dark blues and whites. Cinematic, 16:9, photorealistic.
```

#### 2. sleep_rainy_night（雨の夜）

```
シーン: 雨が降る夜の窓・室内から外を見る・水滴
色調:   暗い青×暖色（窓の外の街灯・ランプ）
雰囲気: 雨音・温かい室内・やすらぎ・落ち着いた夜
禁止:   強い雨（嵐）・稲妻・強い光の点滅
```

**ChatGPT プロンプト例:**
```
A rainy night seen through a window. Rain drops on glass, blurred warm
street lights outside. Cozy interior with soft lamp light inside.
Dark blues and warm amber. No people. Cinematic, 16:9, photorealistic.
```

#### 3. sleep_deep_night（深夜・寝落ち用）

```
シーン: 星空・月・満月・深夜の海・宇宙
色調:   ほぼ黒・非常に暗いネイビー
雰囲気: 完全な静寂・吸い込まれる暗闇・深い眠り
禁止:   人物・明るい色・音楽や音をイメージさせる要素
```

**ChatGPT プロンプト例:**
```
A deep dark night sky filled with stars and the milky way over a calm
ocean. Almost completely dark. Ultra minimal, peaceful, infinite silence.
No people. Dark blue-black. Cinematic, 16:9, photorealistic.
```

---

## 全カテゴリ共通ルール

### 解像度・形式

| 項目 | 推奨 | 最低限 |
|------|------|-------|
| 解像度 | 3840×2160（4K） | 1920×1080 |
| 形式 | PNG | PNG |
| ファイルサイズ | 5MB以下 | — |

> **推奨理由**: スクリプトが動画生成時に画像を zoom_end 倍にアップスケールします。
> 4K 素材があれば 1.3x ズームでも品質低下なし。1920×1080 でも許容範囲です。

### サムネイル仕様

| 項目 | 仕様 |
|------|------|
| サイズ | 1280×720（最低）/ 1920×1080（推奨） |
| 形式 | JPG（YouTube 要件） |
| テキスト | シリーズ名 + Vol.X のみ（入れる場合） |
| 文字色 | 白（暗背景に高コントラスト） |
| 保存先 | `assets/latte_bgm/images/thumbnails/[カテゴリ]/` |

### 禁止事項（全カテゴリ）

- 他者の顔が特定できる写真（著作権・肖像権）
- 撮影禁止場所の写真
- 職場・会社が特定できる写真
- 住所・生活拠点が分かる写真
- 実在のブランドロゴ・商品が映る写真
- AI 生成の不自然なアーティファクト（指が増えているなど）

---

## フォルダ構成 早見表

```
assets/latte_bgm/images/
├── source/
│   ├── workout/   ← ChatGPT から受け取った元画像
│   ├── sleep/
│   ├── study/
│   ├── nature/
│   ├── cafe/
│   └── relax/
├── thumbnails/
│   ├── workout/   ← YouTube サムネイル用（JPG 変換後）
│   └── sleep/ ...
└── backgrounds/
    └── （動画背景専用・未使用の場合は空でよい）
```
