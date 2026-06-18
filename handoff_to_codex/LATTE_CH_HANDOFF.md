# LATTE CH 引き継ぎ（詳細）

最終確認日: 2026-06-18 ／ 正本: `latte_ch/LATTE_MASTER_CONTEXT.md` ＋ `latte_ch/docs/brand_guide.md`

---

## 1. チャンネル方針
- **軸コピー: 「仕事も、お金も、人生も。少しラクに整える。」**（別表現: 「少しラクに生きる、大人の整え方。」）
- 日本語圏向けの**語り系・実用チャンネル**。癒し系BGM動画ではない／BGMの映像版でもない。
- 再生数を追わず、**信頼構築メディア**として運営 → Kei Assist / AI活用 / 自動化 / 副業案件への導線。
- ベンチマーク = サラタメ型（リベシティ キラさん戦略参考）。視聴維持率・シリーズ回遊・SNS展開重視。
- テーマ比率: **お金40% / 習慣40% / 暮らし20%**。
  - お金: 新NISA・家計管理・固定費削減・貯金・節税・保険・年金・ふるさと納税
  - 習慣: 疲れない働き方・時間管理・朝/健康習慣・副業前に整えること
  - 暮らし: 整理整頓・生活導線・暮らしを整える考え方
- AIや副業はメインにしない（必要時のみ「整える道具」として扱う）。

## 2. ブランドカラー / アイデンティティ
- **スカイブルー系（明るめの青 #59CBE8基調）＋白文字＋黄色アクセント**。
- BGM(ネイビー) と CH(スカイブルー) は**同じ犬キャラの兄弟ブランド・色で差別化**。
- 固定軸: ラテキャラ・VOICEVOX四国めたん・整える世界観・青系統一感。背景/レイアウトはテーマで変えてよい。

## 3. サムネ方針
- アニメ調ラテキャラを**必ず**サムネ・動画内に配置。
- サムネに `Latte ch` 表記を入れる。**EP番号は表示しない**。
- 禁止: 白背景だけ / 写真だけ（Unsplash等）/ ミニマルだけ / ラテ不在。
- タイトル文字は大きく・実用的・具体的に。暗い夜っぽさは避ける。

