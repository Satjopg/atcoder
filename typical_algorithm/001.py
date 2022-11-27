import sys

import io

_INPUT = """\
9 4
1 3 5 7 9 11 13 15
"""

sys.stdin = io.StringIO(_INPUT)

# Aは必ず小さい順に並んでいる
# Ai >= K であるようなiのうち「最小」のものを出力する
import sys

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

def solve(mid):
  if A[mid] >= K:
    return True
  else:
    return False

#  条件を満たす最小のindexを求める場合の初期値
#  最小が一番右のindexの可能性があるためokは右にはみ出す
#  すべての値が条件を満たす可能性もあるためngは左にはみ出す
ok = len(A)
ng = -1

while abs(ng - ok) > 1:
  mid = int((ok + ng) / 2)
  if (solve(mid)):
    ok = mid
  else:
    ng = mid

if ok >= 0 and ok < len(A):
  print(ok)
else:
  print(-1)