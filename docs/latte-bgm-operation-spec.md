# Latte BGM 運営仕様

## 基本方針

- **ターゲット**: 英語圏（特に米国）
- **フォーマット**: 長尺動画（1時間〜、将来的に2〜3時間へ拡張）
- **投稿モデル**: 毎日投稿・高速改善
- **音源ルール**: Sunoで毎日新規生成。既存音源の流用は原則なし
- **品質基準**: 30点で公開し、実データから改善する

## 優先ジャンル

| 優先度 | ジャンル |
|--------|---------|
| 1 | Sleep |
| 2 | Focus |
| 3 | Relax |
| 4 | Cafe |
| 5 | Nature |
| 6 | Meditation |

## 将来拡張候補（現時点では着手しない）

- Gym Motivation / Workout BGM
- City Pop Instrumental
- Japanese Nostalgia / Retro Japan
- Baseball系 / Stadium系 / RIZIN系

## ジャンルID（制作スクリプト対応）

| ID | ジャンル | 動画スタイル |
|----|---------|------------|
| 1 | Workout / Gym | Waveform |
| 2 | Sleep | Static Image |
| 3 | Study / Focus | Static Image |
| 4 | Sports | Waveform |
| 5 | Cafe / Lo-fi | Calm Waveform |
| 6 | MMA / Fighting | Waveform |
| 7 | Workout2 / Iron Will | Waveform |
| 8 | Meditation | Static Image |
| 9 | Sleep Vol.2 | Static Image |
| 10 | Jazz | Calm Waveform |

## 公開済みシリーズ

- Rainy Night Vol.1 / Vol.2
- Deep Focus Vol.2 / Vol.3 / Vol.4
- Deep Sleep Vol.1
- Japanese Garden Vol.1 / Vol.2
- Cozy Cafe Vol.1 / Vol.2
- Forest Calm Vol.2 / Vol.3
- Reading Room Vol.1 / Vol.2
- Morning Piano Vol.1 / Vol.2

**公開済み合計: 15本+**

## 制作フロー

```
Suno新曲生成
    ↓
音源確認・audio/に保存
    ↓
サムネイル作成
    ↓
長尺動画化（1時間MP4）
    ↓
YouTubeアップロード
    ↓
サムネイル設定・プレイリスト追加
```

## 次回制作候補

1. Morning Piano Vol.3
2. Deep Sleep Vol.2
3. Meditation Vol.1
4. Rainy Night Vol.3
5. Reading Room Vol.3

## 成長戦略

- ベンチマーク分析
- タイトル・サムネイルのA/Bテスト
- プレイリスト・終了画面によるチャンネル回遊設計
- ジャンルローテーション管理
- Codexによる自動化推進
