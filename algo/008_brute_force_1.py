n,s=[int(x) for x in input().split()]
d=[[False for _ in [0]*n] for _ in [0]*n]
cnt=0
for x in range(n):
  for y in range(n):
    if (x+1)+(y+1) <= s:
      d[x][y]=True
    else:
      break
  cnt+=sum(d[x])
print(cnt)
