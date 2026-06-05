# Latte BGM 制作・投稿ワークフロー

## 1本制作の標準フロー

```
Step 1: Suno で新曲生成
    ↓
Step 2: 音源確認・採用判定
    ↓
Step 3: audio/ に保存
    ↓
Step 4: ジャンル決定（ジャンルID 1〜10）
    ↓
Step 5: サムネイル生成
        make_thumbnail.py 実行
    ↓
Step 6: 長尺動画化（1時間MP4）
        make_static_mp4.py または make_waveform_mp4.py
    ↓
Step 7: YouTubeメタデータ作成
        タイトル / 説明文 / タグ
    ↓
Step 8: YouTube アップロード
        upload_to_youtube.py または手動
    ↓
Step 9: サムネイル設定
    ↓
Step 10: プレイリスト追加
    ↓
Step 11: X / SNS 告知
```

---

## Suno プロンプト作成ルール

- 英語で記述
- ジャンルキーワードを明示（sleep / focus / relax / cafe / nature / meditation）
- テンポ・楽器・雰囲気を指定
- 長尺向けのループ性を意識した指示を入れる

---

## YouTube メタデータルール

### タイトルフォーマット

```
[Series Name] Vol.X | [Genre] BGM | Latte BGM
例: Rainy Night Vol.2 | Sleep & Relax BGM | Latte BGM
```

### 説明文

テンプレート: [/templates/youtube-description.md](../templates/youtube-description.md)

### タグ

ジャンルキーワード + latte bgm + study music / sleep music / relax music 等

---

## 制作ドキュメント管理（latte_music/docs/）

各作品ごとにサブフォルダを作成:

```
docs/
└── [series-name-vol-x]/
    ├── production_plan.md
    ├── suno_prompt.md
    ├── thumbnail_prompt.md
    ├── youtube_metadata.md
    ├── youtube_description.txt
    └── upload_ready_check.md
```

---

## upload_ready_check 確認項目

- [ ] 音源ファイル確認済み
- [ ] 1時間MP4生成済み
- [ ] サムネイル生成済み
- [ ] タイトル確認済み
- [ ] 説明文作成済み
- [ ] タグ設定済み
- [ ] アップロード完了
- [ ] サムネイル設定済み
- [ ] プレイリスト追加済み
- [ ] SNS告知済み
