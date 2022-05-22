from sys import stdin
n,r=map(int, stdin.readline().split())
de=1
nf=1
for i in range(r):
  nf*=n-i
  de*=i+1
print(int(nf/de))
