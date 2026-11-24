# 学習メモ 索引（Claude Academy）

> このファイルは `tools/build_index.py` が `ledger.csv` から作る。手で直さない（直すなら `ledger.csv`）。

## 状態の数（全 73 ページ）

| 状態 | 件数 |
|---|---|
| 未着手 | 0 |
| 取得済 | 0 |
| 作成中 | 23 |
| 完了 | 42 |
| 薄いページ | 5 |
| 重複 | 1 |
| 失敗 | 1 |
| 要確認 | 1 |

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
| 1-15 | [修了バッジ](step1_basics/01_academy-courses-claude-101/15_badge/README.md) | － | 学習・ビジネス | 失敗 |  | 取得できない: REASON=JS_RENDERED |

## ステップ 2：道具を整える（`step2_tools/`）

| ID | ページ | 分 | 種類 | 状態 | 学習済みの日 | 備考 |
|---|---|---|---|---|---|---|
| 2-1 | [Claudeをカスタマイズする](step2_tools/01_academy-tutorials/01_customize-claude-cowork/README.md) | 7 | 技術・ハウツー | 重複 |  | 0-6 と同じページ（実体は 0-6）。解説は作らない |
| 2-2 | [Projectsの概要](step2_tools/01_academy-tutorials/02_intro-to-projects/README.md) | 7 | 技術・ハウツー | 薄いページ |  | 本文 111 字（薄いページ。解説は作らない） |
| 2-3 | [Skillsを使ってClaudeにあなたの仕事の進め方を教える](step2_tools/01_academy-tutorials/03_teach-claude-your-way-of-working-using-skills/README.md) | － | 技術・ハウツー | 完了 |  | M1 の実例。本文に分数なし（学習メモの目安は 11） |

## ステップ 3：職種で習熟（`step3_roles/`）

