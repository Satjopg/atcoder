import sys

import io

_INPUT = """\
5 6
-2 -2 -5 -7 -15
"""

sys.stdin = io.StringIO(_INPUT)

import sys

n, m = map(int, sys.stdin.readline().split())
nl = list(map(int, sys.stdin.readline().split()))

for _ in [0] * m:
  daiji = []
  for j in range(n):
    nl[j] += j + 1
    if nl[j] >= 0 and nl[j] < n:
      daiji.append(nl[j])
  i = 0
  while True:
    if i in daiji:
        i += 1
        continue
    else:
      print(i)
      break
