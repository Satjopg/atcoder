import sys

import io

_INPUT = """\
100 4 16
"""

sys.stdin = io.StringIO(_INPUT)

import sys

def sums(n):
  sm = 0
  for s in str(n):
    sm += int(s)
  return sm

N, A, B = map(int, sys.stdin.readline().split())
ans = 0
prev = 0

for i in range(N+1):
  if i % 10 == 0:
    prev = sums(i)
  else:
    prev += 1
  if prev >= A and prev <= B:
    ans += i
print(ans)
  