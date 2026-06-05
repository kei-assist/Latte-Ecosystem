# Latte BGM Daily Batch Template v1

> 目的：毎日2本以上を最小作業で投稿する

---

## 1日の標準作業枠

| ブロック | 時間目安 | 内容 |
|---------|---------|------|
| A. 音源生成 | 15分 | Sunoで2曲生成・採用判定 |
| B. 動画化 | 10分 | スクリプト1コマンド実行（×2本） |
| C. メタデータ | 15分 | タイトル・説明文・タグをテンプレから複製（×2本） |
| D. アップロード | 10分 | YouTube投稿・サムネイル設定・プレイリスト追加（×2本） |
| E. SNS告知 | 5分 | X告知ツイート（×2本） |
| **合計** | **約55分** | **2本投稿完了** |

---

## Step A：Suno音源生成

1. プロンプトライブラリから本日ジャンルのプロンプトを選ぶ
   → [Latte_BGM_Suno_Prompt_Library_v1.md](./Latte_BGM_Suno_Prompt_Library_v1.md)
2. Sunoで生成（2〜3候補を生成し、最も完成度の高い1曲を採用）
3. MP3をダウンロードして `latte_music/audio/` に保存

```
命名規則: [Series Name] Vol.X.mp3
例: Morning Piano Vol.3.mp3
```

4. 採用判定チェック

- [ ] 音飛び・ノイズなし
- [ ] 1分以上のループ性あり
- [ ] ジャンルのトーンに合っている

---

## Step B：動画化（1コマンド）

```bash
cd ~/Desktop/latte_music

# 静止画BGM（Sleep / Study / Meditation）
python3 scripts/daily_upload.py "[音源ファイル名].mp3" [ジャンルID]

# 波形アニメーション（Workout / Cafe / Jazz）
python3 scripts/daily_upload.py "[音源ファイル名].mp3" [ジャンルID]
```

ジャンルID早見表:

| ID | ジャンル | 動画スタイル |
|----|---------|------------|
| 2 | Sleep | 静止画 |
| 3 | Study / Focus | 静止画 |
| 8 | Meditation | 静止画 |
| 9 | Sleep Vol.2 | 静止画 |
| 5 | Cafe / Lo-fi | 波形（穏） |
| 10 | Jazz | 波形（穏） |
| 1 | Workout | 波形 |

---

## Step C：メタデータ作成

テンプレートから複製して記入:
→ [Latte_BGM_Metadata_Template_v1.md](./Latte_BGM_Metadata_Template_v1.md)

```
作業手順:
1. テンプレートを開く
2. 該当ジャンルのブロックをコピー
3. [Series Name] / [Vol.X] / [URL] を埋める
4. 説明文のタイムスタンプ欄を確認（1時間尺なら 0:00 のみで可）
```

---

## Step D：YouTube投稿チェックリスト

1本あたり:

- [ ] MP4ファイル確認
- [ ] タイトル入力
- [ ] 説明文貼り付け
- [ ] タグ設定
- [ ] サムネイル設定（生成済みJPG）
- [ ] プレイリスト追加
- [ ] 公開設定（即時公開 or スケジュール）

**スケジュール投稿推奨時刻（英語圏向け）**

| 投稿番号 | 推奨時刻（JST） | 英語圏換算 |
|---------|--------------|-----------|
| 1本目 | 07:00 | 前日22:00 EST |
| 2本目 | 21:00 | 当日08:00 EST |

---

## Step E：X告知

テンプレートから複製:
→ [../templates/sns-post.md](./sns-post.md)

```
投稿例:
新着BGM🎵

Rainy Night Vol.3 — Sleep & Relax

雨の夜に、そっと流しておく音楽。

▶ [URL]

#LatteBGM #SleepMusic #作業用BGM
```

---

## 2本目以降の短縮フロー（慣れたら）

```
Suno生成 → audio/保存 → daily_upload.py実行 → メタデータ貼り付け → アップロード → X告知
```

1本目終了後、Step Aから繰り返すだけ。

---

## 月間投稿ペース管理

| 目標 | 1日 | 週 | 月 |
|-----|-----|----|----|
| 最低ライン | 1本 | 7本 | 30本 |
| 標準ライン | 2本 | 14本 | 60本 |
| 理想ライン | 3本 | 21本 | 90本 |
