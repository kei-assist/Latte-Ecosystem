# Latte BGM 自動化ロードマップ

## 現在の自動化状況

Pythonスクリプト (`latte_music/scripts/`) による以下の自動化が完成:

| スクリプト | 機能 |
|-----------|------|
| `daily_upload.py` | メインパイプライン（1コマンドで動画化〜投稿） |
| `make_thumbnail.py` | ジャンル別サムネイル自動生成 |
| `make_static_mp4.py` | 静止画BGM動画生成 |
| `make_waveform_mp4.py` | 波形アニメーション動画生成 |
| `upload_to_youtube.py` | YouTube Data API v3アップロード |
| `merge_mp3.py` | 複数MP3を60分音源に結合 |

## Phase 1: 現状（完成済み）

- [x] Suno MP3 → 1時間MP4変換
- [x] ジャンル別サムネイル自動生成
- [x] YouTube Data APIアップロード
- [x] タイトル・説明文テンプレート自動適用
- [x] 秘密情報のGitHub除外設定

## Phase 2: 近期改善（3ヶ月以内）

- [ ] サムネイルA/Bテスト管理スクリプト
- [ ] 英語タイトル・説明文の品質改善テンプレート
- [ ] プレイリスト自動追加
- [ ] 終了画面の自動設定
- [ ] 投稿後の実績自動記録（YouTube Analytics取得）

## Phase 3: 拡張（6ヶ月以内）

- [ ] 1時間 → 2〜3時間フォーマット対応
- [ ] ジャンルローテーション自動判定
- [ ] KPIダッシュボード自動生成
- [ ] SNS連動（X自動投稿）

## Phase 4: 将来構想

- [ ] Suno生成のバッチ化（候補複数生成→採用判定）
- [ ] 視聴データフィードバックによるジャンル自動最適化
- [ ] Latte CH Shorts切り出し自動化との統合

## 技術スタック

- Python 3.x
- MoviePy（動画生成）
- Pillow（サムネイル生成）
- NumPy（波形アニメーション）
- YouTube Data API v3
- OAuth 2.0（Google認証）
