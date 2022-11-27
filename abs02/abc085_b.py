import sys

import io

_INPUT = """\
3
15
15
15
"""

sys.stdin = io.StringIO(_INPUT)

import sys

N = int(input())
ans = set()
for _ in [0]*N:
  ans.add(int(sys.stdin.readline()))
print(len(ans))