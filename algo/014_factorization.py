import io
import sys

_INPUT = """\
36
"""

sys.stdin = io.StringIO(_INPUT)

n=int(input())
arr=[]
i=2
x=n
while i*i <= n:
  if x % i == 0:
    while x % i == 0:
      arr.append(str(i))
      x=int(x/i)
  if x==1:
    print(' '.join(arr))
    sys.exit()
  i+=1
arr.append(str(x))
print(' '.join(arr))
