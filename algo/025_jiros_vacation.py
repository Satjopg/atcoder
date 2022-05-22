from sys import stdin

ex=0
n=int(stdin.readline())
for a,b in zip(stdin.readline().split(), stdin.readline().split()):
  ex+=int(a)/3+int(b)*2/3
print(ex)