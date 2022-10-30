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

S = [sys.stdin.readline() for _ in range(9)]
ans = 0
# 4点を決めるのではなく2点を固定して考える。※ 4点では条件が難しすぎるので固定して決めていくのは定石である
# itertools.productは指定した配列の要素のすべての場合の数を求めることができる。
# 今回の場合同一の点を含むすべての2点の組み合わせをこれで求めることができる
for y1, x1, y2, x2 in itertools.product(range(9), repeat = 4):
  # 真下 or 右下の向きのベクトルを作れる2点を求める
  if S[y1][x1]=="#" and S[y2][x2]=="#" and x2 >= x1 and y2 > y1:
    # 右に90°回す形で点を求めていく
    dx = x2 - x1 # 横方向の長さ
    dy = y2 - y1 # 縦方向の長さ
    x3 = x2 - dy # 縦方向分横へ戻る
    y3 = y2 + dx # 横方向分進む
    x4 = x3 - dx # 横方向分戻る
    y4 = y3 - dy # 縦方向分戻る
    # 求めた2点が描画範囲にあるかつポーンがおかれているかをチェックし満たしていれば正方形としてカウントする
    if 0 <= y3 < 9 and 0 <= x3 < 9 and 0<= y4 < 9 and 0 <= x4 < 9 and S[y3][x3]=="#" and S[y4][x4]=="#":
      ans += 1
print(ans)
