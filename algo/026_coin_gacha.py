from sys import stdin

n=int(stdin.readline())
ex=0
for x in range(1, n+1):
  ex+=(1/x)
print(n*ex)