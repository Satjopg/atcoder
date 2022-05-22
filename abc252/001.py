from sys import stdin
import io

_INPUT = """\
97
"""

stdin = io.StringIO(_INPUT)

n=int(stdin.readline().rstrip())
print(chr(n))