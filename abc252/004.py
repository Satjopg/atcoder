from sys import stdin
from operator import mul
from functools import reduce
import io

_INPUT = """\
10
99999 99998 99997 99996 99995 99994 99993 99992 99991 99990
"""

stdin = io.StringIO(_INPUT)

n=int(stdin.readline().rstrip())
arr=list(map(int, stdin.readline().split()))
cnt=0
for i in range(n-2):
  for j in range(i+1, n-1):
    if arr[i] == arr[j]:
      continue
    for k in range(j+1,n):
      if arr[i] != arr[k] and arr[j] != arr[k]:
        cnt+=1
print(cnt)

# cnt=0

# for x in combinations(map(int, stdin.readline().split()), 3):
#   print(x)
 