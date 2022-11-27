import sys

import io

_INPUT = """\
000
"""

sys.stdin = io.StringIO(_INPUT)

import sys

cnt = 0
for s in input():
  if s == '1': cnt += 1
print(cnt)