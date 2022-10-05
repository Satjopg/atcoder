import sys

import io

_INPUT = """\
4 5
"""

sys.stdin = io.StringIO(_INPUT)

import sys

a,b=list(map(int, sys.stdin.readline().split()))
print(a|b) 