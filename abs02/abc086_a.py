import sys

import io

_INPUT = """\
1 30
"""

sys.stdin = io.StringIO(_INPUT)

import sys

a, b = map(int, sys.stdin.readline().split())
print('Even' if a * b % 2 == 0 else 'Odd')