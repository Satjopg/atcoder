import sys

import io

_INPUT = """\
1
3
"""

sys.stdin = io.StringIO(_INPUT)

import sys

n = int(sys.stdin.readline())
print(sum(map(int, sys.stdin.readline().split())))