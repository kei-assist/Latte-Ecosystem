# KEI / Claude Code → Codex 総合引き継ぎパッケージ

作成日: 2026-06-18
作成者: Claude Code（藤田啓一の作業統括）
オーナー: 藤田啓一（@kei-assist / @KhhrLatte / @Lattech-x7o）
対象: この1週間（〜2026-06-18）にClaude Codeで扱った全作業をCodexへ完全移管する

> このファイルは「最初に読む1枚」です。詳細は同フォルダ内の個別mdに分割しています。
> 個別md: `LATTE_BGM_HANDOFF.md` / `LATTE_CH_HANDOFF.md` / `GITHUB_FOLDER_MANAGEMENT_HANDOFF.md` / `SCRIPTS_INDEX.md` / `OFFICIAL_FILES_LIST.md` / `DEEP_FOCUS_NIGHT_metadata.md`
> Codexに最初に貼る文章: `CODEX_START_PROMPT.md`

---

## A. 全体方針

### 啓一の現在の主な作業領域
- **Latte エコシステムの運営**（YouTube 2チャンネル + SNS + note + Kei Assist 副業導線）
  - Latte BGM（英語圏・長尺BGM・音で整える）
  - Latte CH（日本語圏・お金/習慣/暮らし・言葉で整える）
- **YouTube制作の自動化**（Suno音源 × Python × ffmpeg/MoviePy で動画・サムネ・メタデータを量産）
- **ブランド統一**（アイコン・右上ロゴ・バナー・サムネの統一）
- **副業（Kei Assist）への導線づくり** = ポートフォリオ化（月5万円目標）

### Codeで最近（直近1週間中心）扱っていたプロジェクト一覧
1. **Latte BGM** — 30分動画の標準化・初期5ジャンル新ロゴ統一・Deep Focus Night新作・バナー作成
2. **Latte CH** — 語り系JP動画（EP13まで公開）・CHブランド素材（スカイブルー系アイコン/バナー）作成
3. **GitHub / フォルダ管理基盤**（latte-ecosystem リポジトリ = 運営本部）
4. **画像・動画・サムネ・音源連結パイプライン**（Pythonスクリプト群）
5. **生成済み素材・完成物の管理**（動画・サムネ・音源・ロゴ・メタデータ）
6. **SNS / note / X / Instagram 展開計画**（docs内に計画あり・実投稿は手動）
7. **ポートフォリオ / 副業案件導線**
8. **作業フォルダ整理**（`_整理_YYYY-MM-DD` への種別集約・移動のみ）

詳細は **B. プロジェクト一覧** を参照。

### Codexへ移行する目的
- Code側にある「プロジェクト・ルール・仕様書・フォルダ構成・スクリプト・生成済み素材・完成物・未完了タスク・禁止事項・次にやること」を、Codexがそのまま理解して継続できる状態にする。
- 啓一が同じ説明を繰り返さずに済むようにする。
- ブランドルール・制作仕様・保護方針（壊さない/作り直さない）を引き継ぎ、品質と一貫性を保つ。

### 今後Codexで優先すべき作業（全体）
1. **Latte BGM**: Cafe 005 の公開確認 → 旧版動画の整理方針決定 → Sleep 003 作り直し（Content ID対応）→ BGMバナー調整
2. **Latte CH**: EP14以降の企画・制作（EP13まで公開済み）、CHアイコン/バナーのYouTube反映
3. **量産継続**: Latte BGM 次回候補（Morning Piano Vol.3 等）の制作
4. ポートフォリオ化・SNS展開（手動投稿前提で素材を整える）

### 触ってはいけないもの / 勝手に作り直してはいけないもの（最重要）
- **公開済みYouTube動画**（ローカルmp4もYouTube上も）削除・直接差し替えしない
- **採用済みの正式ファイル**（後述の正式版一覧）を不採用扱いにしない
- **成功済みの制作スクリプト**を壊さない（改修は別名v2スクリプトで追加する運用）
- **既存BGM音源の使い回し**は禁止（特に `audio/source/sleep_rainy_night_001.mp3` は再利用厳禁）
- **統一ブランドアイコン / 右上ロゴルール**を破らない
- **GitHub / フォルダ構成**を勝手に大幅変更しない
- 詳細は **I. Codexへの禁止事項** を参照。

