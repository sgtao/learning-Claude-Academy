###### [toTopPage](../../../README.md)
###### [toREADME](../README.md)
# 0-3 Claudeを使い始める（Intro to Claude）
- 元ページ: https://academy.claude.com/ja/tutorials/getting-started-with-claude（取得: 2026-11-15／取得手段: Academy 日本語版を url-to-md で変換、`direct`）
- 所要（ページ表示）: 約 5 分（学習メモの値。**取得した本文には分数が無い**）　内容の種類: 技術・ハウツー　状態: 完了

## 成果物
| 種類 | ファイル |
|---|---|
| 原本 | [00_originals/getting-started-with-claude.md](./00_originals/getting-started-with-claude.md) |
| 解説メモ（入口） | [getting-started-with-claude_explained/README.md](./getting-started-with-claude_explained/README.md) |
| 解説スライド | [getting-started-with-claude-explained-slides.html](./getting-started-with-claude-explained-slides.html)（原稿: [.md](./getting-started-with-claude-explained-slides.md)） |

## 検査（実際に出力した結果）
- 解説メモ: `check_docs.py` 11 PASS / 0 FAIL（サブエージェントは 2 回目で合格と報告。メインが再実行して 11 PASS を確認）／読み合わせ: サブエージェントが本文に無い断定の削除と【補足】の付与を 2 件。メインが G-3 として**プラン条件**（Dashboards＝有料プランでベータ、Motion＝Team・Enterprise でベータ、ウェブ検索＝Free・Pro・Max は既定オン）を原本とスライドで照合して食い違い 0
- スライド: 10 枚（本文が 800 字を超えるため 8〜10 枚の目安）／`mdss-convert --strict` の lint は warnings 0・lint 0（メインが再実行）／サブエージェントが撮影した 10 枚のうち 1 枚を修正／出典の無い数字: 0
- 印の件数: `【補足】` 18・`【推測】` 3・`（要確認:` 1（Dashboards の「有料プラン」がどのプランか）

## 確認していないこと
- 動画・画像・リンク先（support.claude.com など）の中身。本文が予告する「ウォークスルー」の中身
- 「有料プラン」の範囲（本文に書かれていない）
- 原本の各リンクに残る「（新しいタブで開きます）」はページ枠の残り（解説メモの概要に注意として記載）

## 学習メモとの食い違い
- 学習メモは所要「約 5 分」。ページの本文には所要時間が無い（リサーチの「数分かかる」が唯一の時間の記述）。解説・スライドには分数を書いていない

-----
[toTop](#totoppage)