| ID | ページ | 分 | 種類 | 状態 | 学習済みの日 | 備考 |
|---|---|---|---|---|---|---|
| 3-01-01 | [マーケティングの役割ページ](step3_roles/01_marketing/01_roles-marketing/README.md) | － | 学習・ビジネス | 作成中 |  | 本文 1053 字（解説はこれから作る。Chrome で読んだ原本） |
| 3-01-02 | [マーケティング：キャンペーンブリーフ（★1）](step3_roles/01_marketing/02_campaign-brief/README.md) | 10 | 技術・ハウツー | 完了 |  | 本文 1972 字（解説はこれから作る） |
| 3-01-03 | [マーケティング：ブランドに沿ったコンテンツ（★2）](step3_roles/01_marketing/03_on-brand-content/README.md) | 10 | 技術・ハウツー | 完了 |  | 本文 1716 字（解説はこれから作る） |
| 3-01-04 | [マーケティング：チャネル横断で再利用（★3）](step3_roles/01_marketing/04_repurpose-content/README.md) | 10 | 技術・ハウツー | 完了 |  | 本文 1613 字（解説はこれから作る） |
| 3-02-01 | [営業の役割ページ](step3_roles/02_sales/01_roles-sales/README.md) | － | 学習・ビジネス | 作成中 |  | 本文 834 字（解説はこれから作る。Chrome で読んだ原本） |
| 3-02-02 | [営業：アカウントリサーチ（★1）](step3_roles/02_sales/02_account-research-brief/README.md) | 10 | 技術・ハウツー | 完了 |  | 本文 2026 字（解説はこれから作る） |
| 3-02-03 | [営業：商談準備（★2）](step3_roles/02_sales/03_call-prep-sheet/README.md) | 10 | 技術・ハウツー | 完了 |  | 本文 1943 字（解説はこれから作る） |
| 3-02-04 | [営業：通話記録テーマ抽出（★3）](step3_roles/02_sales/04_transcript-themes/README.md) | 10 | 技術・ハウツー | 完了 |  | 本文 1806 字（解説はこれから作る） |
| 3-03-01 | [オペレーションの役割ページ](step3_roles/03_operations/01_roles-operations/README.md) | － | 学習・ビジネス | 作成中 |  | 本文 702 字（解説はこれから作る。Chrome で読んだ原本） |
| 3-03-02 | [オペレーション：ワークフロー改善プランナー（★1）](step3_roles/03_operations/02_workflow-improvement-planner/README.md) | 16 | 技術・ハウツー | 完了 |  | 本文 3013 字（解説はこれから作る） |
| 3-03-03 | [オペレーション：ベンダー交渉の準備（★2）](step3_roles/03_operations/03_vendor-negotiation/README.md) | 10 | 技術・ハウツー | 完了 |  | 本文 1543 字（解説はこれから作る） |
| 3-03-04 | [オペレーション：監査向けの文書準備（★3）](step3_roles/03_operations/04_prep-scattered-documents-for-a-compliance-audit/README.md) | 14 | 技術・ハウツー | 完了 |  | 本文 2205 字（解説はこれから作る） |
| 3-04-01 | [人事の役割ページ](step3_roles/04_hr/01_roles-hr/README.md) | － | 学習・ビジネス | 作成中 |  | 本文 544 字（解説はこれから作る。Chrome で読んだ原本） |
| 3-04-02 | [人事：オンボーディングガイド（★1）](step3_roles/04_hr/02_create-new-hire-onboarding-guides/README.md) | 15 | 技術・ハウツー | 完了 |  | 本文 2789 字（解説はこれから作る） |
| 3-04-03 | [人事：新ポジション開設（★2）](step3_roles/04_hr/03_open-new-role/README.md) | 10 | 技術・ハウツー | 完了 |  | 本文 1792 字（解説はこれから作る） |
| 3-04-04 | [人事：サーベイからアクションプラン（★3）](step3_roles/04_hr/04_engagement-survey-themes/README.md) | 11 | 技術・ハウツー | 完了 |  | 本文 1825 字（解説はこれから作る） |
| 3-05-01 | [プロダクトの役割ページ](step3_roles/05_product/01_roles-product/README.md) | － | 学習・ビジネス | 作成中 |  | 本文 794 字（解説はこれから作る。Chrome で読んだ原本） |
| 3-05-02 | [プロダクト：PRD 作成（★1）](step3_roles/05_product/02_prd-from-a-one-pager/README.md) | 6 | 技術・ハウツー | 完了 |  | 本文 1551 字（解説はこれから作る） |
| 3-05-03 | [プロダクト：フィードバック統合（★2）](step3_roles/05_product/03_feedback-synthesis/README.md) | 10 | 技術・ハウツー | 完了 |  | 本文 1870 字（解説はこれから作る） |
| 3-05-04 | [プロダクト：メトリクスのナラティブ化（★3）](step3_roles/05_product/04_metrics-narrative/README.md) | 10 | 技術・ハウツー | 完了 |  | 本文 1775 字（解説はこれから作る） |
| 3-06-01 | [デザインの役割ページ](step3_roles/06_design/01_roles-design/README.md) | － | 学習・ビジネス | 作成中 |  | 本文 854 字（解説はこれから作る。Chrome で読んだ原本） |
| 3-06-02 | [デザイン：ブランドアセット（★1）](step3_roles/06_design/02_create-brand-assets/README.md) | 13 | 技術・ハウツー | 完了 |  | 本文 3048 字（解説はこれから作る） |
| 3-06-03 | [デザイン：デザイン仕様書（★2）](step3_roles/06_design/03_design-spec-from-threads/README.md) | 12 | 技術・ハウツー | 完了 |  | 本文 1743 字（解説はこれから作る） |
| 3-06-04 | [デザイン：インタビュー統合（★3）](step3_roles/06_design/04_uxr-synthesis/README.md) | 12 | 技術・ハウツー | 作成中 |  | 本文 1747 字（解説はこれから作る） |
| 3-07-01 | [財務の役割ページ](step3_roles/07_finance/01_roles-finance/README.md) | － | 学習・ビジネス | 作成中 |  | 本文 1399 字（解説はこれから作る。Chrome で読んだ原本） |
| 3-07-02 | [財務：差異を説明（★1）](step3_roles/07_finance/02_explain-a-variance/README.md) | 12 | 技術・ハウツー | 完了 |  | 本文 1677 字（解説はこれから作る） |
| 3-07-03 | [財務：ビジネスの財務を整理（★2）](step3_roles/07_finance/03_organize-your-business-finances/README.md) | 13 | 技術・ハウツー | 要確認 |  | 本文 2188 字（解説はこれから作る） |
| 3-07-04 | [財務：差異から経営層向けスライド（★3）](step3_roles/07_finance/04_variance-exec-slides/README.md) | 10 | 技術・ハウツー | 作成中 |  | 本文 1606 字（解説はこれから作る） |
| 3-08-01 | [法務の役割ページ](step3_roles/08_legal/01_roles-legal/README.md) | － | 学習・ビジネス | 作成中 |  | 本文 761 字（解説はこれから作る。Chrome で読んだ原本） |
| 3-08-02 | [法務：法律リサーチ（★1）](step3_roles/08_legal/02_legal-research-memo/README.md) | 10 | 技術・ハウツー | 作成中 |  | 本文 2097 字（解説はこれから作る） |
| 3-08-03 | [法務：規制とコンプライアンス（★2）](step3_roles/08_legal/03_regulatory-analysis/README.md) | 11 | 技術・ハウツー | 作成中 |  | 本文 2113 字（解説はこれから作る） |
| 3-08-04 | [法務：Projects で法務ワークフロー整理（★3）](step3_roles/08_legal/04_organize-your-legal-workflows-using-projects/README.md) | 16 | 技術・ハウツー | 作成中 |  | 本文 3479 字（解説はこれから作る） |
| 3-09-01 | [研究の役割ページ](step3_roles/09_research/01_roles-research/README.md) | － | 学習・ビジネス | 作成中 |  | 本文 928 字（解説はこれから作る。Chrome で読んだ原本） |
| 3-09-02 | [研究：文献レビュー計画（★1）](step3_roles/09_research/02_plan-your-literature-review/README.md) | 15 | 技術・ハウツー | 作成中 |  | 本文 2685 字（解説はこれから作る） |
| 3-09-03 | [研究：生データから統計を検証（★2）](step3_roles/09_research/03_verify-statistics-from-raw-data/README.md) | 16 | 技術・ハウツー | 作成中 |  | 本文 2956 字（解説はこれから作る） |
| 3-09-04 | [研究：助成金の選択肢（★3）](step3_roles/09_research/04_work-through-grant-options-in-chat-with-claude/README.md) | 14 | 技術・ハウツー | 作成中 |  | 本文 1797 字（解説はこれから作る） |
| 3-10-01 | [エンジニアリングの役割ページ](step3_roles/10_engineering/01_roles-engineering/README.md) | － | 学習・ビジネス | 作成中 |  | 本文 794 字（解説はこれから作る。Chrome で読んだ原本） |
| 3-10-02 | [エンジニアリング：設計書（RFC）（★1）](step3_roles/10_engineering/02_design-doc/README.md) | 10 | 技術・ハウツー | 作成中 |  | 本文 1822 字（解説はこれから作る） |
| 3-10-03 | [エンジニアリング：ポストモーテム（★2）](step3_roles/10_engineering/03_incident-postmortem/README.md) | 10 | 技術・ハウツー | 作成中 |  | 本文 1668 字（解説はこれから作る） |
| 3-10-04 | [エンジニアリング：オンコール引き継ぎ（★3）](step3_roles/10_engineering/04_oncall-handoff-brief/README.md) | 10 | 技術・ハウツー | 作成中 |  | 本文 1745 字（解説はこれから作る） |
| 3-11-01 | [データの役割ページ](step3_roles/11_data/01_roles-data/README.md) | － | 学習・ビジネス | 作成中 |  | 本文 425 字（解説はこれから作る。Chrome で読んだ原本） |
| 3-11-02 | [データ：アドホックなデータ質問に答える（★1）](step3_roles/11_data/02_answer-the-adhoc/README.md) | 10 | 技術・ハウツー | 作成中 |  | 本文 1885 字（解説はこれから作る） |

