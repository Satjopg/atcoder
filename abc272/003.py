import sys

import io

_INPUT = """\
2
1 0
"""

sys.stdin = io.StringIO(_INPUT)

import sys

o1 = -1
o2 = -1
e1 = -1
e2 = -1

n = int(sys.stdin.readline())

for ms in sys.stdin.readline().split():
  m = int(ms)
  if m % 2 == 0:
    if m > e1:
      e2 = e1
      e1 = m
    elif m < e1 and m > e2:
      e2 = m
    else:
      continue
  else:
    if m > o1:
      o2 = o1
      o1 = m
    elif m < o1 and m > o2:
      o2 = m
    else:
      continue

osum = o1 + o2 if o1 > -1 and o2 > -1 else -1
esum = e1 + e2 if e1 > -1 and e2 > -1 else -1

if osum > esum:
  print(osum)
else:
  print(esum)
