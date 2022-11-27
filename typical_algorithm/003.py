import sys

import io

_INPUT = """\
4
0 3 1 4
1 0 5 9
2 6 0 5
3 5 8 0
"""

sys.stdin = io.StringIO(_INPUT)

# 巡回セールスマン問題
# 全ての地点を訪れるための最小の労力を調べる
# DP[S][v] := 集合の全体のうちの部分集合Sの順列の中で、vが末項となるもののうち、最も最適なもののコスト
import sys
import math

N = int(sys.stdin.readline())
dp = [[math.inf for _ in [0] * N] for _ in [0] * (2**N)]
costs = []
for _ in [0]*N:
  costs.append(list(map(int, sys.stdin.readline().split())))

