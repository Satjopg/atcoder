import sys

import io

_INPUT = """\
9 45000
"""

sys.stdin = io.StringIO(_INPUT)

import sys

N, Y = map(int, sys.stdin.readline().split())

for a in range(N + 1):
  for b in range(N + 1):
    c = N - (a + b)
    if c < 0:
      break
    sums = 10000 * a + 5000 * b + 1000 * c
    if a + b + c == N and sums == Y:
      print(a, b, c)
      exit(0)
print(-1, -1, -1)