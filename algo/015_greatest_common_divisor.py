import io
import sys

_INPUT = """\
33 88
"""

sys.stdin = io.StringIO(_INPUT)

def gcd(a, b):
  if b == 0: return a
  else: return gcd(b, a % b)

a,b=list(map(int, input().split()))
print(gcd(a, b))

## 初期状態(ユークリッド互除法知らんとき)
# a,b=list(map(int, input().split()))
# i=1
# r=1
# # 小さい方の数の約数のうち大きい方の数も割れた数の最大を求める
# n = a if b > a else b
# while i ** 2 <= n:
#   if i > r and a % i == 0 and b % i == 0:
#     r = i
#   if int(n/i) > r and a % int(n/i) == 0 and b % int(n/i) == 0:
#     r = int(n/i)
#   i += 1
# print(r)