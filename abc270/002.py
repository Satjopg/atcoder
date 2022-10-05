import sys

import io

_INPUT = """\
100 1 1000
"""

sys.stdin = io.StringIO(_INPUT)

import sys

x,y,z=list(map(int, sys.stdin.readline().split()))

if x > 0:
  if y > x or y < 0:
    print(abs(x))
  else:
    if z > 0 and y > z:
      print(abs(x))
    elif z < 0 and y > z:
      print(abs(x) + abs(z) * 2)
    else:
      print(-1)
else:
  if x > y or y > 0:
    print(abs(x))
  else:
    if z < 0 and y < z:
      print(abs(x))
    elif z > 0 and y < z:
      print(abs(x) + abs(z) * 2)
    else:
      print(-1)

