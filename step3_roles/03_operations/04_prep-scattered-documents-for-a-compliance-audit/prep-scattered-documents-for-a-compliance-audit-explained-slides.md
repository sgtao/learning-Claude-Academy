---
title: 散らばった監査文書を Cowork で整える
palette: ocean
---
<!-- slide: title -->
# 散らばった監査文書を<br>==Cowork== で整える
subtitle: フォルダを渡して、分類・名前の変更案・不足の指摘まで任せる方法
badges: [Claude Academy, Cowork, SOC 2 監査]
note: 元ページ「文書インベントリ」の解説メモ（README・解説メモ・FAQ）に基づく。Web 検索は行っていない。
---
<!-- slide: points -->
## 状況：100件以上の文書が散らばっている
lead: SOC 2 監査の前に、あいまいな名前の文書を整理したい
- **文書の状態**：100件以上が、scan0042.pdf のようなあいまいな名前で散在している
- **期限**：監査担当者が来る前に整理する必要がある
- **監査範囲**：セキュリティ、可用性、機密性
- **対象期間**：2024年1月から12月
- **出典**：[Claude Academy の元ページ](https://academy.claude.com/ja/use-cases/prep-scattered-documents-for-a-compliance-audit)（取得：2026-11-24）
point: 文書の名前ではなく、中身を読んで整理する
---
<!-- slide: steps -->
badge: HOW
## 始め方は、==4つの動き==
lead: Claude Desktop の Cowork で、フォルダを指定して依頼する
```steps
style: cards
items:
  - icon: "💻"
    title: Cowork を開始
    desc: Claude Desktop をダウンロードし、Cowork セッションを始める
  - icon: "📁"
    title: フォルダを選ぶ
    desc: チャットバーで「フォルダで作業する」を選ぶ。個別のファイルは + ボタンで追加
  - icon: "✍️"
    title: 範囲を伝える
    desc: 監査範囲や管理フレームワークを含めて依頼する
  - icon: "💬"
    title: 質問とプランを見る
    desc: Claude が範囲や要件を質問し、サイドバーにプランを出すことがある
    tone: outline
```
point: プロンプトに必要なのは、監査フレームワークと範囲だけ
note: 4つ目は「想定される流れ」で、必ず起きるとは書かれていない。
---
<!-- slide: points -->
## 依頼は、==3点セット==
lead: 範囲を伝えたうえで、次の3つを頼む
- **名前の変更**：文書の種類、発効日、対象となる管理領域が分かるタイトルにする
- **グループ化**：管理カテゴリ別にまとめる（アクセス制御、変更管理、インシデント対応など）
- **不足のフラグ**：文書が足りなさそうな管理領域に印を付ける
point: 事前のリネームや整理は不要。Claude が各ファイルを読んで理解する
note: 処理中、利用者は他の作業に取り組める。
---
<!-- slide: chart-donut -->
## 確認結果：156件の内訳
lead: 記事の例で、フォルダ内の全文書を確認した結果
```chart
type: donut
title: 文書の種類別の件数（合計156件）
unit: 件
data:
  - { label: 証拠およびログ, value: 67 }
  - { label: 手順書, value: 31 }
  - { label: ポリシー, value: 24 }
  - { label: 契約書および合意書, value: 18 }
  - { label: トレーニング記録, value: 16 }
source: { name: Claude Academy「文書インベントリ」の例（取得 2026-11-24）, url: https://academy.claude.com/ja/use-cases/prep-scattered-documents-for-a-compliance-audit }
```
note: 5つの件数を足すと156件になる。
---
<!-- slide: chart-bar, layout: side-list -->
## 領域別：どこが厚く、どこが薄いか
lead: 管理領域ごとの文書の件数（記事の例）
```chart
type: bar
title: 管理領域別の文書件数
unit: 件
data:
  - { label: アクセス制御, value: 28 }
  - { label: 変更管理, value: 22 }
  - { label: ベンダー管理, value: 18 }
  - { label: インシデント対応, value: 8 }
  - { label: データバックアップと復旧, value: 6 }
source: { name: Claude Academy「文書インベントリ」の例（取得 2026-11-24）, url: https://academy.claude.com/ja/use-cases/prep-scattered-documents-for-a-compliance-audit }
```
### 見方
- **十分にカバー**：アクセス制御、変更管理、ベンダー管理
- **注意が必要な可能性**：インシデント対応、データバックアップと復旧
- 件数が少ない＝不備、とは断定していない
note: 5領域の件数の合計は82で、総数の156とは一致しない。一覧にある領域だけの件数と思われるが、記事からは決められない（推測）。
---
<!-- slide: table -->
## 不足として指摘された==3点==
lead: 件数の少ない領域は、証拠の不足として具体化される
| 領域 | 指摘された不足 |
|---|---|
| インシデント対応 | テストやテーブルトップ演習の証拠がない |
| バックアップと復旧 | 復元テストの証拠がない |
| 事業継続 | インベントリに含まれていない |
point: 最後に「再編成を進めてもよろしいですか？」と確認が入る
note: 名前の変更などは、人が承認してから進む流れになっている。
---
<!-- slide: points -->
## その先の使い方と、データの扱い
lead: 結果をファイルにしたり、Web ツールの情報も読ませたりできる
- **マトリクス**：管理ID、説明、証拠文書、カバレッジ状況の列を持つ Excel を、フォルダに直接作らせる
- **Web ツール**：Jira などにある変更管理の証拠を、Chrome 版 Claude 経由で読み取る（例：過去6か月分の変更リクエスト）
- **参照資料**：ポリシーごとに、対象範囲、最終更新日、主要要件2〜3つを1ページにまとめる
- **データの扱い**：文書は手元に残るが、読み取った内容は Anthropic のサーバーで処理される
- **始め方のコツ**：「整理待ち」のフォルダから。管理マトリクスなどがあればフォルダに入れる
point: （補足）組織のルールを確かめてから、出してよい文書で試す
note: 最後の一文は解説メモの補足であり、元ページの文ではない。
---
<!-- slide: summary, layout: compact -->
## まとめ
1. **範囲を伝えて任せる**：監査フレームワークと範囲だけで、全ファイルの分類が始まる
2. **件数から読み、不足を確かめる**：少ない領域を見つけ、証拠の不足を具体的に確認する
3. **承認してから再編成する**：名前の変更の前に、人が確認する
> 次の一歩：自分の「整理待ち」フォルダを1つ選び、監査フレームワークと範囲を一文ずつ書いてみる。
---
<!-- slide: sources -->
## 出典・参考リンク
- [元ページ（Claude Academy）](https://academy.claude.com/ja/use-cases/prep-scattered-documents-for-a-compliance-audit) — 文書インベントリ（取得 2026-11-24）
- [Cowork と Chat の選び方](https://academy.claude.com/ja/tutorials/choosing-between-claude-cowork-or-chat) — 元ページ内のリンク
- [Claude Desktop のダウンロード](https://claude.com/download) — 元ページ内のリンク
note: 数値はすべて元ページの例示結果。解説メモ（README・02_explanation_memo.md・11_question_and_answer.md）をもとに作成した。
