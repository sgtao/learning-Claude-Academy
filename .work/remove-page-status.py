#!/usr/bin/env python3
"""ページ直下の README.md（表紙）から、<!-- page-status:start --> 以降を削除する（一度きり。何も他のファイルは触らない）。

削除するもの：
  <!-- page-status:start -->  から最後までの行（「状態と関連資料」の節）
  その直前の区切り（-----／[toTop](#totoppage)）。残すと、表紙が区切りだけで終わるため。
残すもの：それより前の本文・「解説資料」の節（<!-- slides:start/end -->）。

安全のため、マーカーの後ろが「状態と関連資料」の節と末尾の区切りだけでないファイルは、何も変えずに止める。

使い方（03_outputs/ から）:
  python3 .work/remove-page-status.py                 試し（何も書かず、対象を表示）
  python3 .work/remove-page-status.py --apply          実行
  python3 .work/remove-page-status.py --root <フォルダ>  検査用（コピーに対して実行する）
何度実行しても同じ結果になる（マーカーが無ければ何もしない）。終了コード: 0＝すべて成功、1＝止めたファイルがある。
"""
import argparse, re, sys
from pathlib import Path

START = "<!-- page-status:start -->"
TAIL = re.compile(
    re.escape(START) + r"\n.*?<!-- page-status:end -->\n\n-----\n\[toTop\]\(#totoppage\)\n?\Z", re.S)
SEP_TAIL = "\n-----\n[toTop](#totoppage)\n"


def covers(root):
    """ステップ／まとまり／ページの README.md（表紙）だけ。"""
    for p in sorted(root.glob("step*/*/*/README.md")):
        yield p


def cut(text):
    """(新しい本文, 状態) を返す。状態は 'none'（マーカー無し）・'cut'（削除）・'stop'（想定外の内容）。"""
    if START not in text:
        return text, "none"
    m = TAIL.search(text)
    if not m or text.count(START) != 1:
        return text, "stop"
    head = text[:m.start()]
    if head.endswith(SEP_TAIL):                       # 状態の節の直前の区切り（-----／[toTop]）も外す
        head = head[: -len(SEP_TAIL)] + "\n"
    return head.rstrip("\n") + "\n", "cut"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    a = ap.parse_args()
    root = Path(a.root).resolve()
    n_cut = n_none = n_stop = 0
    for p in covers(root):
        rel = p.relative_to(root)
        new, st = cut(p.read_text(encoding="utf-8"))
        if st == "none":
            n_none += 1
        elif st == "stop":
            n_stop += 1
            print(f"止める（想定外の内容）: {rel}")
        else:
            n_cut += 1
            print(f"{'削除' if a.apply else '[試し] 削除'}: {rel}")
            if a.apply:
                p.write_text(new, encoding="utf-8")
    print(f"削除: {n_cut}／マーカー無し: {n_none}／止めた: {n_stop}")
    if not a.apply:
        print("（試し。実行するには --apply）")
    return 1 if n_stop else 0


if __name__ == "__main__":
    sys.exit(main())
