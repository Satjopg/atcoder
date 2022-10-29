import sys

import io

_INPUT = """\
3
50 80 70
"""

sys.stdin = io.StringIO(_INPUT)

import sys

n = int(sys.stdin.readline())
ai = -1
a = -1
for i, v in enumerate(map(int, sys.stdin.readline().split())):
  if v > a:
    a = v
    ai = i + 1
print(ai)