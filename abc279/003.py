import sys

import io

_INPUT = """\
8 7
#..#..#
.##.##.
#..#..#
.##.##.
#..#..#
.##.##.
#..#..#
.##.##.
....###
####...
....###
####...
....###
####...
....###
####...
"""

sys.stdin = io.StringIO(_INPUT)

import sys

H, W = map(int, sys.stdin.readline().split())

cntS = []

for s in [0]*H:
  cntS.append(input().count('#'))
for i in range(0, H):
  if cntS[i] != input().count('#'):
    print('No')
    exit(0)
print('Yes')