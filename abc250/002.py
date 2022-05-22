from sys import stdin
import io

_INPUT = """\
5 1 5
"""

stdin = io.StringIO(_INPUT)

white='.'
black='#'
n,y,x=map(int, stdin.readline().split())
table=[[white for _ in [0]*(n*x)] for _ in [0]*(n*y)]

for i in range(n*y):
  if i != 0:
    if i >= y and i % y == 0:
      if table[i-1][0] == white: table[i][0] = black
      else: table[i][0] = white
    else:
      table[i][0] = table[i-1][0]
  for j in range(1, n*x):
    if j % x == 0 and j >= x:
      if table[i][j-1] == white: table[i][j] = black
      else: table[i][j] = white
    else:
      table[i][j] = table[i][j-1]
for cl in table:
  print(''.join(cl))

# n,y,x=map(int, input().split())
# tb=[]
# w='.'
# b='#' 
# cti=0
# ctv = ''
# for i in range(0,y*n):
#   arr=[]
#   ctj = 1
#   for j in range(0,x*n):
#     if j==0:
#       if i-1 < 0:
#         arr.append(w)
#         ctv = w
#       else:
#         if cti >= y:
#           ctv = w if tb[i-1][j] != w else b
#           cti = 0
#         else:
#           ctv = tb[i-1][j]
#         arr.append(ctv)
#     else:
#       if ctj >= x:
#         ctj = 1
#         ctv = w if ctv != w else b
#       else:
#         ctj += 1
#       arr.append(ctv)
#   print(''.join(arr))
#   tb.append(arr[:])
#   cti += 1
