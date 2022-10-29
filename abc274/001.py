import sys

import io

_INPUT = """\
1 0
"""

sys.stdin = io.StringIO(_INPUT)

import sys

a, b = list(map(int, sys.stdin.readline().split()))
print(format(b/a, '.3f'))