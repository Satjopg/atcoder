import sys

import io

_INPUT = """\
11
"""

sys.stdin = io.StringIO(_INPUT)

n = int(input())
nb = [True if b == '1' else False for b in format(n, 'b') ]
print(nb)