---

## B. プロジェクト一覧

> 「最近Codeで扱ったもの」を全て洗い出し。各プロジェクトの詳細は個別mdに分割。

### B-1. Latte BGM（→ 詳細は `LATTE_BGM_HANDOFF.md`）
- **目的**: 英語圏向けの長尺BGM YouTubeチャンネル。音で整える。終了予定なしの継続量産・YouTube資産積み上げ・将来収益化。
- **現在の状態**: 公開15本超。初期5ジャンル（Boxercise/Study/Forest/Sleep/Cafe）の30分新ロゴ版へ統一済み（Cafe 005のみ公開確認待ち）。Deep Focus Night 30分新作（002）完成。チャンネルアイコン=案B採用済み。BGMバナーv2=確定候補作成済み（アップ待ち）。
- **重要ルール**: 基本30分（Sleep/Study/Cafe/Nature等の長時間向けのみ1時間例外）／Suno新規音源が基本・既存使い回し禁止／複数曲をクロスフェード自然連結／右上は統一犬アイコン（青ヘッドホン＋LATTE BGM文字）／背景に犬を主役で出さない／ネイビー基調。
- **関連フォルダ**:
  - `/Users/khhr/Desktop/latte-ecosystem/`（運営本部・仕様/スクリプト/正式アセット）
  - `/Users/khhr/Desktop/latte_music/`（旧来の1時間BGM量産ワークスペース・音源/動画/サムネ/スクリプト多数）
  - `/Users/khhr/Desktop/`（直下に新ロゴ版5本mp4・Deep Focus Night・各種バナーが点在）
- **使用スクリプト**: `latte-ecosystem/scripts/latte_bgm/` の `make_*_30min*.py`、`latte_music/scripts/` の `make_*` / `upload_*`（→ `SCRIPTS_INDEX.md`）
- **完成物**: → `OFFICIAL_FILES_LIST.md`
- **未完了タスク / 次にやること**: Cafe 005公開確認 → 旧版整理 → Sleep 003作り直し → BGMバナー調整 → 次回候補制作（→ H章）
- **Codexへの注意点**: v2系スクリプトが新ロゴ標準。旧スクリプト/旧動画は壊さない。詳細は `LATTE_BGM_HANDOFF.md`。

### B-2. Latte CH（→ 詳細は `LATTE_CH_HANDOFF.md`）
- **目的**: 日本語圏向けの語り系実用チャンネル。「仕事も、お金も、人生も。少しラクに整える。」お金/習慣/暮らしで信頼構築 → Kei Assist導線。
- **現在の状態**: EP13まで公開済み（最新=EP13「夜に抱えすぎない話」）。VOICEVOX四国めたん + MoviePy制作。CHブランド素材（スカイブルー系アイコン `latte_ch_icon_face_final` / バナー `latte_ch_youtube_banner_final_v2`）作成済み（YouTube反映待ち）。
- **重要ルール**: ラテキャラ必須・四国めたん必須・明るめ青基調・静止画のみ禁止・既存BGM流用禁止・EP番号サムネ非表示・NGワード（稼げる/絶対/最強/勝つ/頑張れ等）。
- **関連フォルダ**: `/Users/khhr/Desktop/latte_ch/`（本体）、ブランド素材は `/Users/khhr/Desktop/latte_music/assets/`（latte_ch_* 多数）。
- **使用スクリプト**: `latte_ch/scripts/make_latte_ch_ep*.py` / `*_voice.py` / `make_ep*_thumbnail.py` / `latte_ch_ep*_upload.py`。
- **完成物**: EP01〜EP13動画・サムネ・ナレーション・タイミングJSON。
- **未完了タスク / 次にやること**: EP14企画・制作、CHアイコン/バナーのYouTube反映、品質改善（ラテのアニメ/表情/ポーズ/背景差分）。
- **Codexへの注意点**: BGMチャンネルとは別ブランド・別色（CH=スカイブルー、BGM=ネイビー）。

