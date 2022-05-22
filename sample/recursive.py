import io
import sys

_INPUT = """\
4 11
3 1 4 5
"""
sys.stdin = io.StringIO(_INPUT)

n,s=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]

def recursive(z, r, x):
  if z > n:
    return False
  if r + x == s:
    return True
  elif r + x > s:
    return False
  for y in arr:
    if recursive(z+1, r+x, y):
      return True
  return False

for x in arr:
  if recursive(1, 0, x):
    print('Yes')
    sys.exit()
print('No')
