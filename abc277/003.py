import sys

import io

_INPUT = """\
6
1 3
1 5
1 12
3 5
3 12
5 12
"""
import sys
sys.stdin = io.StringIO(_INPUT)

# 以下幅優先探索

# import sys
# from collections import defaultdict, deque

# n = int(sys.stdin.readline())
# graph = defaultdict(list)
# for _ in [0] * n:
#   a, b = map(int, sys.stdin.readline().split())
#   graph[a].append(b)
#   graph[b].append(a)

# que = deque()
# que.append(1)
# S = {1}
# while que:
#   val = que.popleft()
#   for i in graph[val]:
#     if i not in S:
#       que.append(i)
#       S.add(i)
# print(max(S))

# 以下深さ優先探索

import sys
from collections import defaultdict
# 再帰呼び出しのときには絶対忘れない頼む。。。
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
graph = defaultdict(list)
reached = set()

for _ in [0] * n:
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)


def dfs(now):
  reached.add(now)
  for next in graph[now]:
    if next not in reached:
      dfs(next)

dfs(1)
print(max(reached))