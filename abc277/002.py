import sys

import io

_INPUT = """\
5
00
AA
XX
YY
ZZ
"""

sys.stdin = io.StringIO(_INPUT)

import sys

n = int(sys.stdin.readline())

ft = set(['H' , 'D' , 'C' , 'S'])
sd = set(['A' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , 'T' , 'J' , 'Q' , 'K'])

st = set()
for _ in [0]*n:
  src = sys.stdin.readline()
  if not (src not in st and src[0] in ft and src[1] in sd):
    print('No')
    exit(0)
  st.add(src)
print('Yes')