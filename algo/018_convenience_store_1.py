import io
import sys

_INPUT = """\
7
100 200 300 400 400 200 300
"""

sys.stdin = io.StringIO(_INPUT)

n=int(input())
arr=list(map(int, input().split()))
tb={x: 0 for x in range(100, 500, 100)}
cnt=0
for x in arr:
  cnt+=tb[500-x]
  tb[x] += 1
print(cnt)