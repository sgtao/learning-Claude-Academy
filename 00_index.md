# 学習メモ 索引（Claude Academy）

> このファイルは `tools/build_index.py` が `ledger.csv` から作る。手で直さない（直すなら `ledger.csv`）。

## 状態の数（全 73 ページ）

| 状態 | 件数 |
|---|---|
| 未着手 | 49 |
| 取得済 | 0 |
| 作成中 | 0 |
| 完了 | 21 |
| 薄いページ | 2 |
| 重複 | 0 |
| 失敗 | 1 |
| 要確認 | 0 |

## フォルダの見方

```
03_outputs/
├── README.md            この場所の地図
├── 00_index.md          この索引（台帳から作る）
├── ledger.csv           台帳（ページの一覧と状態の正本）
├── tools/               検査と台帳のスクリプト（tools/README.md）
└── step<N>_<名前>/       ステップごと（0 入口 ／ 1 基礎 ／ 2 道具 ／ 3 職種 ／ 4 発展）
    └── <NN>_<まとまり>/  関連するページのまとまり
        └── <NN>_<ページ>/ 1 ページ分（README、00_originals、*_explained、スライド）
```

## ステップ 0：入口（`step0_intro/`）

| ID | ページ | 分 | 種類 | 状態 | 学習済みの日 | 備考 |
|---|---|---|---|---|---|---|
| 0-1 | [学ぶ（/learning 入口）](step0_intro/01_claude-ai-learning/01_learning/README.md) | － | 学習・ビジネス | 完了 |  | Chrome で読む。ボタンは押さない |
| 0-2 | [Claude 101（コースのトップ）](step0_intro/02_academy-courses-claude-101/01_claude-101/README.md) | 150 | 学習・ビジネス | 完了 |  |  |
| 0-3 | [Claudeを使い始める](step0_intro/03_academy-tutorials/01_getting-started-with-claude/README.md) | 5 | 技術・ハウツー | 完了 |  |  |
| 0-4 | [Coworkを3つのステップで始める](step0_intro/03_academy-tutorials/02_get-started-in-claude-cowork-in-three-steps/README.md) | 4 | 技術・ハウツー | 完了 |  | 旧名称の題名 |
| 0-5 | [Coworkで最初のタスクを委任する](step0_intro/03_academy-tutorials/03_delegating-your-first-task-in-claude-cowork/README.md) | 4 | 技術・ハウツー | 完了 |  | 旧名称の題名 |
| 0-6 | [Claudeをカスタマイズする](step0_intro/03_academy-tutorials/04_customize-claude-cowork/README.md) | 7 | 技術・ハウツー | 完了 |  | 2-1 と同じページ（実体はここ） |

## ステップ 1：基礎（Claude 101）（`step1_basics/`）

| ID | ページ | 分 | 種類 | 状態 | 学習済みの日 | 備考 |
|---|---|---|---|---|---|---|
| 1-1 | [Claudeとは何ですか？](step1_basics/01_academy-courses-claude-101/01_what-is-claude/README.md) | 5 | 学習・ビジネス | 完了 |  |  |
| 1-2 | [Claudeとの最初の会話](step1_basics/01_academy-courses-claude-101/02_your-first-conversation-with-claude/README.md) | 15 | 学習・ビジネス | 完了 |  |  |
| 1-3 | [より良い結果を得る](step1_basics/01_academy-courses-claude-101/03_getting-better-results/README.md) | 10 | 学習・ビジネス | 完了 |  |  |
| 1-4 | [デスクトップでClaudeとどのように仕事をするか](step1_basics/01_academy-courses-claude-101/04_claude-desktop-app-chat-cowork-code/README.md) | 10 | 学習・ビジネス | 完了 |  |  |
| 1-5 | [プロジェクト入門](step1_basics/01_academy-courses-claude-101/05_introduction-to-projects/README.md) | 15 | 学習・ビジネス | 完了 |  |  |
| 1-6 | [アーティファクトで作成する](step1_basics/01_academy-courses-claude-101/06_creating-with-artifacts/README.md) | 10 | 学習・ビジネス | 完了 |  |  |
| 1-7 | [スキルを活用する](step1_basics/01_academy-courses-claude-101/07_working-with-skills/README.md) | 15 | 学習・ビジネス | 完了 |  |  |
| 1-8 | [ツールを接続する](step1_basics/01_academy-courses-claude-101/08_connecting-your-tools/README.md) | 15 | 学習・ビジネス | 完了 |  |  |
| 1-9 | [Enterprise Search（Team・Enterprise 向け）](step1_basics/01_academy-courses-claude-101/09_enterprise-search/README.md) | 15 | 学習・ビジネス | 完了 |  | プラン条件（Team・Enterprise）を照合する |
| 1-10 | [深掘り調査のためのリサーチ機能（有料）](step1_basics/01_academy-courses-claude-101/10_research-mode-for-deep-dives/README.md) | 10 | 学習・ビジネス | 完了 |  | プラン条件（有料）を照合する |
| 1-11 | [Claudeの活用例：職種別ユースケース](step1_basics/01_academy-courses-claude-101/11_claude-in-action-use-cases-by-role/README.md) | 2 | 学習・ビジネス | 完了 |  |  |
| 1-12 | [Claudeを活用するその他の方法](step1_basics/01_academy-courses-claude-101/12_other-ways-to-work-with-claude/README.md) | 15 | 学習・ビジネス | 完了 |  |  |
| 1-13 | [次のステップ](step1_basics/01_academy-courses-claude-101/13_what-s-next/README.md) | 2 | 学習・ビジネス | 完了 |  |  |
| 1-14 | [コースクイズ](step1_basics/01_academy-courses-claude-101/14_certificate-of-completion/README.md) | 8 | 学習・ビジネス | 薄いページ |  | 本文なし（題名とクイズ 8 分だけ） |
| 1-15 | [修了バッジ](step1_basics/01_academy-courses-claude-101/15_badge/README.md) | － | 学習・ビジネス | 失敗 |  | JS で描画されるため取得できない（--force は使わない） |

