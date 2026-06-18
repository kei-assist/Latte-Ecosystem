# GitHub / フォルダ管理 引き継ぎ（詳細）

最終確認日: 2026-06-18 ／ 正本: `latte-ecosystem/docs/github-management.md`

---

## 1. GitHubリポジトリ一覧
| リポジトリ | ローカル | remote | 用途 | 公開 |
|-----------|---------|--------|------|------|
| Latte-Ecosystem | `/Users/khhr/Desktop/latte-ecosystem/` | `https://github.com/kei-assist/Latte-Ecosystem.git` | 運営本部・仕様/自動化/KPI/SNS管理 | Public |
| bruno-sales-report | `/Users/khhr/Desktop/bruno/` | `https://github.com/koumelatte/bruno-sales-report-.git` | ポートフォリオ（売上日報・GitHub Pages） | Public |
| latte_music | `/Users/khhr/Desktop/latte_music/` | （ローカル.gitのみ・remote未設定） | 1時間BGM量産ワークスペース | ローカル |
| latte_ch | `/Users/khhr/Desktop/latte_ch/` | （gitなし） | Latte CH制作フォルダ | ローカル |

- GitHubアカウント: [kei-assist](https://github.com/kei-assist)（Latte-Ecosystem）、koumelatte（bruno）。管理者: 藤田啓一。

## 2. コミット / 除外ルール（厳守）
- ドキュメント追加・更新は都度コミット。大きな方針変更はcommit messageに明記。
- **メディア・認証情報は絶対にコミットしない**（.gitignore管理）:
  - 動画 `*.mp4` / 音源 `*.mp3 *.wav *.aac *.flac *.m4a`
  - 画像 `*.png *.jpg *.jpeg *.gif *.webp`
  - 認証 `*.json *.pickle .env`
  - レンダーファイル・生成物全般
- ブランチ: `main` = 運用中仕様。大規模変更時はブランチを切ってmainへマージ。

## 3. latte-ecosystem ディレクトリ設計
| ディレクトリ | 用途 |
|------------|------|
| `docs/` | 運営仕様書・KPI・SNS計画・GitHub管理・各種ロードマップ |
| `workflows/` | チャンネル/SNSの作業手順フロー |
| `templates/` | YouTube説明文・SNS投稿・スクリプト・メタデータ・Sunoプロンプトのテンプレ |
| `logs/` | 週次/月次レビュー記録 |
| `pipelines/` | 自動化ロードマップ・コンテンツカレンダー・各ジャンル30Series |
| `scripts/latte_bgm/` | BGM制作Pythonスクリプト |
| `assets/latte_bgm/` | images/brand・videos/final(メタ)・thumbnails・metadata・youtube_package・prompts |

## 4. フォルダ整理ルール（PC整理）
- `_整理_YYYY-MM-DD` フォルダを作り、種別（書類/画像/動画/音声/表計算/その他）で**集約・移動のみ**。
- 成果物は据え置き。**削除しない**。
- 既存: `_整理_2026-05-31`（書類/その他/画像/動画/音声/表計算）、`_整理_2026-06-04`（画像）、`_整理_2026-06-10`（その他/画像/音声）。

## 5. 触ってよい / 確認が必要 / 触らない
- **触ってよい**: 各 `docs/` `scripts/` のmd・スクリプト追加/更新（コミット可）。
- **触る前に確認**: `assets/` `video/` `audio/` `thumbnails/`（完成物・認証情報）、Desktop直下の各種mp4/png/jpg。
- **削除・上書きしない**: 公開済み動画、正式版アセット、旧版/不採用ファイル（保持）、認証情報（`client_secret.json` / `*_token.pickle`）。

## 6. 古いファイル・不採用ファイルの扱い
- すべて**保持**。削除も上書きもしない。
- 正式版を不採用へ格下げしない。不採用版を正式版へ格上げしない。
- 旧版BGM動画はYouTube側で非公開化を**検討**するのみ（ローカル保全）。

## 7. Desktop直下の主なフォルダ（誤操作防止のための地図）
- Latte系: `latte-ecosystem/` `latte_music/` `latte_ch/` `latte_images/` `latte_x_header_renewal/` `Latte_BGM_*` `LatteBGM_*` `LatteCH_*`
- 副業/ポートフォリオ: `ポートフィリオ/` `fitness-tracker-gas/` `bruno/` `提案文/` `要望書/` `書類/`
- その他: `Instagram/` `JR東日本/` `apass/` `Python/` `写真/` `bliss_eyecatch/`
- 整理用: `_整理_2026-05-31/` `_整理_2026-06-04/` `_整理_2026-06-10/`

## 8. Codexで最初に開くべきフォルダ
1. `/Users/khhr/Desktop/latte-ecosystem/`（特に `README.md` / `CURRENT_STATUS.md` / `docs/`）
2. `/Users/khhr/Desktop/latte_music/`（`CURRENT_STATUS.md` / `docs/`）
3. `/Users/khhr/Desktop/latte_ch/`（`LATTE_MASTER_CONTEXT.md` / `CURRENT_STATUS.md` / `docs/brand_guide.md`）

## 9. 未完了タスク
- 【中】旧版BGM動画の整理方針決定（YouTube非公開化検討・ローカル削除なし）。
- 【低】追加リポジトリ候補の検討: `latte-bgm-scripts` / `latte-ch-scripts` / `kei-assist-portfolio`。
- 【低】`latte_music` のGitHub remote化を検討するか（現状ローカルのみ）。

## 10. Codexへの注意点
- フォルダ構成・リポジトリ構成を**勝手に大幅変更しない**。
- 削除・移動・上書きは**必ず確認してから**。
- メディア/認証情報をコミットしない。
- 不明点は推測せず報告。
