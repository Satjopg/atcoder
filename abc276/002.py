import sys

import io

_INPUT = """\
5 10
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5
"""

sys.stdin = io.StringIO(_INPUT)

import sys

n, m = list(map(int, sys.stdin.readline().split()))
ans = {i + 1: [] for i in range(n)}
for _ in [0]*m:
  a, b = list(map(int, sys.stdin.readline().split()))
  ans[a].append(b)
  ans[b].append(a)
for k in range(n):
  an = sorted(ans[k+1])
  print(len(ans[k+1]), ' '.join(map(str, an)))
