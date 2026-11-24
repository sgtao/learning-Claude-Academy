#!/usr/bin/env python3
"""旧版スキル（v0.0.6）で作った解説メモの作業フォルダを、今の形（ced-skills 0.0.3）にそろえる。

やること（本文には触れない。形だけ）:
  1. intermediate/06_summary.md（旧構造は out/） の「横断分析」を、視点ごとの子箇条書きにする（（1）（2）… で分けられるときだけ）
  2. README.md・01_source.md の先頭のナビを ./README.md にし、README に「## LLM 用プロンプト」の節を足す
  3. assemble.py で 02・11・12 と README の総括を作り直す（呼ぶのは人。この script は 1・2 だけ）

使い方:  python3 tools/upgrade_explained.py <作業フォルダ> [--dry-run]
作業フォルダ＝解説メモ 5 本があるフォルダ（新構造ではページのフォルダ）。中間ファイルは .work/intermediate/（旧構造は out/）から探す。
分けられないとき（視点が 3 個未満）は、何も書かずに「手で直す」と表示して終わる。
"""
import re, sys
from pathlib import Path

MARK = re.compile(r"[（(]\s*(?:\d+)\s*[)）]|[①-⑨]")


def split_cross(text):
    """『横断分析：』の本文を (前置き, [(視点名, 文)...]) にする。分けられなければ None。"""
    marks = list(MARK.finditer(text))
    if len(marks) < 3:
        return None
    pre = text[: marks[0].start()].strip()
    items = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        seg = text[m.end():end].strip().rstrip("。 ") + "。"
        mm = re.match(r"([^：。]{1,16})：(.+)", seg)
        if mm:
            name, body = mm.group(1).strip(), mm.group(2).strip()
        else:
            name, body = f"視点{i + 1}", seg
        items.append((name, body))
    return pre, items[:4] if len(items) > 4 else items


def fix_summary(path, dry):
    lines = path.read_text(encoding="utf-8").split("\n")
    out, changed = [], False
    for i, ln in enumerate(lines):
        m = re.match(r"- 横断分析：(.*)$", ln)
        nxt_child = i + 1 < len(lines) and re.match(r"\s+- ", lines[i + 1])
        if m and m.group(1).strip() and not nxt_child:
            r = split_cross(m.group(1))
            if r is None:
                return "手で直す（視点を数字で分けられない）"
            pre, items = r
            out.append("- 横断分析：" + pre)
            out += [f"  - {n}：{b}" for n, b in items]
            changed = True
        else:
            out.append(ln)
    if changed and not dry:
        path.write_text("\n".join(out), encoding="utf-8")
    return "変えた" if changed else "変更なし"


def fix_nav(path, dry):
    t = path.read_text(encoding="utf-8")
    t2 = re.sub(r"\A###### \[toTopPage\]\([^)]*\)", "###### [toTopPage](../README.md)", t, count=1)
    if path.name == "README.md" and "## LLM 用プロンプト" not in t2:
        add = ("-----\n[toTop](#totoppage)\n## LLM 用プロンプト\n"
               "- [12_LLM_prompts_as_guide.md](./12_LLM_prompts_as_guide.md)\n\n")
        i = t2.rstrip().rfind("-----\n[toTop](#totoppage)")
        t2 = t2[:i] + add + t2[i:]
    if t2 != t:
        if not dry:
            path.write_text(t2, encoding="utf-8")
        return "変えた"
    return "変更なし"


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    d = Path(sys.argv[1]); dry = "--dry-run" in sys.argv
    mid = d / ".work" / "intermediate"
    if not mid.is_dir():
        mid = d / "out"                # 旧構造
    res = fix_summary(mid / "06_summary.md", dry)
    print(f"{d.name}: 06_summary {res}")
    if res.startswith("手で直す"):
        sys.exit(1)
    for n in ("README.md", "01_source.md"):
        print(f"{d.name}: {n} {fix_nav(d / n, dry)}")


if __name__ == "__main__":
    main()
