#!/usr/bin/env python3
"""ページの README.md と、作業ログ（.work/working-log.md）を作る・更新する。

ページのフォルダの形（解説メモがあるページ）:
  README.md        表紙（解説メモの入口。ced-craft-explanation-docs が作る）。冒頭のリンクを直し、末尾に
                   「解説資料」（スライドの HTML と原稿 MD へのリンク）を足す（このスクリプト）。「状態と関連資料」は置かない（作業ログを見る）
  解説メモ 5 本    冒頭は toTopPage＝../README.md（1 つ上のまとまりの README）、toREADME＝./README.md（README 自身も自分を指す）
  .work/working-log.md   状態・検査の結果・確認していないこと・作業の経緯（検査の結果の節は、このスクリプトが更新する）
解説メモが無いページ（薄いページ・失敗・重複・取得済み）は、README.md をこのスクリプトの render が作る（ページ README）。

使い方:
  python3 tools/page_readme.py <ID>            解説メモがあるページ：作業ログの検査の結果と、表紙末尾の状態を更新する
                                               解説メモが無いページ：README が無いときだけ作る（作り直すなら --force）
  python3 tools/page_readme.py --all           台帳の、解説メモがあるページすべて
何度実行しても同じ結果になる（印のコメントの間だけを書き換える。手で書いた部分は触らない）。
状態の言葉は 作成中／検査済み／確定。検査済み＝台帳が「完了」（機械検査がすべて通った）、確定＝さらに学習済みの日がある。
"""
import os, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (ROOT, read_ledger, today, has_memo, working_log, slide_mds, slide_htmls, MEMO_FILES, LOG_NAME,
                    NAV_RE, NAV_NEW, SLIDES_START, SLIDES_END, SEP_LINES, SLIDES_BLOCK_RE)
from page_status import page_status

STATUS_START, STATUS_END = "<!-- page-status:start -->", "<!-- page-status:end -->"
CHECKS_START, CHECKS_END = "<!-- checks:start -->", "<!-- checks:end -->"
SEP = "-----\n[toTop](#totoppage)"
DEFAULT_UNVERIFIED = ["原本のリンク先の中身、画像・動画", "手順を実際に自分のアカウントで操作した結果",
                      "読み合わせは作成者（AI）が行ったもの（第三者の確認ではない）"]


# ------------------------------------------------------------ 解説メモが無いページの README（従来どおり）

def nav(page):
    return NAV_NEW + "\n"                                # toTopPage＝../README.md、toREADME＝./README.md（ページのフォルダ）


def head(r, page):
    orig = sorted((page / "00_originals").glob("*.md"))
    got = ""
    if orig:
        m = re.search(r"^retrieved_at: (\S+)", orig[0].read_text(encoding="utf-8"), re.M)
        got = m.group(1)[:10] if m else ""
    mins = f"{r['minutes']} 分（学習メモの値。本文に分数が無いことがある）" if r["minutes"] else "本文に書かれていない"
    return (f"# {r['id']} {r['title']}\n- 元ページ: {r['url']}（取得: {got or '未取得'}）\n"
            f"- 所要: {mins}　内容の種類: {r['kind']}　状態: {r['status']}（現在の状態は[台帳](../../../00_index.md)が正）\n")


def original_link(page):
    """原本（00_originals/*.md）へのリンク。フォルダ（./00_originals/）を指すと、VitePress のサイトで切れる。"""
    o = sorted((Path(page) / "00_originals").glob("*.md"))
    return f"[00_originals/{o[0].name}](./00_originals/{o[0].name})" if o else "00_originals/"


