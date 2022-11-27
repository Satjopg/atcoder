import sys

import io

_INPUT = """\
1000000000000000000 100
"""

sys.stdin = io.StringIO(_INPUT)

import sys
import math

A, B = map(int, sys.stdin.readline().split())

gsrc = ((A / (2 * B)) ** 2) ** (1/3)
g = math.ceil(gsrc)
ans = 0
  
while True:
  T = (A / (math.sqrt(g))) + (B * (g - 1))
  if ans == 0 or T < ans:
    g += 1
    ans = T
  else:
    print(format(ans, '.10f'))
    exit(0)