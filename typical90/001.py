import sys

import io

_INPUT = """\
20 1000
4
51 69 102 127 233 295 350 388 417 466 469 523 553 587 720 739 801 855 926 954
"""

sys.stdin = io.StringIO(_INPUT)

# 「答え」を二分探索する問題
# 範囲を「半分の値=基準値」で割って探索するのが二分探索
# 今回の場合、スコアの値は0以上L以下と最大と最小が決まっているのでこれの半分であるM以上の値は満たすかを調べていくことで求められる
import sys

N, L = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# ここは探索条件によって変わる
def solve(mid):
  cnt = 0
  prev = 0
  for ai in A:
    # 前に切った場所から基準値以上の値かつ残りも基準値以上残っているときはその場所で切る
    if ai - prev >= mid and L - ai >= mid:
      cnt += 1
      prev = ai
  # K個以上分割できればOK
  if cnt >= K:
    return True
  else:
    return False


# 最初の境界値
ng = -1
ok = L + 1

while abs(ok - ng) > 1:
  mid = int((ok + ng) / 2) 
  print(ng, mid, ok) 
  if(solve(mid)):
    ng = mid
  else:
    ok = mid

print(ok)
