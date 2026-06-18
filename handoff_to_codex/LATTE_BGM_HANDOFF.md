# LATTE BGM 引き継ぎ（詳細）

最終確認日: 2026-06-18 ／ 正本仕様: `latte-ecosystem/docs/Latte_BGM_30min_Video_Standard_Spec_v1.md`（2026-06-10制定）

---

## 1. 目的・チャンネル方針
- 世界発信のBGM YouTubeチャンネル。**コンセプト: LATTE BGM — Music for Every Moment**。
- ターゲット: 英語圏。長尺視聴。音で整える。
- 終了予定なしの継続量産フェーズ。YouTube資産を積み上げ将来収益化。
- 重点ジャンル: Sleep / Focus(Study) / Relax / Nature / Cafe / Meditation / Workout。

## 2. 正式ブランドルール（厳守）
- **基本尺は30分（1800秒）**。
- **1時間動画は Sleep / Study / Cafe / Nature など長時間再生向きだけ例外**。
- **Suno新規音源が基本。既存音源の使い回しは禁止**。
- **1曲の単純ループ禁止 → 複数曲を自然連結**。クロスフェード／音量調整（ラウドネス正規化）／冒頭フェードイン・末尾フェードアウト。
- **右上ロゴは過去動画と同じ統一アイコンを必ず使う**。
  - 統一アイコン = 丸い犬キャラ＋青ヘッドホン＋「LATTE BGM」文字。
  - 現行標準実装 = `latte_dog_icon_circle_v2.png`（160px・右上 中心x=1785,y=22〜）＋ `latte_brand_text.png`（Impact 50px・白・黒縁・影）を**別レイヤー**でoverlay。
- **背景内に犬キャラを主役として出さない**（右上ロゴとしてのみ使う）。
- **サムネ・動画・タイトル・説明欄・右上ロゴでブランド統一**。
- カラー: **ネイビー基調（Latte Blue / Latte Navy）＋カテゴリ色アクセント**（Workout=Orange / Study=Cyan / Nature=Green / Sleep=Purple / Cafe=Brown / Relax=Teal）。
- 表記は必ず `Latte BGM` / `LATTE BGM`。`Latte Music` は新規アセットで使わない。
- 静止画のみのMP4禁止・サムネ流用禁止・無関係ロゴ/スポーツマーク禁止（FIGHTERS公式は非コピー）。

詳細: `latte_music/docs/Latte_Brand_Guideline_v1.md`、`latte-ecosystem/docs/Latte_BGM_Thumbnail_Rules_v1.md`、`Latte_BGM_Visual_Asset_Guide.md`。

## 3. 現在の状態
### 初期5ジャンル 30分新ロゴ統一（現在地: Desktop直下）
| ジャンル | 正式ファイル | 長さ | 解像度 | サムネ | メタ | YouTube |
|---------|------------|------|--------|--------|------|---------|
| Boxercise/Workout | `boxercise_30min_002.mp4` | 1800s | 1920x1080 | ✅ | ✅ | 公開済み（申告） |
| Study/Deep Focus | `study_deep_focus_30min_002.mp4` | 1800s | 1920x1080 | ✅ | ✅ | 公開済み（申告） |
| Rain & Forest | `forest_relaxation_30min_002.mp4` | 1800s | 1920x1080 | ✅ | ✅ | 公開済み（申告） |
| Calm Sleep | `sleep_rainy_night_30min_002.mp4` | 1800s | 1920x1080 | ✅ | ✅ | 公開済み（※Content ID） |
| Warm Cafe | `cafe_warm_30min_005.mp4` | 1800s | 1920x1080 | ✅ | ✅ | **公開確認待ち（最優先）** |

- メタデータ `*_youtube.md` は `latte-ecosystem/assets/latte_bgm/videos/final/` に残存。
- Cafe 005 タイトル: `Warm Cafe Music for Work & Relaxation | Coffee Shop BGM | Latte BGM`。

### ブランド統一状態（2026-06-13/14 時点）
- チャンネルアイコン: **案B採用済み・YouTube反映済み**（`channel_icon_music_glow_1024.png` / `_800.png`）。犬顔アップ＋青ヘッドホン＋ネイビー＋音符。
- 動画内右上ロゴ: **v2標準**（`latte_dog_icon_circle_v2.png`）。5ジャンル適用済み。
- BGMバナー: **確定候補 `latte_bgm_youtube_banner_v2.png`（2560x1440）作成済み・安全領域検証済み・アップロード待ち**。
- 角ばりスポーツ文字 `latte_brand_text_v2.png`: ドラフト作成済み。採用は任意（採用時はスクリプトのBRAND参照切替＋再レンダー）。

## 4. Deep Focus Night（今回の新作）
- **正式動画**: `/Users/khhr/Desktop/deep_focus_night_30min_002.mp4`（240MB・2026-06-16・統一アイコン版・背景犬なし）。
- **正式サムネ**: `/Users/khhr/Desktop/deep_focus_night_latte_bgm.jpg`（2026-06-16）。
- **不採用**: `deep_focus_night_30min_001.mp4`（右上が文字ロゴ版＝統一アイコンでないため不採用。現在Desktop上に実体なし。復活させない）。
- **metadata**: `latte-ecosystem/assets/latte_bgm/videos/final/deep_focus_night_metadata.md`（本フォルダに `DEEP_FOCUS_NIGHT_metadata.md` として同梱）。
- タイトル: `30 Min Deep Focus BGM | Night Study & Work Music | LATTE BGM`。
- 公開状況: 不明（要確認）。アップロード方針 = まず限定公開 → スマホ確認 → 公開。
- 生成スクリプト: `latte-ecosystem/scripts/latte_bgm/build_deep_focus_night_30min.py` / `make_deep_focus_night_30min.py` / `make_deep_focus_night_thumbnail.py`。

