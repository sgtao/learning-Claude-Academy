---
title: 文献レビューの計画を Claude に手伝ってもらう
palette: ocean
purpose: self-study
---
<!-- slide: title -->
# 文献レビューの計画を==Claude と立てる==
subtitle: 問いを伝え、読む順番をつくり、最後は自分の目で確かめる
badges: [自己学習用, 初めて読む人向け, 解説メモにもとづく]
note: 出典は Claude Academy の記事（原本）と、それを解説した解説メモ（README・解説メモ・FAQ）だけです。Web 検索は行っていません。
---
<!-- slide: points -->
## 困りごとは「==読む量==」
lead: 重要な十数本を見つけるために、何百もの論文を読む必要がある
- **Claude が引き受ける**：データベースの検索、問いに照らした関連性の評価、調査結果の整理
- **自分が集中する**：機械的な仕分け作業ではなく、統合と独自の分析
- **原本の記事**：[Claude Academy「文献レビューの計画」](https://academy.claude.com/ja/use-cases/plan-your-literature-review)
point: 任せるのは「探して並べる」まで。「何が言えるか」は自分で決める
note: 原本は見出しの無い 1 本の記事です。冒頭の画像（Word 文書のロードマップ）は内容を読めておらず、根拠にしていません。
---
<!-- slide: steps -->
badge: 手順
## 使い方は、==5つの流れ==
lead: 原本の順に並べた手順
```steps
style: cards
items:
  - icon: "1"
    title: 問いを伝える
    desc: リサーチクエスチョンを Claude に伝える
  - icon: "2"
    title: 条件を頼む
    desc: 期間・データベース・成果物の形を指定する
  - icon: "3"
    title: PubMed を接続
    desc: 手元の論文だけでなく PubMed 全体を検索できる
  - icon: "4"
    title: ロードマップ受領
    desc: 優先順位つきの読書計画が Word 文書で届く
  - icon: "5"
    title: 読みながら整理
    desc: 論文を読み進めつつ調査結果を整理する
    tone: outline
```
point: 手順を自分のテーマに置き換えれば、そのまま再現できる
note: 3 の PubMed 接続は、原本ではプロンプトのあとに説明されています。
---
<!-- slide: points -->
## 最初のプロンプトに入れる==5つの要素==
lead: 原本の例は、腸脳相関と気分障害（うつ病と不安症）がテーマ
- **観点**：知りたいことを 3 つの箇条書きで（メカニズム／プロバイオティクスの臨床試験／炎症と神経伝達物質）
- **期間**：過去 5 年間
- **データベース**：PubMed
- **成果物**：何を最初に読むべきか優先順位をつけた、構造化されたリーディングガイド
- **見た目**：視覚的階層、研究タイプ別の色分け、メモ用スペースのある Word 文書
point: デザインの指定が無いと、Claude は標準的な書式を選ぶ
note: 5 つに分けたのは解説メモ側の整理です。原本は 1 つの文章として書いています。
---
<!-- slide: chart-donut -->
## 例の結果：==42本==の内訳
lead: Claude の回答例にある数字。12 + 18 + 12 = 42
```chart
type: donut
title: 回答例の論文 42 本の内訳（研究タイプ別）
unit: "本"
data:
  - { label: システマティックレビュー, value: 12 }
  - { label: RCT, value: 18 }
  - { label: メカニズム研究, value: 12 }
source: { name: Claude Academy 原本記事（回答例の数字）, url: https://academy.claude.com/ja/use-cases/plan-your-literature-review }
```
note: 回答例に載っている数字です。論文が実在するか、内容が正確かは本文からは確かめられません。
---
<!-- slide: steps -->
badge: 読書計画
## 3段階で、==基礎から批判的分析へ==
lead: 1 週目から 4 週目までの読む順番
```steps
style: cards
items:
  - icon: "1"
    title: 基礎論文（1週目）
    desc: 影響力の高いシステマティックレビューとメタ分析。理論的な枠組みをつくる
  - icon: "2"
    title: メカニズムとエビデンス（2〜3週目）
    desc: 仕組みを説明する研究と、最も強力な臨床試験
  - icon: "3"
    title: ギャップ分析（4週目）
    desc: 新興の研究や矛盾する知見で、批判的分析を強める
    tone: outline
```
point: まず全体像、次に中身、最後に穴探し
note: 並びの理由づけ「全体像から中身、穴探し」は解説メモ側の補足です。
---
<!-- slide: table -->
## 読みながら使う==3つの追加の質問==
lead: 気づきが出たら、そのまま Claude に確かめてもらう
| 種類 | 使う場面 | Claude に頼むこと |
|---|---|---|
| パターンの検証 | 「最近は X、以前は Y」のような傾向に気づいた | 全体で成り立つか確かめ、例外や矛盾の論文にフラグを立てる |
| 矛盾の分析 | 論文 A と論文 B が正反対のことを言っている | 矛盾の理由を分析し、解消の手がかりになる論文を探す |
| ギャップの補充 | 特定のメカニズム・対象集団・介入の穴に気づいた | PubMed で検索・評価し、ロードマップに追加して読む順番を示す |
point: 原本には、それぞれ穴埋め形式のプロンプト例がある
note: 穴埋め部分に自分のテーマを入れて使います。
---
<!-- slide: points -->
## 信じすぎない：==3つの注意点==
lead: Claude は証拠の追跡に優れているが、最終確認は自分で
- **引用**：主張の中心になる引用は、提出前に必ず元の論文と照らし合わせる。正確な文言は自分で検証する
- **プレビュー**：チャット内は基本的な構造だけ。Word 文書をダウンロードして開き、本来の形を確認する
- **デザイン**：指定が無いとデフォルトの書式になる
point: Claude で関連箇所を素早く見つけ、文言は自分の目で確かめる
note: Google Drive を接続すると、すでに読んだ論文を特定して、新しい知見をライブラリと並べて整理できます。
---
<!-- slide: summary -->
## まとめ
1. **任せる範囲を決める**：検索・評価・整理は Claude、統合と独自の分析は自分
2. **条件を具体的に伝える**：観点・期間・データベース・成果物・見た目
3. **読みながら確かめる**：パターンの検証・矛盾の分析・ギャップの補充
4. **最後は自分の目で**：中心となる引用は元の論文で再確認する
> 解説メモ：[README](./plan-your-literature-review_explained/README.md)・[解説メモ](./plan-your-literature-review_explained/02_explanation_memo.md)・[FAQ](./plan-your-literature-review_explained/11_question_and_answer.md)
---
<!-- slide: sources -->
## 出典・参考リンク
- [Claude Academy：文献レビューの計画（原本）](https://academy.claude.com/ja/use-cases/plan-your-literature-review) — 本スライドの元の記事
- [PubMed コネクタ（Claude ディレクトリ）](https://claude.ai/directory/pubmed) — 原本が案内している接続先
- [解説メモ（README）](./plan-your-literature-review_explained/README.md) — 本スライドの情報源。Web 検索は行っていません
note: 情報源は原本と解説メモだけです。
