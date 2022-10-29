import sys

import io

_INPUT = """\
1 2 5 3
"""

sys.stdin = io.StringIO(_INPUT)

import sys

a,b,c,d=list(map(int, sys.stdin.readline().split()))
ans = (a + b) * (c - d)
print(ans)
print('Takahashi')