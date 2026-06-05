# GitHub管理資料

## リポジトリ一覧

| リポジトリ | 用途 | 公開設定 | URL |
|-----------|------|---------|-----|
| Latte-Ecosystem | 運営本部・仕様管理 | Public | https://github.com/kei-assist/Latte-Ecosystem |
| bruno-sales-report | ポートフォリオ（売上日報） | Public | https://github.com/kei-assist/bruno-sales-report |

---

## Latte-Ecosystem リポジトリ管理ルール

### コミット方針

- ドキュメント追加・更新は都度コミット
- 大きな方針変更は変更内容を commit message に明記
- メディアファイル（mp4/wav/png/jpg等）は絶対にコミットしない

### ブランチ運用

- `main`: 常に運用中の仕様を反映
- 大規模な構成変更時はブランチを切ってから main にマージ

### 除外ファイル（.gitignore管理）

- 動画ファイル: *.mp4
- 音源ファイル: *.mp3 / *.wav / *.aac / *.flac / *.m4a
- 画像ファイル: *.png / *.jpg / *.jpeg / *.gif / *.webp
- 認証情報: *.json / *.pickle / .env
- レンダーファイル・生成物全般

---

## ディレクトリ設計方針

| ディレクトリ | 用途 |
|------------|------|
| `/docs` | 運営仕様書・KPI・SNS計画・GitHub管理資料 |
| `/workflows` | 各チャンネル・SNSの作業手順フロー |
| `/templates` | YouTube説明文・SNS投稿・スクリプトのテンプレート |
| `/logs` | 週次・月次レビュー記録 |
| `/pipelines` | 自動化ロードマップ・コンテンツカレンダー |

---

## 今後追加予定のリポジトリ候補

| リポジトリ名（案） | 用途 |
|----------------|------|
| latte-bgm-scripts | BGM制作・YouTube自動投稿Pythonスクリプト |
| latte-ch-scripts | Latte CH制作自動化スクリプト |
| kei-assist-portfolio | Kei Assistポートフォリオ集約 |

---

## アカウント情報

- GitHub: [kei-assist](https://github.com/kei-assist)
- 管理者: 藤田啓一
