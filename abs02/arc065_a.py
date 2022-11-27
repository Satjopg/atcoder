import sys

import io

_INPUT = """\
dreameraser
"""

sys.stdin = io.StringIO(_INPUT)

import sys

S = input()
ss = set(['dream','dreamer', 'erase', 'eraser'])
tmp = ''

for s in reversed(S):
  tmp = s + tmp
  if len(tmp) > 7:
    break
  if tmp in ss:
    tmp = ''
if tmp == '':
  print('YES')
else:
  print('NO')