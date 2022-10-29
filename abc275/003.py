import sys

import io

_INPUT = """\
##.......
##.......
.........
.......#.
.....#...
........#
......#..
.........
.........
"""

sys.stdin = io.StringIO(_INPUT)

import sys
import itertools

S=[input() for _ in range(9)]
ans=0

for i1,j1,i2,j2 in itertools.product(range(9),repeat=4):
  if i2>i1 and j2>=j1 and S[i1][j1]=="#" and S[i2][j2]=="#":
    print(i1,j1,i2,j2)
