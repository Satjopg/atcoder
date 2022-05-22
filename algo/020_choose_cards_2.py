import io
import sys

_INPUT = """\
13
243 156 104 280 142 286 196 132 128 195 265 300 130
"""

sys.stdin = io.StringIO(_INPUT)

# n=int(input())
# cards=list(map(int, input().split()))
# cnt=0

N=int(input())
A = list(map(int, input().split()))
W=1000
dp = [[0] * (W + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i, x in enumerate(A):
    for j in range(W + 1):
        dp[i + 1][j] += dp[i][j]
        if j - x >= 0:
            dp[i + 1][j] += dp[i][j - x]

print(dp)

# def search(d, s, i):
#   global cnt
#   if d == 5:
#     if s == 1000:
#       cnt+=1
#       return
#     return
#   if s >= 1000 or i == len(cards):
#     return
#   search(d, s, i+1)
#   search(d+1, s+cards[i], i+1)
#   return

# search(0, 0, 0)
# print(cnt)
