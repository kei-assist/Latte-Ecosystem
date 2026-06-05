# Production Log Template v1

> 1本制作するたびにこのログを1ブロックコピーして記録する。
> ファイル名規則: `logs/[YYYY-MM]_production_log.md`

---

## 月次ログファイルの作り方

```
1. logs/ フォルダに [YYYY-MM]_production_log.md を作成
2. 月内の全投稿分ブロックをこのファイルに追記
3. 月末に Weekly_BGM_Review と合わせて振り返る
```

---

## 1本分ログブロック（コピー用）

```markdown
---

## [YYYY-MM-DD] | [Series Name Vol.X]

### 基本情報

| 項目 | 内容 |
|------|------|
| 制作日 | YYYY-MM-DD |
| シリーズ名 | [Series Name] |
| Vol番号 | Vol.[X] |
| ジャンル | [Sleep / Focus / Cafe / Nature / Meditation / Morning] |
| ジャンルID | [1〜10] |

### 音源

| 項目 | 内容 |
|------|------|
| Sunoプロンプト使用ID | [Sleep-A / Focus-B など] |
| 採用ファイル名 | [ファイル名.mp3] |
| 尺 | [例: 1:00:00] |
| 音質確認 | [ ] OK |

### 制作

| 項目 | 内容 |
|------|------|
| 動画スタイル | [静止画 / 波形] |
| スクリプトコマンド | `python3 scripts/daily_upload.py "[ファイル名.mp3]" [ID]` |
| 動画生成完了 | [ ] |
| サムネイル生成完了 | [ ] |

### YouTube

| 項目 | 内容 |
|------|------|
| タイトル | |
| 投稿日時 | YYYY-MM-DD HH:MM JST |
| YouTube URL | |
| プレイリスト追加 | [ ] |
| サムネイル設定 | [ ] |

### SNS告知

| プラットフォーム | 投稿済み | URL |
|--------------|---------|-----|
| X | [ ] | |
| Instagram | [ ] | — |

### メモ

（特記事項・改善点・次回への引き継ぎ）

```

---

## 記入例

```markdown
---

## 2026-06-10 | Morning Piano Vol.3

### 基本情報

| 項目 | 内容 |
|------|------|
| 制作日 | 2026-06-10 |
| シリーズ名 | Morning Piano |
| Vol番号 | Vol.3 |
| ジャンル | Morning |
| ジャンルID | 3（Study兼用） |

### 音源

| 項目 | 内容 |
|------|------|
| Sunoプロンプト使用ID | Morning-A |
| 採用ファイル名 | Morning Piano Vol.3.mp3 |
| 尺 | 1:00:00 |
| 音質確認 | [x] OK |

### 制作

| 項目 | 内容 |
|------|------|
| 動画スタイル | 静止画 |
| スクリプトコマンド | `python3 scripts/daily_upload.py "Morning Piano Vol.3.mp3" 3` |
| 動画生成完了 | [x] |
| サムネイル生成完了 | [x] |

### YouTube

| 項目 | 内容 |
|------|------|
| タイトル | Morning Piano Vol.3 \| Morning Piano BGM & Gentle Wake-Up Music \| Latte BGM |
| 投稿日時 | 2026-06-10 07:00 JST |
| YouTube URL | https://www.youtube.com/watch?v=XXXXXXXXX |
| プレイリスト追加 | [x] |
| サムネイル設定 | [x] |

### SNS告知

| プラットフォーム | 投稿済み | URL |
|--------------|---------|-----|
| X | [x] | https://x.com/... |
| Instagram | [ ] | — |

### メモ

Sunoのモデルが更新されて音質が向上。Morning-Aプロンプトは今後も継続使用。
```

---

## 月間集計欄（月末に記入）

```markdown
## [YYYY年MM月] 月間集計

| 指標 | 数値 |
|------|------|
| 総投稿本数 | X本 |
| 累計投稿本数 | X本 |
| ジャンル内訳 | Sleep:X / Focus:X / Cafe:X / Nature:X / Meditation:X / Morning:X |
| 最多投稿ジャンル | |
| 月間再生数（目安） | |
| 新規登録者数（目安） | |
| 来月の優先ジャンル | |
```