## ステップ 2：道具を整える（`step2_tools/`）

| ID | ページ | 分 | 種類 | 状態 | 学習済みの日 | 備考 |
|---|---|---|---|---|---|---|
| 2-1 | Claudeをカスタマイズする | 7 | 技術・ハウツー | 未着手 |  | 重複予定（実体は 0-6）。README だけ置く |
| 2-2 | Projectsの概要 | 7 | 技術・ハウツー | 未着手 |  | 動画のみで本文が薄い可能性 |
| 2-3 | [Skillsを使ってClaudeにあなたの仕事の進め方を教える](step2_tools/01_academy-tutorials/03_teach-claude-your-way-of-working-using-skills/README.md) | － | 技術・ハウツー | 完了 |  | M1 の実例。本文に分数なし（学習メモの目安は 11） |

## ステップ 3：職種で習熟（`step3_roles/`）

| ID | ページ | 分 | 種類 | 状態 | 学習済みの日 | 備考 |
|---|---|---|---|---|---|---|
| 3-01-01 | マーケティングの役割ページ | － | 学習・ビジネス | 未着手 |  | Chrome で読む。ボタンは押さない |
| 3-01-02 | マーケティング：キャンペーンブリーフ（★1） | 10 | 技術・ハウツー | 未着手 |  |  |
| 3-01-03 | マーケティング：ブランドに沿ったコンテンツ（★2） | 10 | 技術・ハウツー | 未着手 |  |  |
| 3-01-04 | マーケティング：チャネル横断で再利用（★3） | 10 | 技術・ハウツー | 未着手 |  |  |
| 3-02-01 | 営業の役割ページ | － | 学習・ビジネス | 未着手 |  | Chrome で読む。ボタンは押さない |
| 3-02-02 | 営業：アカウントリサーチ（★1） | 10 | 技術・ハウツー | 未着手 |  |  |
| 3-02-03 | 営業：商談準備（★2） | 10 | 技術・ハウツー | 未着手 |  |  |
| 3-02-04 | 営業：通話記録テーマ抽出（★3） | 10 | 技術・ハウツー | 未着手 |  |  |
| 3-03-01 | オペレーションの役割ページ | － | 学習・ビジネス | 未着手 |  | Chrome で読む。ボタンは押さない |
| 3-03-02 | オペレーション：ワークフロー改善プランナー（★1） | 16 | 技術・ハウツー | 未着手 |  |  |
| 3-03-03 | オペレーション：ベンダー交渉の準備（★2） | 10 | 技術・ハウツー | 未着手 |  |  |
| 3-03-04 | オペレーション：監査向けの文書準備（★3） | 14 | 技術・ハウツー | 未着手 |  |  |
| 3-04-01 | 人事の役割ページ | － | 学習・ビジネス | 未着手 |  | Chrome で読む。ボタンは押さない |
| 3-04-02 | 人事：オンボーディングガイド（★1） | 15 | 技術・ハウツー | 未着手 |  |  |
| 3-04-03 | 人事：新ポジション開設（★2） | 10 | 技術・ハウツー | 未着手 |  |  |
| 3-04-04 | 人事：サーベイからアクションプラン（★3） | 11 | 技術・ハウツー | 未着手 |  |  |
| 3-05-01 | プロダクトの役割ページ | － | 学習・ビジネス | 未着手 |  | Chrome で読む。ボタンは押さない |
| 3-05-02 | プロダクト：PRD 作成（★1） | 6 | 技術・ハウツー | 未着手 |  |  |
| 3-05-03 | プロダクト：フィードバック統合（★2） | 10 | 技術・ハウツー | 未着手 |  |  |
| 3-05-04 | プロダクト：メトリクスのナラティブ化（★3） | 10 | 技術・ハウツー | 未着手 |  |  |
| 3-06-01 | デザインの役割ページ | － | 学習・ビジネス | 未着手 |  | Chrome で読む。ボタンは押さない |
| 3-06-02 | デザイン：ブランドアセット（★1） | 13 | 技術・ハウツー | 未着手 |  |  |
| 3-06-03 | デザイン：デザイン仕様書（★2） | 12 | 技術・ハウツー | 未着手 |  |  |
| 3-06-04 | デザイン：インタビュー統合（★3） | 12 | 技術・ハウツー | 未着手 |  |  |
| 3-07-01 | 財務の役割ページ | － | 学習・ビジネス | 未着手 |  | Chrome で読む。ボタンは押さない |
| 3-07-02 | 財務：差異を説明（★1） | 12 | 技術・ハウツー | 未着手 |  |  |
| 3-07-03 | 財務：ビジネスの財務を整理（★2） | 13 | 技術・ハウツー | 未着手 |  |  |
| 3-07-04 | 財務：差異から経営層向けスライド（★3） | 10 | 技術・ハウツー | 未着手 |  |  |
| 3-08-01 | 法務の役割ページ | － | 学習・ビジネス | 未着手 |  | Chrome で読む。ボタンは押さない |
| 3-08-02 | 法務：法律リサーチ（★1） | 10 | 技術・ハウツー | 未着手 |  |  |
| 3-08-03 | 法務：規制とコンプライアンス（★2） | 11 | 技術・ハウツー | 未着手 |  |  |
| 3-08-04 | 法務：Projects で法務ワークフロー整理（★3） | 16 | 技術・ハウツー | 未着手 |  |  |
| 3-09-01 | 研究の役割ページ | － | 学習・ビジネス | 未着手 |  | Chrome で読む。ボタンは押さない |
| 3-09-02 | 研究：文献レビュー計画（★1） | 15 | 技術・ハウツー | 未着手 |  |  |
| 3-09-03 | 研究：生データから統計を検証（★2） | 16 | 技術・ハウツー | 未着手 |  |  |
| 3-09-04 | 研究：助成金の選択肢（★3） | 14 | 技術・ハウツー | 未着手 |  |  |
| 3-10-01 | エンジニアリングの役割ページ | － | 学習・ビジネス | 未着手 |  | Chrome で読む。ボタンは押さない |
| 3-10-02 | エンジニアリング：設計書（RFC）（★1） | 10 | 技術・ハウツー | 未着手 |  |  |
| 3-10-03 | エンジニアリング：ポストモーテム（★2） | 10 | 技術・ハウツー | 未着手 |  |  |
| 3-10-04 | エンジニアリング：オンコール引き継ぎ（★3） | 10 | 技術・ハウツー | 未着手 |  |  |
| 3-11-01 | データの役割ページ | － | 学習・ビジネス | 未着手 |  | Chrome で読む。ボタンは押さない |
| 3-11-02 | データ：アドホックなデータ質問に答える（★1） | 10 | 技術・ハウツー | 未着手 |  |  |