### B-3. GitHub管理基盤（→ 詳細は `GITHUB_FOLDER_MANAGEMENT_HANDOFF.md`）
- **目的**: 運営仕様・自動化・KPI・SNS計画の一元管理（本部リポジトリ）。
- **現在の状態**: `latte-ecosystem` = GitHubリポジトリ（origin: github.com/kei-assist/Latte-Ecosystem）。`bruno` = ポートフォリオ用リポジトリ（github.com/koumelatte/bruno-sales-report-）。`latte_music` はローカル.gitあり（remote未設定）。
- **重要ルール**: メディア（mp4/mp3/wav/png/jpg/認証json/pickle）は **コミットしない**（.gitignore管理）。mdドキュメントのみ追跡。
- **関連フォルダ/ファイル**: → 個別md。
- **未完了タスク**: 旧版ファイル整理方針、追加リポジトリ候補（latte-bgm-scripts等）。
- **Codexへの注意点**: フォルダ構成を勝手に大幅変更しない。削除/移動は確認してから。

### B-4. 画像・動画・サムネ・音源連結パイプライン（→ 詳細は `SCRIPTS_INDEX.md`）
- **目的**: Suno音源 → 30分/60分マスター音声（クロスフェード連結）→ 動画（背景＋右上ロゴ＋イントロ）→ サムネ → メタデータ、を量産する。
- **現在の状態**: 確立済み。ffmpeg は drawtext非対応のため **テキストはPIL生成の透過PNGをoverlay合成**する運用。
- **重要な技術注意**: drawtext不可 / 数百MB動画のYouTube直接アップ不可（**動画投入はユーザー手動**）/ レンダー後は ffprobe + silencedetect + 右上クロップでQC。
- **Codexへの注意点**: → F章・`SCRIPTS_INDEX.md`。

### B-5. 生成済み素材・完成物の管理（→ `OFFICIAL_FILES_LIST.md`）
- 動画・サムネ・BGM音源・ロゴ・画像・md仕様書・メタデータ・スクリプトの正式/不採用を一覧化。

### B-6. SNS / note / X / Instagram 展開
- **目的**: YouTube → X(共感) → Instagram(世界観) → TikTok(短尺) → Kei Assist の導線。
- **現在の状態**: 計画docはあり（`latte-ecosystem/docs/sns-integration-plan.md`、`workflows/sns-post-workflow.md`、`templates/sns-post.md`）。実投稿は手動。
- **関連フォルダ**: `/Users/khhr/Desktop/Instagram/`、`latte_x_header_renewal/`（X用ヘッダー素材1500x500）。
- **Codexへの注意点**: X(@KhhrLatte)は個人ブランドでLatte BGM/CHとは別扱い。

### B-7. ポートフォリオ / 副業案件導線（Kei Assist）
- **目的**: 月5万円目標。スプレッドシート/ダッシュボード/AI自動化案件の獲得。Latteエコシステム自体を「実践者ポートフォリオ」として見せる。
- **重視する実績候補**: Fitness Tracker、売上日報、勤務管理、YouTube運営管理、KPI管理。
- **関連フォルダ**: `/Users/khhr/Desktop/ポートフィリオ/`、`fitness-tracker-gas/`、`bruno/`、`提案文/`、`要望書/`。
- **表現ルール**: プロフィールで「日本製鉄勤務」「単身赴任中」「AI活用学習中」は**使わない**。学習者ではなく実践者として見せる。

### B-8. 作業フォルダ整理
- **ルール**: `_整理_YYYY-MM-DD` フォルダに種別（書類/画像/動画/音声/表計算/その他）で集約。**移動のみ**（成果物は据え置き、削除しない）。
- **既存**: `_整理_2026-05-31` / `_整理_2026-06-04` / `_整理_2026-06-10`。

