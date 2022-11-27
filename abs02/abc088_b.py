import sys

import io

_INPUT = """\
4
20 18 2 18
"""

sys.stdin = io.StringIO(_INPUT)

import sys
N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

index = 0
ALICE = 0
BOB = 0

for i in range(1, N+1):
  if i % 2 == 1:
    ALICE += A[index]
  else:
    BOB += A[index]
  index += 1

print(abs(ALICE-BOB))