import sys

import io

_INPUT = """\
1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000
"""

sys.stdin = io.StringIO(_INPUT)

import sys

a,b,c,d,e,f = map(int, sys.stdin.readline().split())

print(((a*b*c)-(d*e*f)) % 998244353)