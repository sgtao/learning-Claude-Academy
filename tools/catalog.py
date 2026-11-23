#!/usr/bin/env python3
"""Academy の公開サイトマップを取り、台帳の対象（ステップ 0〜4）と比べて差分を報告する（合格条件 2 の一覧の再取得）。

使い方:
  python3 tools/catalog.py            取得して差分を表示。catalog/snapshot-<日付>.json と catalog/latest.md を書く
  python3 tools/catalog.py --due      最後の取得から 30 日を過ぎていれば "due"、そうでなければ "ok" を表示（終了コード 1 が due）
取り込まない。差分は報告だけ。台帳に足すかは、人が決める（PLAYBOOK 判断の基準 7）。
"""
import json, re, sys, urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, read_ledger, today

SITEMAP = "https://academy.claude.com/sitemap.xml"
CAT = ROOT / "catalog"
KINDS = ("courses", "tutorials", "use-cases")
# 台帳が見ている種類だけを比べる（言語は ja、英語版しか無いものは "en" として別に数える）


def fetch_sitemap():
    req = urllib.request.Request(SITEMAP, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        xml = r.read().decode("utf-8")
    return re.findall(r"<loc>([^<]+)</loc>", xml)


def classify(urls):
    """ja の対象ページ（種類 → slug の一覧）と、英語版だけのページを分ける。"""
    ja = {k: set() for k in KINDS}; en = {k: set() for k in KINDS}
    for u in urls:
        m = re.match(r"https://academy\.claude\.com/(ja/)?(courses|tutorials|use-cases)/([^/?#]+)$", u)
        if not m:
            continue
        lang = "ja" if m.group(1) else "en"
        (ja if lang == "ja" else en)[m.group(2)].add(m.group(3))
    return ja, en


def ledger_slugs():
    _, rows = read_ledger()
    s = {}
    for r in rows:
        m = re.search(r"academy\.claude\.com/ja/(courses|tutorials|use-cases)/([^/?#]+)", r.get("url", ""))
        if m:
            s.setdefault(m.group(1), set()).add(m.group(2))
    return s


def main():
    if "--due" in sys.argv:
        snaps = sorted(CAT.glob("snapshot-*.json"))
        if not snaps:
            print("due"); sys.exit(1)
        last = date.fromisoformat(snaps[-1].stem.replace("snapshot-", ""))
        if date.today() - last >= timedelta(days=30):
            print("due"); sys.exit(1)
        print("ok"); sys.exit(0)
    urls = fetch_sitemap()
    ja, en = classify(urls)
    led = ledger_slugs()
    CAT.mkdir(exist_ok=True)
    d = today()
    snap = {"date": d, "ja": {k: sorted(v) for k, v in ja.items()}, "en_only": {k: sorted(v) for k, v in en.items()}}
    (CAT / f"snapshot-{d}.json").write_text(json.dumps(snap, ensure_ascii=False, indent=1), encoding="utf-8")
    L = [f"# 一覧の差分（{d}）", "",
         "取得元: https://academy.claude.com/sitemap.xml。台帳に足すかは人が決める（PLAYBOOK の判断の基準 7）。", ""]
    gone_all = 0
    L += ["## 台帳の対象（学習ステップの 71 ページ）", ""]
    for k in KINDS:
        gone = sorted(led.get(k, set()) - ja[k])
        gone_all += len(gone)
        L.append(f"- {k}: 台帳にあるが日本語版のサイトマップに無い {len(gone)} 件" + "".join(f"\n  - `{x}`" for x in gone))
    L += ["", "## 台帳の対象外（参考。自動では取り込まない）", ""]
    new_all = 0
    for k in KINDS:
        new = sorted(ja[k] - led.get(k, set()))
        new_all += len(new)
        L.append(f"- {k}: 日本語版で台帳に無いもの {len(new)} 件（役割別の残りのユースケースなど）")
    L += ["", f"対象の変化: 消えた {gone_all} 件（確かめる）。対象外の追加: {new_all} 件（参考）。"]
    (CAT / "latest.md").write_text("\n".join(L), encoding="utf-8")
    print("\n".join(L))
    print(f"消えた対象 {gone_all} 件、対象外の追加 {new_all} 件。詳細は catalog/latest.md")


if __name__ == "__main__":
    main()
