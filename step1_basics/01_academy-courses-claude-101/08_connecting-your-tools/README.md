###### [toTopPage](../README.md)
###### [toREADME](./README.md)
# 資料：ツールを接続する（Claude 101 レッスン 8）
- `title`: ツールを接続する（Claude 101 レッスン 8）
- `url`: https://academy.claude.com/ja/courses/claude-101/connecting-your-tools
- `source_format`: html
- `retrieved_at`: 2026-11-15T17:45:06+09:00
- `profile`: article
- `content_type`: 学習・ビジネス

-----
[toTop](#totoppage)
## セクション
分割なし

-----
[toTop](#totoppage)
## 概要
Claude 101 のレッスン 8 の記事です。仕事の情報は会話の外のツールにあるため、コネクタで Claude をそれらに接続し、検索・読み取り・許可された操作を会話の中で行えるようにする方法を説明します。コネクタは Model Context Protocol（MCP）で動き、クラウドサービス向けのウェブコネクタと Claude Desktop アプリ向けのデスクトップ拡張機能の 2 種類があります。接続の手順、依頼の例、スコープされたアクセスなどの考慮事項を載せています。注意：本文に見出しは無く、変換は direct で図はありません。リンク名に「（新しいタブで開きます）」というページ枠の文言が残っています。リンク先の中身と動画は読んでおらず、字幕も取っていません。

-----
[toTop](#totoppage)
## 生成AIの総括
### 情報の置き場所へ Claude をつなぐ「通行許可」
- 横断分析：
  - 目的の視点：会話にコピーを貼る作業をなくし、実際の情報を直接扱わせる。
  - 仕組みの視点：MCP という共通の窓口があり、クラウド向けのウェブコネクタとローカル向けのデスクトップ拡張機能に分かれる。
  - 手順の視点：ウェブコネクタは「見つける→連携する→認証→権限→テスト」、デスクトップ拡張機能は「アプリを入れる→設定 > 拡張機能→インストール→追加設定」と、どちらも順序が決まっており、Team・Enterprise では先に組織のオーナーの対応が要る。
  - 安全の視点：権限は絞られ、自分が見られる範囲までで、いつでも取り消せる。【補足】この 4 つは、便利さと管理のバランスを取る設計として読める（筆者の整理）。
- 一言まとめ：コネクタは、自分が見られる範囲で、必要な権限だけを渡して、Claude を仕事の情報の置き場所へつなぐ仕組みである。

-----
[toTop](#totoppage)
## 本文
- [01_source.md](./01_source.md)：入力 Markdown の複製（本文は変更していません）

-----
[toTop](#totoppage)
## 解説メモ
- [02_explanation_memo.md](./02_explanation_memo.md)

-----
[toTop](#totoppage)
## FAQ
- [11_question_and_answer.md](./11_question_and_answer.md)

-----
[toTop](#totoppage)
## LLM 用プロンプト
- [12_LLM_prompts_as_guide.md](./12_LLM_prompts_as_guide.md)

-----
[toTop](#totoppage)
<!-- slides:start -->
## 解説資料（`Ctrl+Shift+クリック`で開くことをお勧めします）
- [解説スライド](./docs/connecting-your-tools-explained-slides.html)
- [スライド原稿](./docs/connecting-your-tools-explained-slides.md)
<!-- slides:end -->

-----
[toTop](#totoppage)
