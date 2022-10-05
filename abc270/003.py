import sys

import io

_INPUT = """\
5 2 5
1 2
1 3
3 4
3 5
"""

sys.stdin = io.StringIO(_INPUT)

import sys
from collections import deque

deq = deque([])

def dfs(k, to):
  deq.append(k)
  for d in dc[k]:
    dfs(d)
  deq.popleft()
  return

n,x,y=list(map(int, sys.stdin.readline().split()))
dc = {k: [] for k in range(1, n+1)}
for _ in [0] * n:
  i,t = map(int, sys.stdin.readline().split())
  dc[i].push(t)
  dc[t].push(i)