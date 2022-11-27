import sys

import io

_INPUT = """\
4
10 20
12 15
15 18
20 22
"""

sys.stdin = io.StringIO(_INPUT)

# 区間スケジューリング問題
# 終了日が早い順に埋めていく
import sys

N = int(sys.stdin.readline())
tasks = {}
for _ in [0] * N:
  s, e = map(int, sys.stdin.readline().split())
  tasks[e] = s

ends = sorted(list(tasks.keys()))
ans = 0
last = 0
for end in ends:
  start = tasks[end]
  if start > last:
    ans += 1
    last = end
print(ans)
