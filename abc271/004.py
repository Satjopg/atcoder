import sys
import io

_INPUT = """\
3 11
1 4
2 3
5 7
"""

sys.stdin = io.StringIO(_INPUT)

import sys

n,s=list(map(int, sys.stdin.readline().split()))
a=[]
b=[]
for _ in [0] * n:
  t,h = map(int, sys.stdin.readline().split())
  a.append(t)
  b.append(h)

# dp[i][j] = i番目のときにjになれるか
# 例: dp[1][4] = 1番目のときに4になれるか = 1枚目のコインに4が書かれているので1となる
dp=[[0 for _ in [0] * (s+1)] for _ in [0] * (n+1)]

# dp[0][0] = 0番目のときに0になれるか = 初期値の定義
dp[0][0] = 1

for i in range(n):
  for j in range(s+1):
    if dp[i][j]:
      # iが0番目のときには1枚目のコインを見る
      # しかし、1枚目のコインのindexは0になるのでi+1ではなくiをそのまま採用する
      # jに次のコインの値を足してs以下のときにはi+1番目のjに次のコインを足した数字になることができる
      if j + a[i] <= s:
        dp[i+1][j + a[i]] = 1
      if j + b[i] <= s:
        dp[i+1][j + b[i]] = 1
if dp[n][s]:
  print('Yes')
  ans = []
  for i in range(n)[::-1]:
    if s >= a[i] and dp[i][s - a[i]]:
      ans.append('H')
      s -= a[i]
    else:
      ans.append('T')
      s -= b[i]
  print(''.join(ans[::-1]))
else:
  print('No')