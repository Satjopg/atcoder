import sys
import io

_INPUT = """\
2 1
100 1
2
"""

sys.stdin = io.StringIO(_INPUT)

## B問題はあまり計算量を考えなくて良い. 以下で十分いける.

n,k=list(map(int, sys.stdin.readline().split()))
arr=list(map(int, sys.stdin.readline().split()))
mx=max(arr)
for i in map(int, sys.stdin.readline().split()):
  if arr[i-1] == mx:
    print('Yes')
    sys.exit()
print('No')

# 以下は難しく考えすぎ。

# mxs = set()
# mx=0

# for i, x in enumerate(map(int, sys.stdin.readline().split())):
#   if x > mx:
#     mx = x
#     mxs = {i+1}
#   elif x == mx:
#     mxs.add(i+1)

# for y in map(int, sys.stdin.readline().split()):
#   if y in mxs:
#     print('Yes')
#     sys.exit()

# print('No')
