from functools import lru_cache
import sys

import io

_INPUT = """\
100000000000000000000
"""

sys.stdin = io.StringIO(_INPUT)

import sys
import math

# st = set()
# dic = dict()

# def rec(n):
#   if n == 0:
#     return 1
#   if n in st:
#     return dic[n]
#   l = math.floor(n / 2)
#   la = rec(l)
#   if l not in st:
#     st.add(l)
#     dic[l] = la
#   r = math.floor(n / 3)
#   ra = rec(r)
#   if r not in st:
#     st.add(r)
#     dic[r] = ra
#   return la + ra

# Pythonのメモ化はlru_cacheを利用することで簡単にかける
# 同一プロセス中引数が同じものはキャッシュから結果を返却する
# 上記のコメントされているコードと以下コードは同じことをやっている
@lru_cache(None)
def rec(n):
  if n == 0:
    return 1
  return rec(n // 2) + rec(n // 3)

n = int(sys.stdin.readline())
print(rec(n))
