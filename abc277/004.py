import sys

import io

_INPUT = """\
1 10
4
"""
import sys
sys.stdin = io.StringIO(_INPUT)

import sys
from collections import defaultdict

cards = defaultdict(lambda:0)
n, m = map(int, sys.stdin.readline().split())
sum = 0
anss = []

for i in list(map(int, sys.stdin.readline().split())):
  sum += i
  cards[i] += 1

for val in cards:
  ans = sum - (val * cards[val])
  field = {val}
  next = (val + 1) % m
  while next not in field and next in cards:
    field.add(next)
    ans = ans - (next * cards[next])
    next = (next + 1) % m
  anss.append(ans)

print(min(anss))
