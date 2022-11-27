import sys

import io

_INPUT = """\
aaaaa
"""

sys.stdin = io.StringIO(_INPUT)

import sys

S = input()
for ri, s in enumerate(reversed(S)):
  if s == 'a':
    print(len(S) - ri)
    exit(0)
print(-1)
