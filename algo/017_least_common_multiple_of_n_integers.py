from functools import reduce
import io
import sys

_INPUT = """\
3
12 18 14
"""

sys.stdin = io.StringIO(_INPUT)

def gcd(a, b):
  if b == 0: return a
  else: return gcd(b, a % b)

def lcm(a, b):
  # 最大公約数が求まると最大公倍数が求まる
  g = gcd(a, b)
  return int(a / g * b)

n=int(input())
arr=list(map(int, input().split()))
r=arr[0]
for x in arr[1:]:
  r=lcm(r, x)
print(r)