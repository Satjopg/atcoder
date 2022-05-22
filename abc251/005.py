from sys import stdin
import io

_INPUT = """\
20
29 27 79 27 30 4 93 89 44 88 70 75 96 3 78 39 97 12 53 62
"""

stdin = io.StringIO(_INPUT)

a=set()
n=int(stdin.readline())
arr=list(map(int, stdin.readline().split()))
dp=[[0 for _ in [0]*2] for _ in [0]*n]
