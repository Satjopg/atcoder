import sys

import io

_INPUT = """\
wwwvvvvvv
"""

sys.stdin = io.StringIO(_INPUT)

import sys

S = input()

cnt = 0

for s in S:
  if s == 'v':
    cnt += 1
  elif s == 'w':
    cnt += 2
print(cnt)