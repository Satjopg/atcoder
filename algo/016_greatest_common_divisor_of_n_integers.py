import io
import sys

_INPUT = """\
3
12 18 24
"""

sys.stdin = io.StringIO(_INPUT)

def gcd(a, b):
  # 初期状態がb>aだとしても次の呼び出しで引数が逆転するから問題なし
  if b == 0: return a
  else: return gcd(b, a % b)

n=int(input())
arr=list(map(int, input().split()))
r=arr[0]
for x in arr[1:]:
  r=gcd(r, x)
print(r)