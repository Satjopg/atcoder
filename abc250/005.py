import io
import sys

_INPUT = """\
5
1 2 3 4 5
1 2 2 4 3
7
1 1
2 2
2 3
3 3
4 4
4 5
5 5
"""

sys.stdin = io.StringIO(_INPUT)

n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
q=int(input())
arr=[tuple(map(int, input().split())) for _ in [0]*q]

for x,y in arr:
  sa = set(a[:x])
  sb = set(b[:y])
  print('Yes' if sb == sa else 'No')
