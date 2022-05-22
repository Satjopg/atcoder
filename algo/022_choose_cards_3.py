from sys import stdin
n=int(stdin.readline())
tb={}
cnt=0
for x in map(int, stdin.readline().split()):
  cnt+=tb.get(100000-x, 0)
  tb[x]=tb.get(x,0)+1
print(cnt)