def render(r, page, state="pending", reason=""):
    """解説メモが無いページ（thin / pending / failed / duplicate）の README。"""
    page = Path(page)
    orig = original_link(page)
    t = nav(page) + head(r, page) + "\n"
    if state == "thin":
        t += f"## 薄いページ\n本文が 300 字未満のため、解説メモとスライドは作っていない（本文に無いことを書くことになるため）。\n- 理由: {reason}\n- 原本: {orig}\n- 文字起こしなど本文を足せたら、`python3 tools/fetch_page.py {r['id']} --redo` で作り直せる\n"
    elif state == "pending":
        t += (f"## 取得済み（解説は未作成）\n- 原本: {orig}\n"
              f"- {reason}\n- 次: 解説メモ（ced-craft-explanation-docs。作ると、この README が解説メモの表紙に置き換わる）とスライド（ced-websearch-slide-ja。docs/ に置く）を作り、`python3 tools/ledger.py refresh`\n")
    elif state == "failed":
        t += f"## 取得できなかった\n- 理由: {reason}\n- 対処: 強制的な取得（--force）は使わない。ブラウザで本文が読めるなら、Claude in Chrome で読む（ボタンは押さない）\n"
    elif state == "duplicate":
        t += f"## 重複\n同じページが別の場所にある。実体: {reason}\n- 解説メモ・スライドは実体のページを見る。ここでは作らない\n"
    else:
        raise ValueError(f"state が不明: {state}")
    return t + "\n-----\n[toTop](#totoppage)\n"


# ------------------------------------------------------------ 作業ログ

def _replace_between(text, start, end, block):
    """start〜end の印の間（印を含む）を block に置き換える。印が無ければ None。"""
    i, j = text.find(start), text.find(end)
    if i < 0 or j < i:
        return None
    return text[:i] + block + text[j + len(end):]


def marks_count(page):
    cnt = {"補足": 0, "推測": 0}
    for n in MEMO_FILES:
        f = page / n
        if f.is_file() and n != "01_source.md":
            x = f.read_text(encoding="utf-8")
            cnt["補足"] += x.count("【補足】"); cnt["推測"] += x.count("【推測】")
    conf = sum(x.read_text(encoding="utf-8").count("（要確認:") for x in slide_mds(page))
    return cnt, conf


def checks_block(st, cnt, conf):
    return (f"{CHECKS_START}\n## 検査の結果（`tools/page_readme.py` が更新する。最新）\n"
            f"- 確認日: {today()}\n"
            f"- 解説メモ: `check_docs.py`（`--out-dir .work/intermediate`）で {st.get('memo') or '未実施'}\n"
            f"- スライド: {st.get('slides') or '未実施'}\n"
            f"- 数字の照合: 出典の無い数字 {len(st.get('numbers_missing') or [])} 件\n"
            f"- リンク切れ: {st.get('links_broken')} 件\n"
            f"- 印の件数: 解説メモの【補足】{cnt['補足']}・【推測】{cnt['推測']}、スライドの（要確認: {conf}\n"
            f"{CHECKS_END}")


def update_log(r, page, st):
    """作業ログの「検査の結果」を更新する。ログが無ければ作る。手で書いた部分は触らない。"""
    log = working_log(page)
    cnt, conf = marks_count(page)
    block = checks_block(st, cnt, conf)
    if not log.exists():
        log.parent.mkdir(parents=True, exist_ok=True)
        text = (f"# 作業ログ：{r['id']} {r['title']}\n\n"
                f"状態・検査の結果・確認していないこと・作業の経緯を書く。表紙（[../README.md](../README.md)）には要約だけを置く。\n\n"
                f"{block}\n\n## 確認していないこと\n" + "".join(f"- {x}\n" for x in DEFAULT_UNVERIFIED) +
                f"\n## 作業の経緯\n- {today()} 作成（`tools/page_readme.py`）\n")
    else:
        text = log.read_text(encoding="utf-8")
        new = _replace_between(text, CHECKS_START, CHECKS_END, block)
        if new is None:                               # 印が無いログ（移行したもの）：最初の「## 」の前に入れる
            m = re.search(r"^## ", text, re.M)
            at = m.start() if m else len(text)
            new = text[:at] + block + "\n\n" + text[at:]
        text = new
    log.write_text(text, encoding="utf-8")
    return text