### B-9. その他Codeで扱ったフォルダ（Desktop直下・参考）
- `bliss_eyecatch/`（歯科メディ アイキャッチ系）、`latte_images/`（ラテキャラ画像素材）、`latte_x_header_renewal/`（X用ヘッダー）、`JR東日本/`、`apass/`、`Python/`、`写真/`、`書類/`、`Instagram/`。
- これらは今回の引き継ぎの主対象ではないが、Desktopに同居しているため**誤って整理・削除しない**。

---

## C. LATTE BGM（要点・詳細は `LATTE_BGM_HANDOFF.md`）

### 正式ブランドルール
- 世界発信のBGMチャンネル。コンセプト: **LATTE BGM — Music for Every Moment**。
- **基本尺は30分**（1800秒）。
- **1時間動画は Sleep / Study / Cafe / Nature など長時間再生向きだけ例外**。
- **Suno新規音源が基本**。既存音源の使い回しは禁止。
- 1曲単純ループではなく**複数曲を自然連結**（クロスフェード／音量調整／フェードイン・フェードアウト）。
- **右上ロゴは過去動画と同じ統一アイコンを必ず使う**。
- 統一アイコン = **丸い犬キャラ＋青ヘッドホン＋「LATTE BGM」文字**（現行標準 = `latte_dog_icon_circle_v2.png` ＋ `latte_brand_text.png`）。
- **背景内に犬キャラを主役として出さない**。
- サムネ・動画・タイトル・説明欄・右上ロゴでブランド統一（ネイビー基調 + カテゴリ色アクセント）。

### 今回の Deep Focus Night 動画について
- **正式動画**: `deep_focus_night_30min_002.mp4` （フルパス `/Users/khhr/Desktop/deep_focus_night_30min_002.mp4`・240MB・2026-06-16）
- **正式サムネ**: `deep_focus_night_latte_bgm.jpg` （`/Users/khhr/Desktop/deep_focus_night_latte_bgm.jpg`・2026-06-16）
- **不採用**: `deep_focus_night_30min_001.mp4`（※現在Desktop上に実体は見当たらない＝既に置換/削除済みの可能性。復活させない）
- **不採用理由**: 右上が「文字ロゴ版」で統一アイコンではないため。
- **公開状況**: 不明（ローカルからは判定不可）。要ユーザー/YouTube Studio確認。
- **metadata md の場所**: `/Users/khhr/Desktop/latte-ecosystem/assets/latte_bgm/videos/final/deep_focus_night_metadata.md`（このフォルダにもコピー `DEEP_FOCUS_NIGHT_metadata.md` を同梱）。

### 初期5ジャンル新ロゴ統一（30分・現在地はDesktop直下）
| ジャンル | 正式ファイル（Desktop直下） | 状態 |
|---------|------------------------|------|
| Boxercise/Workout | `boxercise_30min_002.mp4` | 公開済み（ユーザー申告） |
| Study/Deep Focus | `study_deep_focus_30min_002.mp4` | 公開済み（ユーザー申告） |
| Rain & Forest | `forest_relaxation_30min_002.mp4` | 公開済み（ユーザー申告） |
| Calm Sleep | `sleep_rainy_night_30min_002.mp4` | 公開済み（※Content ID申し立てあり） |
| Warm Cafe | `cafe_warm_30min_005.mp4` | **公開確認待ち（最優先）** |

メタデータ `*_youtube.md` は `latte-ecosystem/assets/latte_bgm/videos/final/` に残存。

---

## D. LATTE CH（要点・詳細は `LATTE_CH_HANDOFF.md`）

