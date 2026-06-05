# Latte BGM Playlist Strategy v1

> YouTube プレイリストによるチャンネル回遊設計。
> 1本の視聴を2本・3本へつなぐ仕組みを作る。

---

## なぜプレイリストが重要か

| 効果 | 説明 |
|------|------|
| 視聴時間の延長 | プレイリスト再生は自動送りで視聴時間が伸びる |
| チャンネル回遊 | 1本見た人が同ジャンルの別動画に移る |
| 検索流入 | プレイリスト自体がYouTube検索に表示される |
| アルゴリズム強化 | 視聴時間が長いほどYouTubeが推薦しやすくなる |

---

## プレイリスト一覧

### メインプレイリスト（ジャンル別）

| プレイリスト名 | 対象動画 | 目標本数 |
|-------------|---------|---------|
| Sleep & Relax BGM \| Latte BGM | Sleep / Rainy Night / Deep Sleep | 20本+ |
| Deep Focus & Study BGM \| Latte BGM | Focus / Study / Coding / Work | 20本+ |
| Cafe & Lo-Fi Chill \| Latte BGM | Cafe / Lo-fi / Jazz | 15本+ |
| Nature & Meditation BGM \| Latte BGM | Nature / Forest / Japanese Garden / Meditation | 15本+ |
| Morning & Relax BGM \| Latte BGM | Morning Piano / Sunrise / Reading Room | 10本+ |

### シリーズプレイリスト（シリーズ別）

| プレイリスト名 | 対象動画 |
|-------------|---------|
| Rainy Night Series \| Latte BGM | Rainy Night Vol.1〜 |
| Deep Focus Series \| Latte BGM | Deep Focus Vol.1〜 |
| Forest Calm Series \| Latte BGM | Forest Calm Vol.1〜 |
| Morning Piano Series \| Latte BGM | Morning Piano Vol.1〜 |
| Japanese Garden Series \| Latte BGM | Japanese Garden Vol.1〜 |
| Cozy Cafe Series \| Latte BGM | Cozy Cafe Vol.1〜 |
| Reading Room Series \| Latte BGM | Reading Room Vol.1〜 |

### まとめプレイリスト（ユースケース別）

| プレイリスト名 | 用途 |
|-------------|------|
| Best of Latte BGM | 全ジャンルのベスト動画 |
| 1-Hour BGM for Sleep \| Latte BGM | 就寝前に通して聴く |
| 8-Hour Study Music \| Latte BGM | 長時間学習向け連続再生 |
| Work From Home BGM \| Latte BGM | テレワーク向け |

---

## 新規動画投稿時のプレイリスト追加ルール

```
投稿直後に必ず以下の2つに追加:
1. 該当ジャンルのメインプレイリスト
2. 該当シリーズのシリーズプレイリスト（なければ作成）
```

### プレイリスト内の並び順

- **シリーズプレイリスト**: Vol.1 → Vol.2 → Vol.3（昇順）
- **メインプレイリスト**: 新しい順（視聴者が最新作から入りやすい）

---

## 終了画面（エンドスクリーン）設計

投稿動画の終了20秒前に表示する要素:

| 要素 | 内容 |
|------|------|
| 動画カード1 | 同シリーズの前作（例: Vol.2 → Vol.1） |
| 動画カード2 | 同ジャンルの別シリーズ（例: Rainy Night → Deep Sleep） |
| チャンネル登録ボタン | 必ず設置 |

### 回遊パターン設計（主要シリーズ）

```
Rainy Night Vol.3
    → 終了画面: Rainy Night Vol.2 / Deep Sleep Vol.1
    → プレイリスト: Sleep & Relax BGM

Deep Focus Vol.5
    → 終了画面: Deep Focus Vol.4 / Study Session Vol.1
    → プレイリスト: Deep Focus & Study BGM

Cozy Cafe Vol.3
    → 終了画面: Cozy Cafe Vol.2 / Jazz Lounge Vol.1
    → プレイリスト: Cafe & Lo-Fi Chill
```

---

## プレイリスト説明文テンプレート

```
[Playlist Name] | Latte BGM

[1〜2文のプレイリスト説明。用途・ジャンルを英語で]

Perfect for [use case 1], [use case 2], and [use case 3].
No ads, no interruptions — just [genre] music for [benefit].

🔔 Subscribe for daily BGM uploads:
https://www.youtube.com/@LatteBGM
```

### 記入例（Sleep）

```
Sleep & Relax BGM | Latte BGM

A curated collection of the best sleep and relaxation music from Latte BGM.
Soft piano, ambient soundscapes, and gentle melodies to help you unwind.

Perfect for bedtime, napping, or simply letting go of stress.
No ads, no interruptions — just peaceful music for deep rest.

🔔 Subscribe for daily BGM uploads:
https://www.youtube.com/@LatteBGM
```

---

## プレイリスト成長管理

| プレイリスト | 現在本数 | 目標本数 | 進捗 |
|------------|---------|---------|------|
| Sleep & Relax | | 20本 | |
| Deep Focus & Study | | 20本 | |
| Cafe & Lo-Fi | | 15本 | |
| Nature & Meditation | | 15本 | |
| Morning & Relax | | 10本 | |

*月次レビュー時に本数を記入して管理する*
