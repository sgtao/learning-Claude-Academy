#!/usr/bin/env python3
"""学習の案内：次に学ぶ 1 件を決める（PLAYBOOK の判断の基準 8 を、そのまま書いた規則）。

使い方:
  python3 tools/guide.py --role 営業 --minutes 30 --plan 無料          台帳の学習済みの日から決める
  python3 tools/guide.py --role 営業 --minutes 30 --plan 無料 --learned 0-3,1-1   学習済みの ID を直接渡す（検査用）

規則（上から順に）:
  1. 何も学んでいなければ、ステップ 0 の 0-3（Intro to Claude、5 分）を勧める（時間が 5 分以上あるとき）。
  2. 最短ルートの順に見る：L1 1-1, L2 1-2, L3 1-3, L5 1-5, L6 1-6, Customize Claude 0-6, 役割の★1〜★3。
     未学習で、時間内に収まり、プランで使えるものの最初の 1 件を勧める。
  3. プランの制限：無料は 1-9（Enterprise Search・Team/Enterprise）と 1-10（リサーチ・有料）を飛ばす。Pro は 1-9 を飛ばす。
  4. 役割が分からないときは、役割の 1 問を聞く（この script は理由を "need_role" で返す）。
  5. 候補が無いときは None（時間が足りない、または全部学習済み）。
終了コード: 0＝決まった / 1＝候補なし / 2＝引数の誤り
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import read_ledger

ROLE_NN = {"マーケティング": "01", "営業": "02", "オペレーション": "03", "人事": "04", "プロダクト": "05",
           "デザイン": "06", "財務": "07", "法務": "08", "研究": "09", "エンジニアリング": "10", "データ": "11"}
INTRO, CUSTOMIZE = "0-3", "0-6"
ROUTE = ["1-1", "1-2", "1-3", "1-5", "1-6"]
EXCLUDE = {"無料": {"1-9", "1-10"}, "Pro": {"1-9"}, "Team": set(), "Enterprise": set()}


def minutes_of(rows):
    return {r["id"]: (int(r["minutes"]) if (r.get("minutes") or "").isdigit() else None) for r in rows}


def recommend(role, minutes, plan, learned, rows):
    """(ID, 理由) を返す。候補が無ければ (None, 理由)。"""
    mins = minutes_of(rows)
    titles = {r["id"]: r["title"] for r in rows}
    if not learned:                                   # 規則 1
        if mins.get(INTRO) and minutes >= mins[INTRO]:
            return INTRO, "何も学んでいないので、入口の Intro to Claude（約 5 分）から"
        return None, "入口（5 分）も入らない時間"
    if plan not in EXCLUDE:
        return None, f"プランの指定が分からない: {plan}"
    if not role or role not in ROLE_NN:
        return None, "need_role（役割を 1 問聞く）"
    nn = ROLE_NN[role]
    seq = ROUTE[:] + [CUSTOMIZE, f"3-{nn}-02", f"3-{nn}-03", f"3-{nn}-04"]   # 規則 2 の順
    for i in seq:
        if i in learned or i in EXCLUDE[plan]:
            continue
        m = mins.get(i)
        if m is None or m > minutes:
            continue
        note = "" if i not in EXCLUDE[plan] else ""
        return i, f"最短ルートの未学習・{minutes} 分に収まる（{titles.get(i, '')}）"
    return None, f"{minutes} 分内に、未学習で使える最短ルートの項目が無い"


def learned_from_ledger():
    _, rows = read_ledger()
    return {r["id"] for r in rows if (r.get("learned_on") or "").strip()}, rows


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit(2)
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    try:
        minutes = int(opt("--minutes", "0"))
    except ValueError:
        print("--minutes は整数"); sys.exit(2)
    role, plan = opt("--role"), opt("--plan", "無料")
    if "--learned" in a:
        learned = set(x for x in opt("--learned").split(",") if x)
        _, rows = read_ledger()
    else:
        learned, rows = learned_from_ledger()
    rid, why = recommend(role, minutes, plan, learned, rows)
    title = next((r["title"] for r in rows if r["id"] == rid), "") if rid else ""
    print(f"ID={rid or 'None'}\t{title}\t理由: {why}")
    sys.exit(0 if rid else 1)


if __name__ == "__main__":
    main()