- **チャンネル方針**: 「仕事も、お金も、人生も。少しラクに整える。」再生数より信頼構築。ベンチマーク=サラタメ型。お金40%/習慣40%/暮らし20%。
- **ブランドカラー**: スカイブルー系（明るめの青 #59CBE8基調）＋白文字＋黄色アクセント。BGM(ネイビー)と色で差別化する兄弟ブランド。
- **サムネ方針**: アニメ調ラテキャラ必須・`Latte ch`表記・EP番号は出さない・白背景だけ/写真だけ/ラテ不在は禁止・タイトル文字大きく。
- **アイコン/ヘッダー方針**: アイコン=`latte_ch_icon_face_final.png`（顔のみ・服なし・最終確定）/ バナー=`latte_ch_youtube_banner_final_v2.png`（2560x1440・安全領域フィット確定）。場所はいずれも `/Users/khhr/Desktop/latte_music/assets/`。YouTube反映は手動・**未実施**。
- **企画方針**: 共感→問い→整えるポイント3つ→今日の1アクション→ラテから一言。NGワード/NGトーン厳守。
- **既存動画**: EP01〜EP13公開済み（`latte_ch/video/latte_ch_ep**_final.mp4`）。最新EP13 = https://www.youtube.com/watch?v=B8cNxhDVtp8
- **使用スクリプト**: `make_latte_ch_ep*.py` / `*_voice.py`（VOICEVOX四国めたん）/ `make_ep*_thumbnail.py` / `latte_ch_ep*_upload.py`。
- **VOICEVOX/動画生成ルール**: ナレーション=VOICEVOX四国めたん（`narration/*.wav`）、タイミングJSON（`scripts/latte_ch_timing_*.json`）で字幕同期、軽いアニメ必須（静止画のみ禁止）。
- **次にやること**: EP14企画・制作、CHアイコン/バナーYouTube反映、EP13以降の品質改善（ラテのアニメ/表情/ポーズ/背景差分）。
- **Codexへの注意点**: EP12は作り直さない（現行版公開優先）。

---

## E. GitHub / フォルダ管理（詳細は `GITHUB_FOLDER_MANAGEMENT_HANDOFF.md`）

- **GitHub管理基盤の現状**:
  - `latte-ecosystem` → origin `https://github.com/kei-assist/Latte-Ecosystem.git`（運営本部・mdのみ追跡）
  - `bruno` → origin `https://github.com/koumelatte/bruno-sales-report-.git`（ポートフォリオ・GitHub Pages）
  - `latte_music` → ローカル.gitあり / remote未設定
  - `latte_ch` → gitなし（ローカル作業フォルダ）
- **ローカルフォルダの場所**: すべて `/Users/khhr/Desktop/` 直下。
- **整理済みフォルダ**: `_整理_2026-05-31` / `_整理_2026-06-04` / `_整理_2026-06-10`。
- **整理途中**: なし（次回整理時は新しい `_整理_YYYY-MM-DD` を作る運用）。
- **触っていいフォルダ**: 各プロジェクトの `docs/` `scripts/`（mdやスクリプトの追加・更新）。
- **触る前に確認が必要**: `assets/` `video/` `audio/` `thumbnails/`（完成物・認証情報を含む）、Desktop直下の各種mp4/png。
- **古いファイル・不採用ファイルの扱い**: 削除しない・上書きしない・保持。正式版を不採用に格下げしない。
- **Codexで最初に開くべきフォルダ**: `/Users/khhr/Desktop/latte-ecosystem/`（特に `README.md` / `CURRENT_STATUS.md` / `docs/`）。

---

## F. 画像・動画生成パイプライン（詳細は `SCRIPTS_INDEX.md`）

