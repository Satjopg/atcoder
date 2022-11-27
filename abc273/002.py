import sys

import io

_INPUT = """\
314159265358979 12
"""

sys.stdin = io.StringIO(_INPUT)

import sys
from decimal import Decimal, ROUND_HALF_UP

a, k = list(map(int, sys.stdin.readline().split()))
ans = Decimal(a)
if len(str(a)) < k:
  print(0)
else:
  for i in range(1, k + 1):
    if int(ans) == 0:
      break
    ans = ans.quantize(Decimal('1E' + str(i)), rounding = ROUND_HALF_UP)
  print(int(ans))
