# 主要スクリプト一覧

最終確認日: 2026-06-18。パスは `/Users/khhr/Desktop/` 起点。
共通の技術注意は末尾参照。

---

## A. Latte BGM 30分（latte-ecosystem/scripts/latte_bgm/）

### 動画生成 — 新ロゴ標準（v2＝これを使う）
| スクリプト | 何をするか | 入力 | 出力 |
|-----------|-----------|------|------|
| make_boxercise_30min_v2.py | Workout 30分動画（新ロゴv2） | 30分音源・背景・brand PNG | boxercise_30min_002.mp4 |
| make_study_focus_30min_v2.py | Study 30分動画（新ロゴv2） | 同上 | study_deep_focus_30min_002.mp4 |
| make_cafe_warm_30min_v2.py | Cafe 30分動画（新ロゴv2） | 同上 | cafe_warm_30min_005.mp4 |
| make_forest_relaxation_30min_v2.py | Forest 30分動画（新ロゴv2） | 同上 | forest_relaxation_30min_002.mp4 |
| make_sleep_rainy_night_30min_v2.py | Sleep 30分動画（新ロゴv2） | 同上 | sleep_rainy_night_30min_*.mp4（Sleep 003はこれを流用） |
| build_deep_focus_night_30min.py / make_deep_focus_night_30min.py | Deep Focus Night 30分動画 | 音源・背景・brand PNG | deep_focus_night_30min_002.mp4 |

### 音源マスター（30分・クロスフェード連結）
| スクリプト | 何をするか |
|-----------|-----------|
| make_nature_audio_30min.py | Nature/Forest系 30分マスター生成（複数曲連結） |
| make_sleep_audio_30min.py | Sleep系 30分マスター生成（Sleep 003はこれで新音源連結） |

### サムネ
| スクリプト | 何をするか |
|-----------|-----------|
| make_deep_focus_night_thumbnail.py | Deep Focus Night サムネ生成 |
| make_video_from_image.py / make_video_from_image_ffmpeg.sh | 静止画→動画化（汎用） |
| batch_make_videos.py | 複数動画の一括生成 |

### 旧（無印・新作には使わない／保持）
- make_boxercise_30min.py / make_cafe_warm_30min.py / make_forest_relaxation_30min.py / make_sleep_rainy_night_30min.py（旧ロゴ・文字ロゴ版）

## B. Latte BGM 1時間系（latte_music/scripts/）
| スクリプト | 何をするか |
|-----------|-----------|
| merge_mp3.py | 複数mp3をクロスフェード連結し長尺マスター化 |
| make_static_mp4.py | 静止画＋音源で長尺mp4 |
| make_waveform_mp4.py | 波形ビジュアル付きmp4 |
| make_youtube_mp4.py | YouTube用mp4書き出し |
| make_thumbnail.py / make_*_thumbnail.py | サムネ生成（ジャンル別） |
| genre_detect.py / unsplash_fetch.py | ジャンル判定 / 画像取得（※CHは写真NG・BGMで使用） |
| upload_to_youtube.py / daily_upload.py / upload_*.py | YouTubeアップロード補助（要認証・大容量は手動推奨） |
| set_thumbnails.py / set_localizations.py / add_to_playlist.py / create_playlists.py | サムネ設定/多言語/プレイリスト |
| check_pending_videos.py / replace_videos.py / delete_duplicates.py | 状態確認/差し替え/重複削除（**実行前に確認**） |
| config.py / common.py | 共通設定・ユーティリティ（API認証情報を参照） |

## C. Latte CH（latte_ch/scripts/）
| スクリプト | 何をするか |
|-----------|-----------|
| make_latte_ch_ep01.py 〜 make_latte_ch_ep13.py（一部 _v2） | EP本編動画生成（MoviePy・ラテキャラ＋字幕＋軽アニメ） |
| make_latte_ch_ep**_voice.py / make_latte_ch_voice.py | VOICEVOX四国めたんでナレーション生成 |
| make_ep10_thumbnail.py 〜 make_ep13_thumbnail.py | EPサムネ生成 |
| latte_ch_ep07_upload.py 〜 latte_ch_ep13_upload.py | EPアップロード補助 |
| latte_ch_caption_check.py / latte_ch_caption_fix.py | 字幕チェック/修正 |
| make_latte_ch_template.py / latte_ch_factory.py | テンプレ/量産工場 |
| ep**_voice_segments.json / latte_ch_timing_*.json | 音声区切り・字幕タイミング |

## D. 認証情報（コミット禁止・削除禁止）
- `latte_music/assets/client_secret.json`
- `latte_music/assets/*_token.pickle`（youtube_token / youtube_full_token / latte_ch_token / latte_ch_caption_token）

---

## 共通の技術注意（失敗しやすいポイント）
1. **このMacのffmpegは drawtext 非対応** → 動画内テキストは必ず **PIL生成の透過PNGを overlay 合成**する。
2. **数百MBの動画はClaude/Codexから直接YouTubeアップ不可** → 動画ファイル投入は**ユーザー手動**。スクリプトはメタデータ/サムネ設定までを担う想定。
3. **レンダー後QC必須**:
   - ffprobe で 長さ(30:00/1:00:00)・解像度(1920x1080)・コーデック(H.264/AAC)確認
   - 全編 silencedetect で無音/不自然な切れ目チェック
   - t=8 付近の右上クロップで**スマホ可読性**（犬アイコン＋LATTE BGM文字が両方読める）
4. **音声仕様**: クロスフェード 通常4秒/Sleep系6秒、ラウドネス 通常−14 LUFS/Sleep −16 LUFS、冒頭フェードイン3〜5秒/末尾フェードアウト6〜10秒。
5. **成功済みスクリプトは壊さない**。改修は別名（v2/v3）で追加する運用。
6. **状態変更系スクリプト**（replace_videos / delete_duplicates / set_thumbnails 等）は**実行前に必ず確認**。
