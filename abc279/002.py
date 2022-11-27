import sys

import io

_INPUT = """\
toyotasystems
toyotasystems
"""

sys.stdin = io.StringIO(_INPUT)

import sys

S = input()
T = input()

if T in S:
  print('Yes')
else:
  print('No')
