import sys

import io

_INPUT = """\
10
"""

sys.stdin = io.StringIO(_INPUT)

import sys

def rec(k):
  if k == 0:
    return 1
  else:
    return k * rec(k - 1)

n = int(sys.stdin.readline())
print(rec(n))