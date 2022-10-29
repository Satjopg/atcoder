import sys

import io

_INPUT = """\
5 47
.#..#..#####..#...#..#####..#...#...###...#####
.#.#...#.......#.#...#......##..#..#...#..#....
.##....#####....#....#####..#.#.#..#......#####
.#.#...#........#....#......#..##..#...#..#....
.#..#..#####....#....#####..#...#...###...#####
"""

sys.stdin = io.StringIO(_INPUT)

import sys

h, w = list(map(int, sys.stdin.readline().split()))
ans=[0 for _ in [0]*w]
for _ in [0]*h:
  for i, s in enumerate(sys.stdin.readline()):
    if s == '#':
      ans[i] += 1
print(' '.join(map(str, ans)))
