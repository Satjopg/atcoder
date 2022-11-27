import sys

import io

_INPUT = """\
10
9 8 6 5 10 3 1 2 4 7
"""

sys.stdin = io.StringIO(_INPUT)

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
