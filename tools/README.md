# tools/ — 台帳・索引・検査のスクリプト

標準ライブラリだけで動く（Python 3.9 以上）。リポジトリのトップ（`03_outputs/`）から実行する。

| スクリプト | 用途 | いつ使うか |
|---|---|---|
| `ledger.py seed` | 台帳 `ledger.csv` を作る（71 ページ） | 初回だけ |
| `ledger.py refresh` | フォルダのあるページを検査し直し、台帳の検査結果と状態を更新（薄いページ・重複・失敗は手で決めた状態なので変えない） | ページを作った・直したあと |
| `ledger.py learned <ID> [日付]` | 学習済みの日を入れる | 学んだとき |
| `build_index.py` | 台帳から `00_index.md` と、各ステップ・まとまりの README の表を作る（`--check` で古さだけ確かめる） | 台帳を変えたあと |
| `check_index.py` | 台帳と索引の検査（状態の値・完了の条件・台帳に無いページ・索引の古さ） | 毎回の最後 |
| `check_numbers.py <ページ>` | スライド（`docs/`）の数字が原本か解説メモにあるか | ページを作ったとき |
| `check_links.py [フォルダ]` | Markdown の相対リンク切れ | 毎回の最後 |
| `page_status.py <ページ>` | 1 ページ分の検査結果（JSON） | 調べたいとき |
| `add_page.py <URL>` | 日本語版の URL 1 つを、取得・薄い判定・台帳への追加まで行う（止まる条件は 4 通り） | 台帳に無い新しいページを足すとき |
| `page_readme.py <ID>` / `--all` | 解説メモがあるページ：表紙 `README.md` の末尾の「状態と関連資料」と、`.work/working-log.md` の「検査の結果」を更新（何度でも同じ結果）。解説メモが無いページ：README が無いときだけ作る（`--force` で作り直す） | ページを作ったあと |
| `catalog.py [--due]` | 公開のサイトマップを取り、台帳の対象の消えた件数と、対象外の件数を報告（`catalog/` に記録）。`--due` は 30 日経過の判定 | 30 日ごと |
| `upgrade_explained.py <ページのフォルダ>` | 旧版のスキルで作った解説メモの形を、今の版にそろえる（本文は変えない） | 旧版のページを直すとき |
| `test_structure.py` | 構造の移行スクリプトと、表紙・作業ログの更新の検査（見本の木と実物の木） | 移行スクリプトや `page_readme.py` を直したとき |
| `memo.py groups [STEP]` | ステップごとの「まとまり」の名前だけの一覧 | 何があるか見たいとき |
| `memo.py pages [STEP] GROUP` / `pages -a [STEP]` | まとまりの中のページ（解説メモ）の一覧。`-a` は全ページ（STEP を付けるとそのステップだけ） | 読むページを探すとき |
| `memo.py info PAGE [--json]` | 表紙 `README.md` のフロントマター（題名・URL・取得日など。無いページは原本の frontmatter） | ページの素性を確かめるとき |
| `memo.py show PAGE [--only ...]` | 表紙 `README.md`・`.work/intermediate/09_input-memo.md`・`12_LLM_prompts_as_guide.md` を表示（09 か 12 が無いページは README と `01_source`、解説メモが無いページはページの README と原本） | 解説メモを読む・LLM に渡すとき |
| `test_site.py` | VitePress のサイトの検査（ビルドできる・リンク切れ 0・台帳の全ページが出る・スライドがコピーされる・`.work/` が出ない・base が効く。Node と `npm ci` が要る） | サイトの設定を直したとき、公開の前 |
| `test_memo.py` | `memo.py` の検査（見本の木と実物の木） | `memo.py` を直したとき |

解説メモの検査（`check_docs.py`）は、ced-skills の `ced-craft-explanation-docs` のものを使う（`page_status.py` が最新の版を探し、ページのフォルダを `--out-dir <ページ>/.work/intermediate` つきで検査する）。
表紙 `README.md` のリンクは、check_docs の C-5 により、ページのフォルダの外を指せない。

## URL を 1 つ追加する流れ
```bash
python3 tools/add_page.py <URL> --step 9 --group 01_added --kind 技術・ハウツー
# ここで解説メモとスライドを作る（learning-page スキル。解説メモは直下、スライドは docs/、中間ファイルは .work/intermediate/）
python3 tools/page_readme.py <ID>
python3 tools/ledger.py refresh && python3 tools/build_index.py && python3 tools/check_index.py && python3 tools/check_links.py
```

## 1 ページを作ったあとの流れ
```bash
python3 tools/ledger.py refresh      # そのページの検査と状態を台帳に反映
python3 tools/build_index.py         # 索引と README の表を作り直す
python3 tools/check_index.py && python3 tools/check_links.py
```

## 解説メモを引く（`memo.py`）
読むだけで、何も書き換えない。ツール自身の文言（見出し・ラベル・注記・エラー）は半角英数字記号で出す。
ファイルの内容、題名、台帳の値（状態など）は、そのまま（日本語のまま）出る。題名は「<ステップ名>_<まとまり名>_<解説メモの題名>」で表示する。
STEP は `1`・`step1_basics`・`basics`、GROUP は `01`・`01_academy-courses-claude-101`・`claude-101`、
PAGE は台帳の ID（`1-7`）・フォルダ名・slug・パス・名前の一部のどれでもよい（複数に当たると候補を出して止まる）。

```bash
python3 tools/memo.py groups                 # 全ステップの「まとまり」（名前だけ）
python3 tools/memo.py groups 3               # ステップ 3 だけ
python3 tools/memo.py pages 1 01             # ステップ 1 のまとまり 01 のページ
python3 tools/memo.py pages -a               # 全ページ（`pages -a 3` ならステップ 3 だけ）
python3 tools/memo.py info 1-7               # フロントマター（--json で JSON）
python3 tools/memo.py show 1-7               # README ＋ out/09_input-memo.md ＋ 12_LLM_prompts_as_guide.md
python3 tools/memo.py show 1-7 --only prompt # 一部だけ（readme input prompt source）
python3 tools/test_memo.py                   # 検査
```

## ページのフォルダの形と、構造の移行
```
<ページ>/README.md（表紙）・00_originals/・01_source.md・02_explanation_memo.md・11_question_and_answer.md・12_LLM_prompts_as_guide.md
        docs/（スライドの MD と HTML）・.work/working-log.md（追跡する）・.work/intermediate/（追跡しない）
```
旧構造（`<slug>_explained/` の中に解説メモと `out/`、スライドがページ直下、ページ README に状態）からは、
`.work/migrate-page-structure.sh` で一度だけ移した（2026-11-25）。試しは `bash .work/migrate-page-structure.sh`、実行は `--apply`。
旧ページ README は `.work/working-log.md` に、解説メモの README は表紙に、`out/` は `.work/intermediate/` に、スライドは `docs/` に移る（何も削除しない）。
