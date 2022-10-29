import sys

import io

_INPUT = """\
2
1 2
"""

sys.stdin = io.StringIO(_INPUT)

import sys

n = int(sys.stdin.readline())
ans = [0 for _ in [0]*(2 * n + 1)]

for i, v in enumerate(map(int, sys.stdin.readline().split())):
  ans[2 * (i+1) - 1] = ans[v-1] + 1
  ans[2 * (i+1)] = ans[v-1] + 1

for a in ans:
  print(a)
