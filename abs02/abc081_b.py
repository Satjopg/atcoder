import sys

import io

_INPUT = """\
6
382253568 723152896 37802240 379425024 404894720 471526144
"""

sys.stdin = io.StringIO(_INPUT)

import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
ans = 0
flg = True

while flg:
  for i in range(N):
    next = int(A[i] / 2)
    mod = int(A[i] % 2)
    if mod == 1:
      flg = False
    A[i] = next
  if flg:
    ans += 1
print(ans)