## 4. アイコン / ヘッダー方針（★最新・YouTube反映待ち）
- **アイコン（最終確定）**: `latte_ch_icon_face_final.png`（1024）/ `latte_ch_icon_face_final_800.png`（アップ用）。
  - 場所: `/Users/khhr/Desktop/latte_music/assets/`。
  - 仕様: 服・文字なしの顔だけ版。Latte BGMアイコン(`channel_icon_music_glow_1024.png`)を直接編集して制作（再生成なし）。ヘッドフォン/音符除去・背景ネイビー→スカイブルー(#59CBE8)・外周うすい水色リング・耳の自然さ改善。
  - 非採用（保持のみ）: 襟あり版 `latte_ch_icon_final.png`、`*_faceonly.png`、`*_genver_old.png`、v2(LATTEユニフォーム)、v1。すべて削除しない。
- **ヘッダー（正式候補）**: `latte_ch_youtube_banner_final_v2.png`（2560x1440）。
  - 場所: `/Users/khhr/Desktop/latte_music/assets/`。
  - 白背景＋スカイブルーの角ばりカレッジ体「LATTE CH」＋うっすら銀フレーム。文字幅1018へ縮小し安全領域に厳密収納（実機Studioで切れない確認済み）。FIGHTERS公式は非コピー。
  - 確認用: `latte_ch_youtube_banner_final_v2_safearea_preview.png`。
  - 旧版(final/v6/v5/v4/v3/v1) は保持・上書きなし。
- **反映手順**: YouTube Studio（Latte ch / @Lattech-x7o）→ カスタマイズ → アイコン=`_800.png`、バナー=`final_v2.png` を**ユーザー手動アップ**。**未実施**。

## 5. 企画 / 制作方針
- 標準構成: ①今日の悩み ②なぜ整わないのか ③整えるポイント3つ ④今日の1アクション ⑤ラテから一言。
- 話し方: 共感 → 問い → 整えるポイント → 今日の1アクション。
- トーン: 実用寄り・断定しすぎない・共感ベース・具体化・暗くしすぎない・自己啓発に寄せすぎない。
- **NGワード**: 稼げる / 絶対 / 誰でも簡単 / 最強 / 勝つ / 頑張れ / 成功者マウント。
- **NGトーン**: 病み系 / 過激系 / 煽り系 / 恐怖訴求 / 上から目線。
- タイトル: 静かに気になる・考えたくなる系（例「情報を集めるほど動けなくなる理由」「朝に増やさないもの」）。煽り/自己啓発テンプレは避ける。
- 長さ: Aパターン3〜4分 / Bパターン2分前後 / Shorts 60秒以内。週1本（無理なく継続優先）。

## 6. 動画生成ルール（VOICEVOX / アニメ）
- ナレーション = **VOICEVOX 四国めたん**（`latte_ch/narration/latte_ch_narration_*.wav`）。
- 字幕同期 = タイミングJSON（`latte_ch/scripts/latte_ch_timing_*.json` / `ep*_voice_segments.json`）。
- **静止画のみで完結させない**。軽い動きを必ず入れる（ラテの上下/左右移動・軽いズーム・背景パン・テキストフェード）。
- 既存BGM音源の流用は禁止。

## 7. 既存動画 / 進捗
- **EP01〜EP13 公開済み**（`latte_ch/video/latte_ch_ep**_final.mp4`）。
- 最新: **EP13「夜に抱えすぎない話」** https://www.youtube.com/watch?v=B8cNxhDVtp8 （2026-05-30公開）
- EP12「朝を少し軽くする話」 https://www.youtube.com/watch?v=0Ebwr7PpXlQ
- EP13制作物: video `latte_ch/video/latte_ch_ep13_final.mp4` / thumb `latte_ch/thumbnails/latte_ch_ep13_thumbnail.jpg` / Shorts plan `latte_ch/ideas/ep13_yorunikakaesuginai/`。
- EP14: 企画レビューあり（`latte_ch/ideas/ep14_planning_review.md`）→ 制作はこれから。
- **EP12は作り直さない**（現行版公開優先）。

## 8. 使用スクリプト（→ `SCRIPTS_INDEX.md`）
- 本編生成: `make_latte_ch_ep01.py`〜`make_latte_ch_ep13.py`（一部 `_v2`）
- 音声: `make_latte_ch_ep**_voice.py` / `make_latte_ch_voice.py`
- サムネ: `make_ep10_thumbnail.py`〜`make_ep13_thumbnail.py`
- アップロード: `latte_ch_ep07_upload.py`〜`latte_ch_ep13_upload.py`
- 字幕チェック: `latte_ch_caption_check.py` / `latte_ch_caption_fix.py`
- テンプレ/工場: `make_latte_ch_template.py` / `latte_ch_factory.py`

## 9. 関連フォルダ
- `/Users/khhr/Desktop/latte_ch/`（本体: video / narration / scripts / thumbnails / ideas / docs / shorts / assets）
- ブランド素材: `/Users/khhr/Desktop/latte_music/assets/`（latte_ch_icon_* / latte_ch_youtube_banner_* 多数）
- docs: `latte_ch/docs/`（brand_guide / production_system / quality_gate / production_template / progress_note）

## 10. 次にやること
1. **【高】CHアイコン/バナーのYouTube手動反映**（`latte_ch_icon_face_final_800.png` / `latte_ch_youtube_banner_final_v2.png`）。
2. **【高】EP14 の企画確定・制作**（`ideas/ep14_planning_review.md` ベース）。
3. **【中】EP13以降の品質改善**: ラテの軽いアニメ・表情差分・ポーズ差分・背景差分を段階導入（工数は増やさず使い回せる差分から）。
4. **【低】Shorts展開・SNS連動**。

## 11. Codexへの注意点
- BGMとは**別ブランド・別色**（CH=スカイブルー、BGM=ネイビー）。混同しない。
- ラテキャラ必須・四国めたん必須・静止画のみ禁止・既存BGM流用禁止を厳守。
- 採用済みアイコン/バナー（face_final / final_v2）を正式版として扱い、旧版を格上げしない。
- 公開済みEPは作り直さない。新EPは新規制作。曖昧なら啓一に確認。
