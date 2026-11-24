###### [toTopPage](./README.md)
###### [toREADME](./README.md)
# 本文：設定とマルチファイルSkills
- `title`: 設定とマルチファイルSkills
- `url`: https://academy.claude.com/ja/tutorials/configuration-and-multi-file-skills
- `source_format`: html
- `retrieved_at`: 2026-11-24T07:47:25+09:00
- 解説の入口：[README.md](./README.md)

> 要約：Claude Code で skills を設定する方法と、複数ファイルからなる skill の構造の扱い方を学ぶ動画のページ。本文は 1 文の説明と、動画の訂正の注記だけ。

-----
[toTop](#totoppage)

<!-- source-body:start -->
[Claude Academy](https://academy.claude.com/ja)

探索[ウェビナー](https://academy.claude.com/webinars)



読み込み中



1. [Academy](https://academy.claude.com/ja)
2. /[チュートリアル](https://academy.claude.com/ja/tutorials)

[チュートリアル](https://academy.claude.com/ja/tutorials)

# 設定とマルチファイルSkills

Claude Codeでのskillsの設定方法と、マルチファイルのskill構造の扱い方を学びます。

4 分Claude Code

視聴

![](https://academy.claude.com/assets/v1/thumbnail.light-ctra72zy.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-ktlv28wr.png)

読み込み中



訂正

0:40、1:20、3:35で、動画では`allowed-tools`がClaudeの使用できるツールを制限すると述べていますが、これは誤りです。実際には、リストしたツールを事前承認するものであり、次のメッセージを送るまでの間、Claudeは確認を求めずにそれらを使用できるようになります。Claudeは、通常の権限設定のもとで、他のツールも引き続き使用できます。skillが有効な間にツールを取り除くには、`disallowed-tools`を使用してください。[skillのためにツールを事前承認する（新しいタブで開きます）](https://code.claude.com/docs/en/skills#pre-approve-tools-for-a-skill)を参照してください。

## AIについて学ぶ

* [AI 活用力](https://academy.claude.com/collections/ai-fluency)
* [AIの仕組み](https://academy.claude.com/collections/how-ai-works)
* [AIとの協働](https://academy.claude.com/collections/collaborating-with-ai)
* [人間とAIエージェントのチーム構築](https://academy.claude.com/collections/human-agent-teams)
* [Claude で構築](https://academy.claude.com/collections/build-with-claude)

## 対象者別

* [仕事でのClaude活用](https://academy.claude.com/collections/claude-for-work)
* [個人利用向けClaude](https://academy.claude.com/collections/claude-for-you)
* [高等教育向け Claude](https://academy.claude.com/collections/higher-education)
* [K-12向けClaude](https://academy.claude.com/collections/k-12)
* [非営利団体向けClaude](https://academy.claude.com/collections/nonprofits)
* [中小企業向けClaude](https://academy.claude.com/collections/small-business)

## 種類別

* [すべてのリソース](https://academy.claude.com/ja/all)
* [コース](https://academy.claude.com/ja/courses)
* [チュートリアル](https://academy.claude.com/ja/tutorials)
* [ユースケース](https://academy.claude.com/ja/use-cases)
* [ウェビナー](https://academy.claude.com/webinars)

## 製品別

* [Claude](https://academy.claude.com/products/claude)
* [Claude Cowork](https://academy.claude.com/products/cowork)
* [Claude Code](https://academy.claude.com/products/code)
* [Claude Tag](https://academy.claude.com/products/tag)
* [Claude Platform](https://academy.claude.com/products/platform)

## ヘルプとドキュメント

* [よくある質問](https://academy.claude.com/help/faq)
* [ヘルプセンター （新しいタブで開きます）](https://support.claude.com)
* [開発者向けドキュメント （新しいタブで開きます）](https://code.claude.com/docs/en/overview)
* [開発者ブログ （新しいタブで開きます）](https://claude.dev)

© 2026 Anthropic PBC

* プライバシー設定
* [Privacy policy （新しいタブで開きます）](https://www.anthropic.com/legal/privacy)
* [Usage policy （新しいタブで開きます）](https://www.anthropic.com/legal/aup)

言語 日本語