def normalize_nav(page):
    """解説メモ 5 本の冒頭リンクをそろえる（toTopPage＝../README.md、toREADME＝./README.md）。変えたファイル名を返す。"""
    changed = []
    for n in MEMO_FILES:
        f = Path(page) / n
        if not f.is_file():
            continue
        t = f.read_text(encoding="utf-8")
        t2 = NAV_RE.sub(NAV_NEW, t, count=1)
        if t2 != t:
            f.write_text(t2, encoding="utf-8"); changed.append(n)
    return changed


def slides_block(page):
    """「解説資料」の節（スライドの HTML と原稿 MD へのリンク）。スライドが無ければ None。"""
    sh, sm = slide_htmls(page), slide_mds(page)
    if not sh and not sm:
        return None
    L = [SLIDES_START, "## 解説資料（別タブで開きます）"]
    if sh:
        L.append(f"- [解説スライド](./docs/{sh[0].name})")
    if sm:
        L.append(f"- [スライド原稿](./docs/{sm[0].name})")
    L.append(SLIDES_END)
    return "\n".join(L)


STATUS_BLOCK_RE = re.compile(re.escape(STATUS_START) + r".*?" + re.escape(STATUS_END) + r"\n\n" + re.escape(SEP_LINES), re.S)


def apply_cover_sections(text, slides):
    """表紙の末尾に「解説資料」の節を置く。何度でも同じ結果。以前の版の「状態と関連資料」の節が残っていれば外す。
    slides が None なら「解説資料」は置かない。"""
    text = STATUS_BLOCK_RE.sub("", text)
    text = SLIDES_BLOCK_RE.sub("", text)
    body = text.rstrip("\n")
    if not body.endswith(SEP):
        raise ValueError("表紙の末尾が区切り（-----／[toTop](#totoppage)）で終わっていない。解説メモの表紙ではない？")
    if slides:
        body += "\n" + slides + "\n\n" + SEP                  # 実際の表紙の形：解説資料のあとにも区切りを 1 つ置く
    return body + "\n"


def update_cover(r, page):
    """解説メモがあるページ：作業ログと、表紙（README.md）の末尾の「解説資料」の節を更新する。"""
    page = Path(page)
    st = page_status(page)
    log_text = update_log(r, page, st)
    normalize_nav(page)                                # 5 本の冒頭リンク
    f = page / "README.md"
    new = apply_cover_sections(f.read_text(encoding="utf-8"), slides_block(page))
    f.write_text(new, encoding="utf-8")
    return st


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit(2)
    _, rows = read_ledger()
    if a[0] == "--all":
        n = 0
        for r in rows:
            page = ROOT / r["page_dir"]
            if page.is_dir() and has_memo(page):
                update_cover(r, page); n += 1
        print(f"{n} ページの作業ログと表紙の状態を更新しました")
        return
    hit = [x for x in rows if x["id"] == a[0]]
    if not hit:
        print("その ID は台帳にありません"); sys.exit(2)
    r = hit[0]; page = ROOT / r["page_dir"]
    if has_memo(page):
        update_cover(r, page)
        print(f"{page / 'README.md'} の状態と {working_log(page)} を更新しました")
        return
    if (page / "README.md").exists() and "--force" not in a:
        print("解説メモが無いページ。README.md が既にあります（作り直すなら --force）"); sys.exit(0)
    state = {"薄いページ": "thin", "失敗": "failed", "重複": "duplicate"}.get(r["status"], "pending")
    (page / "README.md").write_text(render(r, page, state, "（理由は台帳の備考を参照）" if state != "pending" else ""), encoding="utf-8")
    print(f"{page / 'README.md'} を作りました（{state}）")


if __name__ == "__main__":
    main()
