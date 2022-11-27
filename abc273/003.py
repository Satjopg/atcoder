import sys

import io

_INPUT = """\
6
2 7 1 8 2 8
"""

sys.stdin = io.StringIO(_INPUT)

import sys
import bisect

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
anss = [0] * n
sort_A = sorted(list(set(A)))

for i in range(n):
  ans = len(sort_A) - 1 - bisect.bisect_left(sort_A, A[i])
  anss[ans] += 1
print(*anss, sep='\n')


# st = set()
# d = {}
# ml = []

# for i, a in enumerate(A):
#   if a in st:
#     d[a] += 1
#   elif len(ml) == 0:
#     ml.append(a)
#     d[a] = 1
#     st.add(a)
#   else:
#     d[a] = 1
#     st.add(a)
#     ct = len(ml) - 1
#     for j, m in enumerate(ml):
#       if a > m:
#         ml.insert(j, a)
#         break
#       elif j == ct:
#         ml.append(a)

# cml = len(ml)

# for i in range(n):
#   if cml > i:
#     print(d[ml[i]])
#   else:
#     print(0)
