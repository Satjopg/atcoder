import sys

import io

_INPUT = """\
5 11
abcabbbbcac
cbabcbbbcac
abcbabbbcac
ccbcbbbbcac
bbbabbbbcac
bca
"""

sys.stdin = io.StringIO(_INPUT)

import sys

def right(nw, h, mv):
  tmp_str = ''
  for mw in range(0, mv + 1):
    if nw + mw > w:
      break
    tmp_str += fields[h][nw + mw]
  return tmp_str

def down(w, nh, mv):
  tmp_str = ''
  for mh in range(0, mv + 1):
    if nh + mh > h:
      break
    if nh + mh == nh:
      continue
    tmp_str += fields[nh + mh][w]
  return tmp_str

h, w = map(int, sys.stdin.readline().split())
fields = []
for i in range(h):
  tmp = []
  line = input()
  for ln in range(len(line)):
    tmp.append(line[ln])
  fields.append(tmp)
t = input()
ans = 0
for hi in range(h):
  for wj in range(w):
    if fields[hi][wj] != t[0]:
      continue
    for mv in range(len(t)):
      if wj + mv < w:
        tmp_r = right(wj, hi, mv)
        if len(tmp_r) == len(t):
          if tmp_r == t:
            ans += 1
          continue      
        if hi + (len(t) - len(tmp_r)) < h:
          tmp_d = down(wj + mv, hi, len(t) - len(tmp_r))
          if tmp_r + tmp_d == t:
            ans += 1
print(ans)