## 5. Content ID（Sleep 002）— 記録と対応方針
- 対象: `sleep_rainy_night_30min_002`。使用コンテンツ = **Dusty Lullaby**。該当 0:20–2:13 / 19:32–19:48。
- 影響: **収益化のみ**（ブロック・ストライクではない）。異議申し立てしない・即削除しない・公開継続。
- 原因曲: **`audio/source/sleep_rainy_night_001.mp3` に特定済み → 今後一切再利用しない**。
- 対応: 完全新規音源で **Sleep 003** を作り直す（下記タスク）。

## 6. 旧版・不採用（保持・削除しない）
- 旧版動画（新版に置換）: `boxercise_30min_001` / `study_deep_focus_30min_001` / `forest_relaxation_30min_001` / `sleep_rainy_night_30min_001` / `cafe_warm_30min_004`(及び003/002/001)。→ YouTube側 非公開化を**検討**（ローカル保全）。
- 別尺・別シリーズ（30min統一の対象外・現状維持）: `boxercise_1hour_001` / `boxercise_10min_001` / `running_10min_001` / `workout_boxercise_60min_001`。
- 旧ブランド素材: `latte_dog_icon_circle.png`（旧右上ロゴ・旧版動画が使用）、不採用アイコン案A/C。すべて保持。

## 7. 関連フォルダ
- `/Users/khhr/Desktop/latte-ecosystem/`（本部）
  - `docs/`（仕様書・SEO・サムネルール・競合分析・リメイクMap・TODO）
  - `scripts/latte_bgm/`（制作スクリプト）
  - `assets/latte_bgm/`（images/brand, videos/final のメタ, thumbnails, metadata, youtube_package, prompts）
  - `pipelines/`（30Day Calendar, 各ジャンル30Series）、`templates/`、`workflows/latte-bgm-workflow.md`、`logs/`
- `/Users/khhr/Desktop/latte_music/`（1時間BGM量産ワークスペース・公開15本系の音源/動画/サムネ/スクリプト/各作品docs）
- `/Users/khhr/Desktop/`（直下に新ロゴ版5本・Deep Focus Night・各種バナーが点在）
- `/Users/khhr/Desktop/Latte_BGM_Deep_Focus_Coding_Session/`（Coding Session 60min一式・別パッケージ）

## 8. 使用スクリプト（→ 詳細 `SCRIPTS_INDEX.md`）
- 30分動画(新ロゴ標準/v2): `make_boxercise_30min_v2.py` / `make_study_focus_30min_v2.py` / `make_cafe_warm_30min_v2.py` / `make_forest_relaxation_30min_v2.py` / `make_sleep_rainy_night_30min_v2.py`
- 30分音源マスター: `make_nature_audio_30min.py` / `make_sleep_audio_30min.py`
- Deep Focus Night: `build_deep_focus_night_30min.py` / `make_deep_focus_night_30min.py` / `make_deep_focus_night_thumbnail.py`
- 1時間系(latte_music): `make_static_mp4.py` / `make_waveform_mp4.py` / `make_youtube_mp4.py` / `merge_mp3.py` / `make_thumbnail.py` / `upload_*.py`

## 9. 未完了タスク / 次にやること（優先順）
1. **【高】Cafe 005 公開確認**（YouTube Studio / チャンネル）。
2. **【高】Sleep 003 作り直し**: 完全新規音源を用意 → `make_sleep_audio_30min.py` で30分マスター再構築 → `make_sleep_rainy_night_30min_v2.py` の音源/出力名を差し替えて `sleep_rainy_night_30min_003.mp4`（v2新ロゴ）→ アップ後Content ID申し立てが出ないことを確認 → 公開 → 002の扱い検討。**`sleep_rainy_night_001.mp3` は使わない**。
3. **【中】旧版動画の整理**（YouTube非公開化/再生リスト除外を検討・ローカル削除しない）。
4. **【中】BGMバナー調整＋ `latte_bgm_youtube_banner_v2.png` を手動アップ**。
5. **【中】次回候補の制作**（Morning Piano Vol.3 → Deep Sleep Vol.2 → Meditation Vol.1 → Rainy Night Vol.3 等）。
6. **【中/任意】`latte_brand_text_v2.png` 採用判断**（採用時はスクリプトのBRAND参照切替＋再レンダー＋仕様書反映）。
7. **【低】30分共通テンプレ化**（成功済みスクリプトは壊さず追加型）。

## 10. Codexへの注意点
- **v2系スクリプトが新ロゴ標準**。無印（旧）スクリプトは旧ロゴ/文字ロゴ版なので新作には使わない。
- 成功済みスクリプト・公開済み動画・正式アセットは**壊さない/削除しない/上書きしない**。改修は別名v2で追加。
- ffmpeg drawtext不可 → テキストはPIL透過PNG overlay。
- 動画のYouTubeアップは**ユーザー手動**（数百MB直接アップ不可）。Codexはメタデータ・サムネ・動画ファイルを揃えるところまで。
- レンダー後は ffprobe + silencedetect + t=8右上クロップでQC。右上ロゴが読めないものは不採用。
- 制作前に最新の `CURRENT_STATUS.md`（latte-ecosystem / latte_music）と本書・標準仕様を必ず確認。曖昧なら啓一に確認。
