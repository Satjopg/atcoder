import sys

import io

_INPUT = """\
6
1 
"""

sys.stdin = io.StringIO(_INPUT)

import sys
import math
from functools import lru_cache

@lru_cache
def cnt(k, mp):
  cnt = 0
  src = k
  while src > mp:
    if src % 2 == 0:
      src = src / 2
    elif src % 3 == 0:
      src = src / 3
    else:
      print(-1)
      exit(0)
    cnt += 1
  return cnt

@lru_cache
def is_prime(k):
  if k == 1: return False
  for l in range(2, int(math.sqrt(k)) + 1):
    if k % l == 0:
      return False
  return True

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
st = set(A)
mnp = -1
prc = 0

if len(st) == 1:
  print(0)
  exit(0)

for j in A:
  ip = is_prime(j)
  if ip:
    prc += 1
  if prc > 1:
    print(-1)
    exit(0)
  if mnp == -1 or j == 1 or (mnp > j and ip):
    mnp = j

ans = 0
for s in A:
  if s == mnp:
    continue
  ans += cnt(s, mnp)
print(ans)
