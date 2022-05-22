from sys import stdin

# Python標準のsort or sortedのが早いんでそれ使う
# これはマージソートを実装する問題なのでマージソートを実装した

def sort(l):
  if len(l) == 1:
    return l
  ll=sort(l[:int(len(l)/2)])
  rl=sort(l[int(len(l)/2):])
  return merge(ll, rl)

def merge(ll, rl):
  i=0
  j=0
  sl=[]
  while i < len(ll) and j < len(rl):
    if ll[i] < rl[j]:
      sl.append(ll[i])
      i+=1
    else:
      sl.append(rl[j])
      j+=1
  return sl+ll[i:] if i < len(ll) else sl+rl[j:]

n=int(stdin.readline())
arr=list(map(int, stdin.readline().split()))
print(' '.join(map(str, sort(arr))))