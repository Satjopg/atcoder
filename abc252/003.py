from sys import stdin
import io

_INPUT = """\
3
1937458062
8124690357
2385760149
"""

stdin = io.StringIO(_INPUT)

n=int(stdin.readline().rstrip())
arr=[stdin.readline().rstrip() for _ in [0]*n]

cnt=[[0 for _ in [0]*10]for _ in [0]*10]

for i in range(n):
  for j in range(10):
    cnt[int(arr[i][j])][j] = cnt[int(arr[i][j])][j] + 1

for j in range(10):
  print(cnt[j])

mx=[0 for i in range(10)]
for i in range(10):
  for j in range(10):
    mx[i]=max(mx[i], 10 * (cnt[i][j] - 1) + j)
print(min(mx))