- **音源連結**: `make_nature_audio_30min.py` / `make_sleep_audio_30min.py` / `merge_mp3.py` 等。複数Suno音源をクロスフェード連結（通常4秒・Sleep系6秒）、ラウドネス正規化（通常−14 LUFS / Sleep −16 LUFS）、冒頭フェードイン3〜5秒・末尾フェードアウト6〜10秒。
- **動画生成（30分・新ロゴ標準）**: `make_boxercise_30min_v2.py` / `make_study_focus_30min_v2.py` / `make_cafe_warm_30min_v2.py` / `make_forest_relaxation_30min_v2.py` / `make_sleep_rainy_night_30min_v2.py`。背景静止画/映像 ＋ 右上ロゴ（犬アイコンv2＋LATTE BGM文字を別レイヤーoverlay）＋ 冒頭イントロoverlay。
- **動画生成（1時間・latte_music系）**: `make_static_mp4.py` / `make_waveform_mp4.py` / `make_youtube_mp4.py` 等。
- **サムネ生成**: `make_deep_focus_night_thumbnail.py` / `make_thumbnail.py` / `make_*_thumbnail.py`。1280x720・2MB以内・右上に統一ロゴ。
- **入力**: Suno生成mp3（Downloads等）、背景画像、ブランドPNG（`images/brand/`）。
- **出力**: `*_30min_*.mp4`（1920x1080/H.264/AAC）、`*_thumbnail.png/jpg`、`*_youtube.md`（メタデータ）。
- **使い回してよいテンプレ**: v2系スクリプト（新ロゴ標準）、`Latte_BGM_Metadata_Template_v1.md`、`Latte_BGM_Suno_Prompt_Library_v1.md`、`youtube-description.md`。
- **古くて使わない方がいいテンプレ**: 旧 `make_*_30min.py`（v2でない無印・旧ロゴ/文字ロゴ版）、旧ロゴ素材 `latte_dog_icon_circle.png`（旧版動画の再現用にのみ保持）。
- **注意点 / 失敗しやすいポイント**:
  - このMacの **ffmpeg は drawtext 非対応** → テキストは必ずPIL生成の透過PNGをoverlay。
  - **数百MBの動画はClaude/Codexから直接YouTubeアップ不可** → 動画投入はユーザー手動。
  - レンダー後QC必須: ffprobeで長さ/解像度/コーデック、全編silencedetect、t=8右上クロップでスマホ可読性。
  - 右上ロゴが小さすぎ/読めないものは不採用。

---

## G. 生成済み素材・完成物（詳細は `OFFICIAL_FILES_LIST.md`）

代表的な正式版（フルパス・最終更新は `OFFICIAL_FILES_LIST.md` 参照）:
- 動画(BGM 30min正式): Desktop直下の `boxercise_30min_002.mp4` / `study_deep_focus_30min_002.mp4` / `forest_relaxation_30min_002.mp4` / `sleep_rainy_night_30min_002.mp4` / `cafe_warm_30min_005.mp4` / `deep_focus_night_30min_002.mp4`
- サムネ(正式): 各 `*_thumbnail.png` ＋ `deep_focus_night_latte_bgm.jpg`
- ブランド素材(正式): `latte-ecosystem/assets/latte_bgm/images/brand/channel_icon_music_glow_1024.png`(=案B) / `latte_dog_icon_circle_v2.png`(右上ロゴ) / `latte_brand_text.png`(文字) / `latte_bgm_youtube_banner_v2.png`(BGMバナー)
- Latte CH素材(正式): `latte_music/assets/latte_ch_icon_face_final(_800).png` / `latte_ch_youtube_banner_final_v2.png`
- BGM音源: `latte_music/audio/*.mp3`（公開済みシリーズ各Vol）
- md仕様書(正本): `latte-ecosystem/docs/Latte_BGM_30min_Video_Standard_Spec_v1.md`（30分標準仕様の正本）、`latte_music/docs/Latte_Brand_Guideline_v1.md`、`latte_ch/docs/brand_guide.md` / `latte_ch/LATTE_MASTER_CONTEXT.md`

---

## H. 未完了タスク（優先度つき）

### 優先度: 高
1. **Cafe 005 のYouTube公開確認**（`cafe_warm_30min_005.mp4`）— 確認できれば初期5ジャンル新ロゴ統一が完全完了。
2. **Sleep 003 の作り直し**（Content ID対応）— `sleep_rainy_night_30min_002` にContent ID申し立て（Dusty Lullaby・収益化のみ影響）。原因曲 `audio/source/sleep_rainy_night_001.mp3` は**再利用厳禁**。完全新規音源で30分マスター再構築 → `sleep_rainy_night_30min_003.mp4`（v2新ロゴ仕様）。
3. **Latte CH アイコン/バナーのYouTube反映**（`latte_ch_icon_face_final_800.png` / `latte_ch_youtube_banner_final_v2.png`）— 手動アップ。
4. **Latte CH EP14 の企画・制作**（EP13まで公開済み）。

