# Latte BGM TODO

更新日: 2026-06-12（本日の作業終了時点）

## 2026-06-12 完了状況 — 初期5ジャンル新ロゴ統一【ほぼ完了】

| ジャンル | 新版ファイル | 状態 |
|---------|------------|------|
| Boxercise | `boxercise_30min_002.mp4` | ✅ 公開済み |
| Study Deep Focus | `study_deep_focus_30min_002.mp4` | ✅ 公開済み |
| Rain & Forest | `forest_relaxation_30min_002.mp4` | ✅ 公開済み |
| Calm Sleep | `sleep_rainy_night_30min_002.mp4` | ✅ 公開済み（※Content ID申し立てあり・下記参照） |
| Warm Cafe | `cafe_warm_30min_005.mp4` | ⚠️ アップロード作業中 or 公開済み確認待ち（**次回要確認**） |

- 5本すべて新ロゴ仕様（`latte_dog_icon_circle_v2.png` + LATTE BGM文字・Cafe 004基準配置）でレンダー・検証合格済み
- サムネイル5本・YouTubeメタデータ5本も作成済み（`videos/final/` 内）
- チャンネルアイコン（案B）・動画内右上ロゴ・サムネのブランド統一が成立
- **Cafe 005の公開が確認できた時点で、初期5ジャンルの新ロゴ統一は完全完了**

## 次回作業（優先順）
1. [ ] **Cafe 005 公開確認**: `cafe_warm_30min_005.mp4` がYouTubeで公開済みかチャンネルで確認する
2. [ ] **旧版動画の整理**: 新版公開済みジャンルの旧版（boxercise_30min_001、study_deep_focus_30min_001、forest_relaxation_30min_001、sleep_rainy_night_30min_001、cafe_warm_30min_004等）の扱いを決める（非公開化・再生リスト除外など。**削除はしない**）
3. [ ] **Sleep 003 作り直し**（下記セクション参照・Content ID対応）
4. [ ] **Latte BGM ヘッダー（バナー）調整**: 新アイコン（案B）に合わせたチャンネルバナーの調整

## Sleep 003 作り直し（Content ID対応・優先度高）
- 経緯: `sleep_rainy_night_30min_002` に Content ID 申し立てあり（2026-06-12確認）。
  - 使用コンテンツ: **Dusty Lullaby**
  - 該当箇所: **0:20〜2:13** および **19:32〜19:48**
  - 影響: **収益化のみ**（ブロック・ストライクではない）
  - 対応方針: 異議申し立てはしない。公開は継続。将来の収益化のため新音源で作り直す。
- **該当曲は `audio/source/sleep_rainy_night_001.mp3` と特定済み（2026-06-12）**。マスターは sleep(171s)→nature(212s)→study(164s) の約9分7秒サイクルのループ構成で、申し立て2箇所はどちらも sleep_rainy_night_001 再生区間に一致。nature/study の2曲は公開済みのForest/Study動画で申し立てが出ていないこととも整合。
- **`sleep_rainy_night_001.mp3` は今後一切再利用しないこと**（Sleep 003 のマスターからも除外）。
- [ ] Sleep用の完全新規音源を用意する（Suno等で新規生成・既存3曲は使わない）
- [ ] 新音源で30分マスターを再構築する（`make_sleep_audio_30min.py` 参照）
- [ ] `sleep_rainy_night_30min_003.mp4` として新ロゴ仕様（v2）でレンダーする（`make_sleep_rainy_night_30min_v2.py` の音源・出力名を差し替え）
- [ ] アップ後に Content ID 申し立てが出ないことを確認してから公開する
- [ ] 問題なければ 002 の扱い（非公開化など）を検討する

## その他の継続タスク
- [ ] 追加型で30分動画共通テンプレを作成する（成功済みスクリプトは壊さない）
- [ ] Relax / Morning など今後の新作も、新ロゴ（v2）方針で統一する

## 新アイコン・新ロゴ（2026-06-12 採用済み・完了）
- [x] 新チャンネルアイコン = **案B（ミュージックグロー版）** をYouTubeに反映済み（文字なし）
- [x] 動画内右上ロゴ実用版 `latte_dog_icon_circle_v2.png` 作成・可読性検証済み（案Bの円形透過512px版）
- [x] 「LATTE BGM」文字（`latte_brand_text.png`）と別レイヤー構成・Cafe 004基準配置を維持
- [x] 初期5ジャンルすべて新ロゴ版レンダー完了（v2スクリプト5本: `make_boxercise_30min_v2.py` / `make_study_focus_30min_v2.py` / `make_cafe_warm_30min_v2.py` / `make_forest_relaxation_30min_v2.py` / `make_sleep_rainy_night_30min_v2.py`）
- 採用ファイル: `brand/channel_icon_music_glow_1024.png`（マスター）/ `channel_icon_music_glow_800.png`（YouTube用）/ `latte_dog_icon_circle_v2.png`（動画右上ロゴ用）
- 旧 `latte_dog_icon_circle.png` は旧標準ロゴとして保持（旧版公開動画が使用）

## 保護方針
- 成功済みスクリプトと動画素材は直接壊さない（v2はすべて別スクリプトとして追加済み）
- 公開済み動画は YouTube 上で直接差し替えない・削除しない
- 旧動画はリメイク時に新ロゴ版へ順次置き換える
