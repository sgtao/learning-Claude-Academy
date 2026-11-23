#!/usr/bin/env python3
"""ページの README.md を作る（完了・薄いページ・失敗・重複で中身を変える）。

使い方:  python3 tools/page_readme.py <ID> [--force]     完了に向かうページの README を、検査の結果から作る
README が既にあるときは、--force が無ければ何もしない。fetch_page.py は、薄いページ・失敗・重複のときにここの render を使う。
"""
import os, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, read_ledger, body_of, today
from page_status import page_status


def nav(page):
    top = os.path.relpath(ROOT / "README.md", page)
    up = os.path.relpath(page.parent / "README.md", page)
    return f"###### [toTopPage]({top})\n###### [toREADME]({up})\n"


def head(r, page):
    orig = sorted((page / "00_originals").glob("*.md"))
    got = ""
    if orig:
        m = re.search(r"^retrieved_at: (\S+)", orig[0].read_text(encoding="utf-8"), re.M)
        got = m.group(1)[:10] if m else ""
    mins = f"{r['minutes']} 分（学習メモの値。本文に分数が無いことがある）" if r["minutes"] else "本文に書かれていない"
    return (f"# {r['id']} {r['title']}\n- 元ページ: {r['url']}（取得: {got or '未取得'}）\n"
            f"- 所要: {mins}　内容の種類: {r['kind']}　状態: {r['status']}（現在の状態は[台帳](../../../00_index.md)が正）\n")


def render(r, page, state="complete", reason=""):
    page = Path(page)
    t = nav(page) + head(r, page) + "\n"
    if state == "thin":
        t += f"## 薄いページ\n本文が 300 字未満のため、解説メモとスライドは作っていない（本文に無いことを書くことになるため）。\n- 理由: {reason}\n- 原本: [00_originals](./00_originals/)\n- 文字起こしなど本文を足せたら、`python3 tools/fetch_page.py {r['id']} --redo` で作り直せる\n"
    elif state == "pending":
        o = sorted((page / "00_originals").glob("*.md"))
        t += (f"## 取得済み（解説は未作成）\n- 原本: [00_originals](./00_originals/)\n"
              f"- {reason}\n- 次: 解説メモ（ced-craft-explanation-docs）とスライド（ced-websearch-slide-ja）を作り、`python3 tools/ledger.py refresh`\n")
    elif state == "failed":
        t += f"## 取得できなかった\n- 理由: {reason}\n- 対処: 強制的な取得（--force）は使わない。ブラウザで本文が読めるなら、Claude in Chrome で読む（ボタンは押さない）\n"
    elif state == "duplicate":
        t += f"## 重複\n同じページが別の場所にある。実体: {reason}\n- 解説メモ・スライドは実体のページを見る。ここでは作らない\n"
    else:
        sl = sorted(page.glob("*-explained-slides.md")); ex = sorted(page.glob("*_explained"))
        stt = page_status(page)
        cnt = {"補足": 0, "推測": 0}
        for e in ex:
            for f in e.glob("0*.md"):
                x = f.read_text(encoding="utf-8"); cnt["補足"] += x.count("【補足】"); cnt["推測"] += x.count("【推測】")
            f = e / "11_question_and_answer.md"
            if f.exists():
                x = f.read_text(encoding="utf-8"); cnt["補足"] += x.count("【補足】"); cnt["推測"] += x.count("【推測】")
        conf = sum(x.read_text(encoding="utf-8").count("（要確認:") for x in sl)
        o = sorted((page / "00_originals").glob("*.md"))
        slug = r["slug"]
        t += "## 成果物\n| 種類 | ファイル |\n|---|---|\n"
        if o:
            t += f"| 原本 | [00_originals/{o[0].name}](./00_originals/{o[0].name}) |\n"
        if ex:
            t += f"| 解説メモ（入口） | [{ex[0].name}/README.md](./{ex[0].name}/README.md) |\n"
        if sl:
            h = sl[0].with_suffix(".html")
            t += f"| 解説スライド | [{h.name}](./{h.name})（原稿: [.md](./{sl[0].name})） |\n"
        t += (f"\n## 検査（{today()} に実際に出力を確認）\n- 解説メモ: `check_docs.py` で {stt.get('memo') or '未実施'}\n"
              f"- スライド: {stt.get('slides') or '未実施'}\n- 数字の照合: 出典の無い数字 {len(stt.get('numbers_missing') or [])} 件\n"
              f"- リンク切れ: {stt.get('links_broken')} 件\n- 印の件数: 解説メモの【補足】{cnt['補足']}・【推測】{cnt['推測']}、スライドの（要確認: {conf}\n"
              "\n## 確認していないこと\n- 原本のリンク先の中身、画像・動画\n- 手順を実際に自分のアカウントで操作した結果\n- 読み合わせは作成者（AI）が行ったもの（第三者の確認ではない）\n")
    return t + "\n-----\n[toTop](#totoppage)\n"


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit(2)
    _, rows = read_ledger()
    hit = [x for x in rows if x["id"] == a[0]]
    if not hit:
        print("その ID は台帳にありません"); sys.exit(2)
    r = hit[0]; page = ROOT / r["page_dir"]
    if (page / "README.md").exists() and "--force" not in a:
        print("README.md が既にあります（作り直すなら --force）"); sys.exit(0)
    (page / "README.md").write_text(render(r, page), encoding="utf-8")
    print(f"{page / 'README.md'} を作りました")


if __name__ == "__main__":
    main()
