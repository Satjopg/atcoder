import sys

import io

_INPUT = """\
1000000000000000000
"""

sys.stdin = io.StringIO(_INPUT)

import sys
import math

st = set()
dic = dict()

def rec(n):
  if n == 0:
    return 1
  if n in st:
    return dic[n]
  l = math.floor(n / 2)
  la = rec(l)
  if l not in st:
    st.add(l)
    dic[l] = la
  r = math.floor(n / 3)
  ra = rec(r)
  if r not in st:
    st.add(r)
    dic[r] = ra
  return la + ra

n = int(sys.stdin.readline())
print(rec(n))
