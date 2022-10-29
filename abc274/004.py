import sys

import io

_INPUT = """\
3 2 7
2 7 4
"""

sys.stdin = io.StringIO(_INPUT)

import sys

n,x,y = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))

def fun(ud, p, q, i):
  if i == n and p == x and q == y:
    print('Yes')
    exit(0)
  if i >= n:
    return
  ni = i + 1
  if ud:
    if y > q:
      fun(False, p, q + a[i], ni)
    else:
      fun(False, p, q - a[i], ni)
  else:
    if x > p:
      fun(True, p + a[i], q, ni)
    else:
      fun(True, p - a[i], q, ni)

p=a[0]
q=0
fun(True, p, q, 1)
print('No')
