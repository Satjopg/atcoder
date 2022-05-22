from sys import stdin
import io

_INPUT = """\
10
bb 3
ba 1
aa 4
bb 1
ba 5
aa 9
aa 2
ab 6
bb 5
ab 3
"""

stdin = io.StringIO(_INPUT)

srr=set()
mx=0
mst=0
n=int(stdin.readline())
for i in range(n):
  s,t=stdin.readline().split()
  if s not in srr:
    srr.add(s)
    if int(t) > mx:
      mx = int(t)
      mst = i+1
print(mst)
