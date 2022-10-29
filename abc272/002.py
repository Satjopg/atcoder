import sys

import io

_INPUT = """\
3 3
2 1 2
2 2 3
2 1 3
"""

sys.stdin = io.StringIO(_INPUT)

import sys
import math

def comb(n, r):
  return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


n, m = map(int, sys.stdin.readline().split())
hash = [[False for _ in [0] * n] for _ in [0] * n]
tc = 0
maxtc = comb(n, 2)

for _ in [0]*m:
  nl = list(map(int, sys.stdin.readline().split()))
  for i in range(1, nl[0]):
    for j in range(i + 1, nl[0] + 1):
      if not hash[nl[i] - 1][nl[j] - 1]:
        hash[nl[i] - 1][nl[j] - 1] = True
        hash[nl[j] - 1][nl[i] - 1] = True
        tc += 1
    if tc >= maxtc:
      print('Yes')
      exit(0)
print('No')