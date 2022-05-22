from sys import stdin
import io

_INPUT = """\
10 6
1
5
2
9
6
6
"""

stdin = io.StringIO(_INPUT)

n,q = map(int, stdin.readline().split())
arr = [int(stdin.readline().rstrip()) for _ in [0]*q]
position = [i-1 for i in range(0,n+1)]
target = list(range(1, n+1))

for x in arr:
  if position[x] != n - 1:
    # 変更対象と右隣の値を入れ替える
    target[position[x]], target[position[x]+1] = target[position[x]+1], target[position[x]]
    # 元右隣の値を記憶する(変更対象のポジションにはスワップ対象の値が格納される)
    y = target[position[x]]
    # 変更対象と元右隣の値の記録している位置を入れ替える
    position[x], position[y] = position[y], position[x]
  else:
    # 変更対象と左隣の値を入れ替える
    target[position[x]], target[position[x]-1] = target[position[x]-1], target[position[x]]
    # 元左隣の値を記憶する(変更対象のポジションにはスワップ対象の値が格納される)
    y = target[position[x]]
    # 変更対象と元左隣の値の記録している位置を入れ替える
    position[x], position[y] = position[y], position[x]
print(' '.join([str(x) for x in target]))
    


# n,q=map(int, input().split())
# arr=[int(input()) for _ in [0] * q]

# idx={x:x-1 for x in range(1,n+1)}
# r=list(idx.keys())
# for x in arr:
#   if idx[x] == len(r)-1:
#     tmp=r[idx[x]]
#     tix = idx[x]
#     idx[x] = idx[x] - 1
#     idx[r[tix-1]] = idx[r[tix-1]] + 1
#     r[tix] = r[tix-1]
#     r[tix-1] = tmp
#   else:
#     tmp = r[idx[x]]
#     tix = idx[x]
#     idx[x] = idx[x] + 1
#     idx[r[tix+1]] = idx[r[tix+1]] - 1
#     r[tix] = r[tix+1]
#     r[tix+1] = tmp
# print(' '.join([str(x) for x in r]))