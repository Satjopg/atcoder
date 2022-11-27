import sys

import io

_INPUT = """\
72
128 256
myonmyon
"""

sys.stdin = io.StringIO(_INPUT)

import sys

a = int(sys.stdin.readline())
b, c = map(int, sys.stdin.readline().split())
s = input()

print(a + b + c, s)
