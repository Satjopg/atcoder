import sys
import io

_INPUT = """\
2 2
3 1 4 7
2 5 9
1 3
2 1
"""

sys.stdin = io.StringIO(_INPUT)

n,q=list(map(int, sys.stdin.readline().split()))
arr=[list(map(int, sys.stdin.readline().rstrip().split(' ')))[1:] for _ in [0]*n]

for _ in [0]*q:
  i, j = map(int, sys.stdin.readline().rstrip().split(' '))
  print(arr[i-1][j-1])