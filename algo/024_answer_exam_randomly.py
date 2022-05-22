from sys import stdin


n=int(stdin.readline())
ex=0
for _ in [0]*n:
  p,q=map(int, stdin.readline().split())
  ex+=(q/p)
print(ex)