## ステップ 4：発展（`step4_advanced/`）

| ID | ページ | 分 | 種類 | 状態 | 学習済みの日 | 備考 |
|---|---|---|---|---|---|---|
| 4-1 | AI Fluency: Framework and foundations | 240 | 学習・ビジネス | 未着手 |  | コースのトップだけ（4 時間・14 レッスン） |
| 4-2 | AI capabilities and limitations | 210 | 学習・ビジネス | 未着手 |  | コースのトップだけ（3.5 時間・13 レッスン） |
| 4-3 | Introduction to Claude Cowork | 150 | 学習・ビジネス | 未着手 |  | 有料機能を含む。プラン条件を照合する |
| 4-4 | Claude for personal use（コレクション） | － | 学習・ビジネス | 未着手 |  | 日本語版なし。英語版を取り、解説は日本語で書く |
| 4-5 | Claude for work（コレクション） | － | 学習・ビジネス | 未着手 |  | 日本語版なし |

## ステップ 9：追加（台帳の対象外で、URL を渡して作ったもの）（`step9_added/`）

| ID | ページ | 分 | 種類 | 状態 | 学習済みの日 | 備考 |
|---|---|---|---|---|---|---|
| 9-add-072 | [creating-your-first-skill](step9_added/01_added/01_creating-your-first-skill/README.md) | － | 技術・ハウツー | 薄いページ |  | 本文 138 字（ナビとフッターを除く。動画のみ）。薄いページのため、解説は作らない |
| 9-add-073 | [configuration-and-multi-file-skills](step9_added/01_added/03_configuration-and-multi-file-skills/README.md) | － | 技術・ハウツー | 完了 |  | 本文 380 字（ナビを除く。訂正の注記を含む）。動画が中心。【本文が短い】 |
