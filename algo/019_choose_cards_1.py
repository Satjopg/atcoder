import io
import sys

_INPUT = """\
6
1 3 2 1 1 2
"""

sys.stdin = io.StringIO(_INPUT)

n=int(input())
tb={x:0 for x in range(1,4)}
cnt=0
for c in list(map(int, input().split())):
  cnt+=tb[c]
  tb[c]+=1
print(cnt)
