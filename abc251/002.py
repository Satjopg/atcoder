from sys import stdin
import io

_INPUT = """\
7 251
202 20 5 1 4 2 100
"""

stdin = io.StringIO(_INPUT)

# srr=set()
# cnt=0

# def search(d, s, i):
#   global cnt
#   global srr
#   if d==3:
#     if s <= w and s not in srr:
#       srr.add(s)
#       cnt+=1
#     return
#   if i==len(arr):
#     if d!=0 and s <= w and s not in srr:
#       srr.add(s)
#       cnt+=1
#     return
#   search(d, s, i+1)
#   search(d+1, s+arr[i], i+1)
#   return

n,w=list(map(int, stdin.readline().split()))
arr=list(map(int, stdin.readline().split()))

flags=[False for _ in [0]*(w+1)]
for i in range(n):
  s = arr[i]
  if s <= w:
    flags[s] = True

for i in range(n):
  for j in range(i+1,n):
    s = arr[i] + arr[j]
    if s <= w:
      flags[s] = True

for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      s = arr[i] + arr[j] + arr[k]
      if s <= w:
        flags[s]=True

print(flags.count(True))

# 場合の数パターン. 今回の場合1,2,3でやったほうが簡単だし早い。
# search(0, 0, 0)
# print(cnt)