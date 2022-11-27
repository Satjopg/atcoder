import sys

import io

_INPUT = """\
30
40
50
6000
"""

sys.stdin = io.StringIO(_INPUT)

import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
X = int(sys.stdin.readline())

max = A * 500 + B * 100 + C * 50
ans = 0

if max >= X:
  for a in range(A+1):
    for b in range(B+1):
      for c in range(C+1):
        sum = a * 500 + b * 100 + c * 50
        if sum == X:
          ans += 1
          break
        if sum > X:
          break
print(ans)