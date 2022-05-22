n,s=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]

dp=[[0 for _ in [0] * (s+1)] for _ in [0] * (n+1)]
for y in range(1,n+1):
  for x in range(1, s+1):
    if x - arr[y-1] >= 0:
      dp[y][x] = arr[y-1] + dp[y-1][x - arr[y-1]] if arr[y-1] + dp[y-1][x - arr[y-1]] > dp[y-1][x] else dp[y-1][x]
    else:
      dp[y][x] = dp[y-1][x]
print('Yes' if dp[n][s] == s else 'No')