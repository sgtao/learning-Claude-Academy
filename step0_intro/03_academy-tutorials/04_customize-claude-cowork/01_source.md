###### [toTopPage](../README.md)
###### [toREADME](./README.md)
# 本文：Claudeをカスタマイズする
- `title`: Claudeをカスタマイズする
- `url`: https://academy.claude.com/ja/tutorials/customize-claude-cowork
- `source_format`: html
- `retrieved_at`: 2026-11-15T16:51:28+09:00
- 解説の入口：[README.md](./README.md)

> 要約：コネクタ・指示・Skill・プラグインで、自分のシステムとチームのやり方を Claude に組み込み、以降のタスクをその状態から始められるようにする方法の説明。

-----
[toTop](#totoppage)
## セクション目次
- 1 : [プラグインの例](#プラグインの例)

-----
[toTop](#totoppage)

<!-- source-body:start -->
[Claude（新しいタブで開きます）](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) は、あなたのファイルやツール全体にわたって完全なタスクを実行します。一度カスタマイズしておけば、それ以降のすべてのタスクは、あなたのシステムが接続され、チームのプロセスがすでに組み込まれた状態でスタートします。クイックスタートについては、[3ステップで始める（新しいタブで開きます）](https://academy.claude.com/ja/tutorials/get-started-in-claude-cowork-in-three-steps)を参照してください。

[コネクタ（新しいタブで開きます）](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)は、Slack、[Salesforce（新しいタブで開きます）](https://claude.ai/desktop/directory/salesforce-headless-360)、Microsoft 365、Jira、社内独自のツールなど、すでにあなたの仕事が存在するシステムにClaudeを接続し、タスクを理解するためのコンテキストと、それを実行する能力をClaudeに与えます。コネクタを有効にすると、Claudeはあなたのデータを読み取る*だけでなく*、書き込みもできます：チケットの更新、返信の下書き作成、チャンネルへの投稿、ファイルの保存などです。

左サイドバーの**カスタマイズ**パネルからコネクタを有効にしてください。一度認証すれば、Claudeはその後どのセッションでもそのツールを使用できます。

指示とは、Claudeがどのように作業すべきかについてあなたが書く標準ルールです。トーン、書式、最初に確認すべきソース、従うべき規則などです。次の2つのレベルで設定できます：

**1. グローバル指示**はあなたが実行するすべてのタスクに適用されます。*設定の「グローバル指示」（アプリのバージョンによっては「Claudeへの指示」と呼ばれます）で編集します。*

**2. プロジェクト指示**は、そのプロジェクト内でのみ、グローバル指示に加えて適用されます。[プロジェクト（新しいタブで開きます）](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)の右パネルの「指示」で編集します。

**3. 組織の指示：** エンタープライズユーザーの場合、管理者が組織の設定を行うこともあります。これは、あなた自身の指示に加えて、あなたの会話、タスク、Codeの全体に適用される組織全体のガイダンスです。

指示はすべてのタスクに適用されます。これは、あなたが何に取り組んでいても関係なくClaudeが従う背景的なルールのようなものです。一方、Skillは特定の種類のタスク1つに対応するもので、関連するときだけ読み込まれ、チームメンバーと共有することもできます。一般的なルールは指示に、繰り返し行うプロセスはSkillに入れます。

[Skills（新しいタブで開きます）](https://support.claude.com/en/articles/12512176-what-are-skills)は、Claudeが特定のタスクを繰り返し可能な形で完了するための指示ファイルです。Skillsを使って、あなた個人のベストプラクティスやチームの専門知識を、繰り返し使える指示のセットとしてエンコードしましょう。

[Skillを使用する（新しいタブで開きます）](https://support.claude.com/en/articles/12512180-use-skills-in-claude)には、直接名前を指定する（`/skill-name`）か、タスクを平易な言葉で説明します。ClaudeはどのSkillが当てはまるかを認識し、読み込むことができます。

[Skillの作成（新しいタブで開きます）](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)も、プロンプト内でClaudeと一緒に行うことができます。普段通りにワークフローを一通り実行してください。作業の最後に、Claudeにこう頼みます：

組み込みのskill-creatorが手順、テンプレート、ソースの所在を記録するため、次回の実行はプロンプト1つで済みます。[Coworkで最初のSkillを作成する](claude://cowork/new?q=Walk%20me%20through%20creating%20my%20first%20Skill.%20Ask%20me%20about%20a%20task%20I%20repeat%20every%20week%2C%20then%20help%20me%20capture%20it.)。

[プラグイン（新しいタブで開きます）](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)は、コネクタとSkillsをまとめてバンドルすることで、チームメンバーがすぐに使い始められるようにします。

#### **プラグインの例**

Anthropicは、よくある職種向けにすぐ使えるプラグインを公開しています。それぞれ、その職種が頼りにするコネクタと、主要なワークフロー向けのSkillsがペアになっています：

- [**セールス**（新しいタブで開きます）](https://github.com/anthropics/knowledge-work-plugins/tree/main/sales) — HubSpot、Close、Clay、ZoomInfo、Fireflies（Slackも含む）、アカウント調査、商談準備、パイプラインレビュー、競合バトルカード向けのSkills。
- [**プロダクト**（新しいタブで開きます）](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management) — Atlassian（JiraとConfluence）、Linear、Notion、Slack、フィードバックのクラスタリング、PRD作成、スプリント更新、競合分析向けのSkills。
- [**リーガル**（新しいタブで開きます）](https://github.com/anthropics/knowledge-work-plugins/tree/main/legal) — Box、Egnyte、DocuSign、Slack、Atlassian、契約レビュー、NDAのトリアージ、署名リクエスト、ベンダーチェック向けのSkills。
- [**オペレーション**（新しいタブで開きます）](https://github.com/anthropics/knowledge-work-plugins/tree/main/operations) — Jira、Asana、Notion、ベンダーレビュー、プロセス文書化、変更リクエスト、キャパシティプランニング向けのSkills。

さらに多くの選択肢については、**カスタマイズ**サイドバーで利用可能なプラグインを閲覧するか、あなた自身のコネクタとSkillsをまとめたカスタムプラグインを作ってチームと共有するようClaudeに依頼してください。[自分の職種向けのプラグインをCoworkで閲覧する](claude://cowork/new?q=Show%20me%20the%20plugins%20available%20for%20my%20role%20and%20help%20me%20pick%20one%20to%20install.)。

多くの人は、まずコネクタと指示から始め、同じタスクを何度か実行した後にSkillを作成し、チームメンバーから「同じように設定するにはどうすればいいか」と聞かれたときにそれを共有するようになります。プラグインは、管理者が組織の標準セットを各職種に配布するための手段です。

セットアップが完了したら、以下の追加機能でさらに活用できます：

- **スケジュールされたタスク**は、あなたが接続したすべてのものにアクセスしながら、設定した時刻にプロンプトを実行します。つまり、あなたが書いたSkillを、あなたが起動しなくても毎週平日の午前9時に実行させることができます。どのセッションでもClaudeに頼めば設定できます。[スケジュールされたタスクについて詳しくはこちら（新しいタブで開きます）](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)。
- **Artifacts**は、セッションをまたいでサイドバーに残るダッシュボード、トラッカー、比較ビューです。いつでも開いて、コネクタからの最新データでClaudeに更新させることができます。[Artifactsについて詳しくはこちら（新しいタブで開きます）](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)。

Claudeとの作業についてさらに詳しく知るには：

- [Claude CoworkとChatのどちらを選ぶか（新しいタブで開きます）](https://academy.claude.com/ja/tutorials/choosing-between-claude-cowork-or-chat) — タスクを任せる価値があるときと、会話だけで十分なときの見極め方。
- [ゼロからプラグインを作る（新しいタブで開きます）](https://academy.claude.com/ja/tutorials/how-to-build-a-plugin-from-scratch-in-cowork) — マーケットプレイスに必要なものが無いときの対処法。