## ステップ 4：発展（`step4_advanced/`）

| ID | ページ | 分 | 種類 | 状態 | 学習済みの日 | 備考 |
|---|---|---|---|---|---|---|
| 4-1 | [AI Fluency: Framework and foundations](step4_advanced/01_academy-courses/01_ai-fluency-framework-foundations/README.md) | 240 | 学習・ビジネス | 完了 |  | 本文 2051 字（解説はこれから作る） |
| 4-2 | [AI capabilities and limitations](step4_advanced/01_academy-courses/02_ai-capabilities-and-limitations/README.md) | 210 | 学習・ビジネス | 完了 |  | 本文 1314 字（解説はこれから作る） |
| 4-3 | [Introduction to Claude Cowork](step4_advanced/01_academy-courses/03_introduction-to-claude-cowork/README.md) | 150 | 学習・ビジネス | 完了 |  | 本文 313 字（解説はこれから作る） |
| 4-4 | [Claude for personal use（コレクション）](step4_advanced/02_academy-collections/01_claude-for-you/README.md) | － | 学習・ビジネス | 薄いページ |  | 本文 182 字（薄いページ。解説は作らない） |
| 4-5 | [Claude for work（コレクション）](step4_advanced/02_academy-collections/02_claude-for-work/README.md) | － | 学習・ビジネス | 薄いページ |  | 本文 180 字（薄いページ。解説は作らない） |

## ステップ 9：追加（台帳の対象外で、URL を渡して作ったもの）（`step9_added/`）

| ID | ページ | 分 | 種類 | 状態 | 学習済みの日 | 備考 |
|---|---|---|---|---|---|---|
| 9-add-072 | [creating-your-first-skill](step9_added/01_added/01_creating-your-first-skill/README.md) | － | 技術・ハウツー | 薄いページ |  | 本文 138 字（ナビとフッターを除く。動画のみ）。薄いページのため、解説は作らない |
| 9-add-073 | [configuration-and-multi-file-skills](step9_added/01_added/03_configuration-and-multi-file-skills/README.md) | － | 技術・ハウツー | 完了 |  | 本文 380 字（ナビを除く。訂正の注記を含む）。動画が中心。【本文が短い】 |
