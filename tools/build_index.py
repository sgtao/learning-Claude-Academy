#!/usr/bin/env python3
"""台帳（ledger.csv）から、索引（00_index.md）と、各ステップ・各まとまりの README の台帳の表を作る。

索引（00_index.md）は、「## ステップ N：…」の節の表だけを書き換える。表の外の文章（見出し・注記・フォルダの見方）は、
手で直してよく、このスクリプトは触らない。索引が無いときだけ、ひな形（index_text）から作る。

使い方:  python3 tools/build_index.py          書き込む
         python3 tools/build_index.py --check  書かずに、今のファイルが台帳と同じかを確かめる（違えば終了コード 1）
README の表は <!-- ledger:start --> と <!-- ledger:end --> の間だけを書き換える（外の文章は触らない）。
README が無いステップ・まとまりは、作る。人が書いた README（印が無いもの）は変えない。
"""
import sys
import re
from collections import OrderedDict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, INDEX, STEPS, read_ledger

START, END = "<!-- ledger:start -->", "<!-- ledger:end -->"


def rel(path_from, target):
    import os
    return os.path.relpath(target, path_from).replace(os.sep, "/")


def table(rows, base):
    out = ["| ID | ページ | 分 | 種類 | 状態 | 学習済みの日 | 備考 |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        readme = ROOT / r["page_dir"] / "README.md"
        title = r["title"].replace("|", "／")
        cell = f"[{title}]({rel(base, readme)})" if readme.exists() else title
        out.append(f"| {r['id']} | {cell} | {r['minutes'] or '－'} | {r['kind']} | {r['status']} | {r['learned_on'] or ''} | {r['note'].replace('|', '／')} |")
    return "\n".join(out)


NOTE = "> このファイルは `tools/build_index.py` が `ledger.csv` から作る。手で直さない（直すなら `ledger.csv`）。"


def step_sections(rows):
    by = OrderedDict()
    for r in rows:
        by.setdefault(r["step"], []).append(r)
    return by


def index_text(rows):
    """索引が無いときの、ひな形。今の索引の形（フォルダの見方 → ステップごとの表 → 末尾の注記）。"""
    L = ["# 学習メモ 索引（Claude Academy）", "",
         "## フォルダの見方", "", "```", "03_outputs/",
          "├── README.md            この場所の地図",
          "├── 00_index.md          この索引（台帳から作る）",
          "├── ledger.csv           台帳（ページの一覧と状態の正本）",
          "├── tools/               検査と台帳のスクリプト（tools/README.md）",
          "└── step<N>_<名前>/       ステップごと（0 入口 ／ 1 基礎 ／ 2 道具 ／ 3 職種 ／ 4 発展）",
          "    └── <NN>_<まとまり>/  関連するページのまとまり",
          "        └── <NN>_<ページ>/ 1 ページ分（README=表紙、00_originals、解説メモ 5 本、docs/=スライド、.work/=作業用）",
          "```", ""]
    for s, rs in step_sections(rows).items():
        name, jp = STEPS[s]
        L += [f"## ステップ {s}：{jp}（`{name}/`）", "", table(rs, ROOT), ""]
    L += ["## note", "", NOTE, "", ""]
    return "\n".join(L)


def update_index(old, rows):
    """今の索引の本文のうち、各ステップの表（「## ステップ N：」の節の、| で始まる連続した行）だけを台帳から作り直す。
    表の外は 1 字も変えない。台帳にあるステップの節が無ければ、最後のステップの節の後ろ（無ければ末尾）に足す。何度でも同じ結果。"""
    lines = old.split("\n")
    for s, rs in step_sections(rows).items():
        name, jp = STEPS[s]
        head = f"## ステップ {s}："
        tbl = table(rs, ROOT).split("\n")
        at = next((i for i, l in enumerate(lines) if l.startswith(head)), None)
        if at is None:
            ends = [i for i, l in enumerate(lines) if l.startswith("## ステップ ")]
            pos = len(lines)
            if ends:                                       # 最後のステップの節の終わり（次の「## 」の手前）
                pos = next((i for i in range(ends[-1] + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
            sec = [f"## ステップ {s}：{jp}（`{name}/`）", ""] + tbl + [""]
            lines[pos:pos] = sec
            continue
        i = at + 1
        while i < len(lines) and not lines[i].startswith("|") and not lines[i].startswith("## "):
            i += 1
        j = i
        while j < len(lines) and lines[j].startswith("|"):
            j += 1
        if i == j:                                         # 表が無い節：見出しの後ろに置く
            lines[at + 1:at + 1] = ["", *tbl]
        else:
            lines[i:j] = tbl
    return "\n".join(lines)


def block(rows, base):
    return f"{START}\n{table(rows, base)}\n{END}"


def readme_new(kind, d, title, rows):
    top = rel(d, d.parent / "README.md")                 # toTopPage は 1 つ上の README
    if kind == "step":
        head = f"###### [toTopPage]({top})\n###### [toREADME](./README.md)\n# {d.name} — {title}\n\nこのステップのページの台帳。`ledger.csv` から作る（表は自動で更新される。外の文章は手で書いてよい）。\n\n## 台帳\n"
    else:
        head = f"###### [toTopPage]({top})\n###### [toREADME](./README.md)\n# {d.name}\n\nこのまとまりのページ。`ledger.csv` から作る。\n\n"
    return head + block(rows, d) + "\n"


def apply(path, kind, title, rows, check, bad):
    base = path.parent
    if path.exists():
        t = path.read_text(encoding="utf-8")
        if START not in t:
            return                     # 人が書いた README は触らない
        a, b = t.index(START), t.index(END) + len(END)
        new = t[:a] + block(rows, base) + t[b:]
    else:
        new = readme_new(kind, base, title, rows)
    if not path.exists() or path.read_text(encoding="utf-8") != new:
        if check:
            bad.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(new, encoding="utf-8")


def main():
    check = "--check" in sys.argv
    _, rows = read_ledger()
    bad = []
    txt = update_index(INDEX.read_text(encoding="utf-8"), rows) if INDEX.exists() else index_text(rows)
    if not INDEX.exists() or INDEX.read_text(encoding="utf-8") != txt:
        if check:
            bad.append("00_index.md")
        else:
            INDEX.write_text(txt, encoding="utf-8")
    steps, groups = OrderedDict(), OrderedDict()
    for r in rows:
        steps.setdefault(r["step"], []).append(r)
        groups.setdefault((r["step"], r["group"]), []).append(r)
    for s, rs in steps.items():
        d = ROOT / STEPS[s][0]
        if any((ROOT / r["page_dir"]).exists() for r in rs):
            apply(d / "README.md", "step", f"ステップ {s}：{STEPS[s][1]}", rs, check, bad)
    for (s, g), rs in groups.items():
        d = ROOT / STEPS[s][0] / g
        if any((ROOT / r["page_dir"]).exists() for r in rs):
            apply(d / "README.md", "group", g, rs, check, bad)
    if check:
        for b in bad:
            print("古い:", b)
        print(f"古いファイル: {len(bad)}")
        sys.exit(1 if bad else 0)
    print("索引と README の表を作りました")


if __name__ == "__main__":
    main()
