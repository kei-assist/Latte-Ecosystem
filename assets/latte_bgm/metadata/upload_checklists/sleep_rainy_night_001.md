# Upload Checklist: sleep_rainy_night_001

## 動画情報

| 項目 | 内容 |
|------|------|
| タイトル | 1 Hour Sleep Music 2026 \| Rainy Night BGM for Deep Sleep \| Latte BGM |
| Preset | `sleep_rainy_night` |
| 動画ファイル | sleep_rainy_night_60min_001.mp4 |
| サムネイル | sleep_rainy_night_001.png → JPG変換 |
| 長さ | 60分 |
| 解像度 | 1920×1080 |

## 制作チェック

- [ ] 画像: `assets/latte_bgm/images/source/sleep/sleep_rainy_night_001.png` を確認
- [ ] 音源: `assets/latte_bgm/audio/source/sleep_rainy_night_001.mp3` を確認
- [ ] 動画生成コマンド実行済み（下記参照）
- [ ] `videos/drafts/` で確認（冒頭・中間・末尾）
- [ ] 雨筋エフェクトが自然に見えるか確認
- [ ] ズームが遅すぎず速すぎないか確認
- [ ] 音源ループのつなぎ目が不自然でないか確認
- [ ] `videos/final/` へ移動完了

## 生成コマンド

```bash
cd scripts/latte_bgm

python3 make_video_from_image.py \
  --image ../../assets/latte_bgm/images/source/sleep/sleep_rainy_night_001.png \
  --audio ../../assets/latte_bgm/audio/source/sleep_rainy_night_001.mp3 \
  --preset sleep_rainy_night \
  --duration 3600 \
  --title "1 Hour Sleep Music 2026 | Rainy Night BGM for Deep Sleep | Latte BGM" \
  --output ../../assets/latte_bgm/videos/drafts/sleep_rainy_night_60min_001.mp4
```

## アップロードチェック

- [ ] タイトル入力（`metadata/titles/sleep_rainy_night_001.txt` からコピー）
- [ ] 説明文入力（`metadata/descriptions/sleep_rainy_night_001.txt` からコピー）
- [ ] サムネイル設定（PNG→JPG変換してアップロード）
- [ ] タグ設定（説明文のハッシュタグを参照）
- [ ] プレイリスト追加: `Sleep & Rain BGM | Latte BGM`
- [ ] カテゴリ: 音楽
- [ ] 公開設定確認

## 公開後チェック

- [ ] YouTube URL を `Latte_BGM_Existing_Video_Remake_Map.md` に記録
- [ ] X告知ツイート投稿
- [ ] Instagram Stories 投稿（サムネイル使用）
- [ ] `Production_Log_Template_v1.md` に記録

## SNS告知文（X用）

```
新着BGM🌧️

1 Hour Sleep Music — Rainy Night

雨の夜に、静かに眠る。

▶ [URL]

#SleepMusic #RainyNight #LatteBGM #深夜BGM
```

## YouTubeタグ（コピー用）

```
sleep music, rainy night sleep, deep sleep music, rain sounds for sleeping,
1 hour sleep music, latte bgm, relaxing sleep music, rain sleep bgm,
ambient sleep music, peaceful sleep music, calm music for sleep,
rain and sleep, nighttime music, bedtime music, sleeping music
```