### 優先度: 中
5. **旧版BGM動画の整理**（boxercise/study/forest/sleep の_001、cafe_004等）— YouTube側で非公開化/再生リスト除外を検討。**ローカル削除はしない**。
6. **Latte BGM ヘッダー（バナー）調整**＋ `latte_bgm_youtube_banner_v2.png` のYouTube手動アップ。
7. **Latte BGM 次回候補の制作**（Morning Piano Vol.3 → Deep Sleep Vol.2 → Meditation Vol.1 → Rainy Night Vol.3 等）。
8. **角ばりスポーツ文字 `latte_brand_text_v2.png` を採用するか判断**（採用時はスクリプトのBRAND参照切替・再レンダー）。
9. **スマホ確認**（公開/限定公開動画の右上ロゴ・音量・1080p・サムネ表示）。

### 優先度: 低
10. **30分動画の共通テンプレ化**（成功済みスクリプトは壊さず追加型で）。
11. **SNS/note/X/Instagram 投稿**（手動・計画docあり）。
12. **ポートフォリオ化**（Fitness Tracker / 売上日報 / 勤務管理 / YouTube運営管理 を資産化）。
13. **作業フォルダ整理**（次回は新しい `_整理_YYYY-MM-DD`）。
14. **GitHub追加リポジトリ候補**（latte-bgm-scripts 等）の検討。

---

## I. Codexへの禁止事項

1. **勝手に動画を作り直さない**（特に公開済み・採用済み）。
2. **勝手にサムネを作り直さない**。
3. **古い仕様書を最新ルールより優先しない**（最新 = `Latte_BGM_30min_Video_Standard_Spec_v1.md`(2026-06-10制定) と各 `CURRENT_STATUS.md` / このハンドオフ）。
4. **不採用ファイルを正式版にしない**（例: deep_focus_night_30min_001、cafe_004以前、無印スクリプト）。
5. **LATTE BGMの右上統一アイコンルールを破らない**（丸い犬＋青ヘッドホン＋LATTE BGM文字）。
6. **既存音源を勝手に使い回さない**（特に `audio/source/sleep_rainy_night_001.mp3` は再利用厳禁）。
7. **GitHubやフォルダ構成を勝手に大幅変更しない**。
8. **削除や上書きは必ず確認してから行う**（メディア・認証情報・正式版は特に）。
9. **不明点がある場合は勝手に推測せず報告する**（曖昧なときは確認を取る）。
10. **メディア（mp4/mp3/png等）と認証情報（json/pickle）をGitにコミットしない**。
11. プロフィール表現で「日本製鉄勤務/単身赴任中/AI活用学習中」を**使わない**。

---

## J. Codexが最初にやること（手順）

1. このフォルダの `CODEX_START_PROMPT.md` の指示に従う。
2. **`KEI_CODE_TO_CODEX_HANDOFF.md`（本ファイル）を最後まで読む**。
3. 同フォルダの個別md（`LATTE_BGM_HANDOFF.md` / `LATTE_CH_HANDOFF.md` / `GITHUB_FOLDER_MANAGEMENT_HANDOFF.md` / `SCRIPTS_INDEX.md` / `OFFICIAL_FILES_LIST.md` / `DEEP_FOCUS_NIGHT_metadata.md`）を読む。
4. **latte-ecosystem の場所を確認**: `/Users/khhr/Desktop/latte-ecosystem/`。
5. 主要フォルダ一覧を確認: `latte-ecosystem/` `latte_music/` `latte_ch/`（＋Desktop直下の正式mp4）。
6. 最新仕様書を確認: `latte-ecosystem/docs/Latte_BGM_30min_Video_Standard_Spec_v1.md` ＋ 各 `CURRENT_STATUS.md`。
7. **H章の未完了タスク**を確認。
8. **勝手に制作・削除・作り直しをせず、まず「現状把握の報告」と「次にやるべきことの提案」を啓一に提出する**。承認を得てから着手する。
