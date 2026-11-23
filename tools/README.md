# tools/ — 台帳・索引・検査のスクリプト

標準ライブラリだけで動く（Python 3.9 以上）。リポジトリのトップ（`03_outputs/`）から実行する。

| スクリプト | 用途 | いつ使うか |
|---|---|---|
| `ledger.py seed` | 台帳 `ledger.csv` を作る（71 ページ） | 初回だけ |
| `ledger.py refresh` | フォルダのあるページを検査し直し、台帳の検査結果と状態を更新（薄いページ・重複・失敗は手で決めた状態なので変えない） | ページを作った・直したあと |
| `ledger.py learned <ID> [日付]` | 学習済みの日を入れる | 学んだとき |
| `build_index.py` | 台帳から `00_index.md` と、各ステップ・まとまりの README の表を作る（`--check` で古さだけ確かめる） | 台帳を変えたあと |
| `check_index.py` | 台帳と索引の検査（状態の値・完了の条件・台帳に無いページ・索引の古さ） | 毎回の最後 |
| `check_numbers.py <ページ>` | スライドの数字が原本か解説メモにあるか | ページを作ったとき |
| `check_links.py [フォルダ]` | Markdown の相対リンク切れ | 毎回の最後 |
| `page_status.py <ページ>` | 1 ページ分の検査結果（JSON） | 調べたいとき |
| `upgrade_explained.py <解説メモのフォルダ>` | 旧版のスキルで作った解説メモの形を、今の版にそろえる（本文は変えない） | 旧版のページを直すとき |

解説メモの検査（`check_docs.py`）は、ced-skills の `ced-craft-explanation-docs` のものを使う（`page_status.py` が最新の版を探す）。

## 1 ページを作ったあとの流れ
```bash
python3 tools/ledger.py refresh      # そのページの検査と状態を台帳に反映
python3 tools/build_index.py         # 索引と README の表を作り直す
python3 tools/check_index.py && python3 tools/check_links.py
```
