# Latte Ecosystem

> BGMで整えて、言葉で考える——それが Latte のスタイル。

**Latte BGM / Latte CH / SNS / note / Kei Assist** の運営・自動化・仕様管理を行う本部リポジトリ。

---

## チャンネル構成

| チャンネル | コンセプト | ターゲット |
|-----------|-----------|-----------|
| Latte BGM | 音で整うBGMチャンネル | 英語圏・長尺視聴 |
| Latte CH | 言葉で整える実用チャンネル | 日本語圏・お金/習慣/仕事 |
| SNS | X / Instagram / TikTok | ブランド拡張・案件導線 |
| note | 深堀り文章資産 | Kei Assist 導線 |
| Kei Assist | 副業・案件窓口 | スプレッドシート/AI自動化 |

---

## ディレクトリ構成

```
Latte-Ecosystem/
│
├── docs/                          # 運営仕様・管理資料
│   ├── latte-bgm-operation-spec.md   # Latte BGM 運営仕様
│   ├── latte-ch-operation-spec.md    # Latte CH 運営仕様
│   ├── sns-integration-plan.md       # SNS 連携計画
│   ├── kpi-management.md             # KPI管理（BGM / CH / SNS）
│   ├── github-management.md          # GitHub管理資料
│   └── ecosystem-overview.md         # エコシステム全体設計
│
├── workflows/                     # 作業手順フロー
│   ├── latte-bgm-workflow.md         # BGM制作〜投稿フロー
│   ├── latte-ch-workflow.md          # CH制作〜投稿フロー
│   └── sns-post-workflow.md          # SNS投稿フロー
│
├── templates/                     # 再利用テンプレート
│   ├── youtube-description.md        # YouTube説明文テンプレート
│   ├── sns-post.md                   # SNS投稿テンプレート
│   └── episode-script.md             # Latte CH スクリプトテンプレート
│
├── logs/                          # レビュー記録
│   └── README.md                     # ログ命名規則・テンプレート
│
├── pipelines/                     # 自動化・コンテンツ計画
│   ├── automation-roadmap.md         # 自動化ロードマップ（Phase 1〜4）
│   └── content-calendar.md           # コンテンツカレンダー
│
├── .gitignore                     # メディアファイル除外設定
└── README.md                      # このファイル
```

---

## 最終導線

```
Latte CH / Latte BGM（YouTube）
        ↓
X / Instagram / TikTok / note
        ↓
Kei Assist
        ↓
スプレッドシート / ダッシュボード / AI自動化 案件
```

---

## 関連リポジトリ

| リポジトリ | 用途 |
|-----------|------|
| [Latte-Ecosystem](https://github.com/kei-assist/Latte-Ecosystem) | 本部・仕様管理（このリポジトリ） |
| [bruno-sales-report](https://github.com/kei-assist/bruno-sales-report) | ポートフォリオ（売上日報） |

---

## Owner

藤田啓一 / [@kei-assist](https://github.com/kei-assist)
