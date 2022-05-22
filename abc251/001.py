import io
import sys

_INPUT = """\
zz
"""

sys.stdin = io.StringIO(_INPUT)

s=input()
n=int(6/len(s))
print(s*n)
