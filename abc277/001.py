import sys

import io

_INPUT = """\
6 6
1 2 3 4 5 6
"""

sys.stdin = io.StringIO(_INPUT)

import sys

n, x = list(map(int, sys.stdin.readline().split()))
for i, v in enumerate(list(map(int, sys.stdin.readline().split()))):
  if x == v:
    print(i + 1)