###### [toTopPage](./README.md)
###### [toREADME](./README.md)
# 本文：(無題)
- `title`: (無題)
- `url`: https://academy.claude.com/ja/use-cases/feedback-synthesis
- `source_format`: html
- `retrieved_at`: 2026-11-24T09:49:47+09:00
- 解説の入口：[README.md](./README.md)

> 要約：Product Managementプラグインの/synthesize-researchを出発点に、Cowork（Slack・Linear・Google Driveと連携）で顧客フィードバックを5〜7テーマに整理し、1ページのVoice of Customerブリーフを作る手順と、スキル化・毎週金曜の定期実行までを説明する記事。

-----
[toTop](#totoppage)

<!-- source-body:start -->
Product Managementプラグインには、出発点として`/synthesize-research`やその他のディスカバリースキルが同梱されており、生の信号をテーマにクラスタリングしてランク付けするようにすでに構成されています。管理者がプラグインを管理していてまだ利用できない場合は、これをスキップしてください。以下の内容はこれを必要としません。

Claude Coworkは、お使いのシステムと直接連携することでより強力になります。権限とアクセスはあなたが管理します。[ツールアクセスについて学ぶ（新しいタブで開きます）](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access)。

設定するには、Coworkで**Customize → Connectors**に移動してください。

[接続](https://claude.ai/desktop/directory/slack)

[接続](https://claude.ai/desktop/directory/linear)

[接続](https://claude.ai/desktop/directory/google-drive-drivemcp)

使用するファイル（NPSの逐語エクスポート、サポートチケットのCSV、セールスコールの抜粋、6件のインタビュー記録）をマシン上の1つのフォルダにドラッグし、Coworkにそのフォルダを指定してください。Coworkはそこから読み込み、Voice of Customerブリーフをそこに書き戻します。これを四半期ごとに実行する場合は、そのフォルダから[Coworkプロジェクトを作成（新しいタブで開きます）](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)すると、ソース、指示、メモリが紐付いたままになります。

このフォルダと#product-feedback Slackチャンネル、feedbackタグが付いた未解決のZendeskチケットを読み込んでください。すべてを5〜7のテーマにクラスタリングし、それぞれの出現頻度と深刻度を数え、各テーマの最良の引用を抜き出し、Linearのロードマップ項目に対応するものと新規のものをフラグ付けし、ロードマップレビュー用の1ページのVoice of Customerブリーフを作成してください。

**数の範囲を指定する。** 「5〜7のテーマ」と指定することで、40行のタグリストではなく本当のクラスタリングが強制され、ブリーフが1ページに収まり、ロードマップの議論が最重要な信号に集中します。

**頻度と深刻度を求める。** 両方を指定することでClaudeにランキング基準を伝えられるため、単に出現頻度だけでなく、プランニングにとって重要な順にテーマが返ってきます。

**最良の一例を求める。** ロードマップレビューでは、証拠の山よりも最良の一つの引用の方が効果的です。Coworkは最も強力な一文を選び、残りをその下にリンクします。

**既存の計画と比較する。** 「Linearのロードマップ項目に対応するものと新規のもの」を指定することで、ブリーフは「計画済みの検証」と「見落としていたもの」にすでに分かれた状態で届きます。

**参考例を追加する。** 気に入っている例をフォルダに入れておくと、Coworkがその構成とトーンに合わせます。

**不確実な点をフラグするよう依頼する。** 「確信が持てない点があればフラグを付けてください」と追加すると、ドラフトをレビューする際に最初に確認すべき箇所がわかります。

プラグインのスキルは出発点です — 自分自身のプラクティスと専門知識でカスタマイズしましょう。数分の対話を行えば、それ以降は自分の基準で実行されるようになります。

このタスクでこれまで行ったことをスキルにしてください。あるいは、私のフィードバックを反映して/synthesize-researchスキルを編集してください。

フィードバックは、誰かが読んでいるかどうかに関わらず、プランニングサイクルの間に積み重なっていきます。プロンプトに`/schedule`と入力するか、Coworkのサイドバーで**Scheduled**を開くと、カスタマイズされたスキルが各ロードマップレビューの前の金曜日に新しいブリーフを作成します。

**/schedule** 毎週金曜日の午後4時に、Product/voc-\<current-quarter>とライブのSlackおよびZendeskソースに対して/synthesize-researchを実行し、そのフォルダにvoc-brief-\<date>.mdとしてブリーフを書き出してください。

カスタマイズされた`/synthesize-research`には、あなたの深刻度スケール、常設のソース、ブリーフの形式が組み込まれています。これを共有することで、チームのすべてのPMが同じ方法でフィードバックをクラスタリングでき、どの担当領域であってもロードマップレビューは一貫したVoCページを読むことになります。
