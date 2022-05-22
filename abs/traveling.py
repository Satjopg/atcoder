n = int(input())
ot = 0
ox = 0
oy = 0
fg = True
 
for _ in [0] * n:
    t, x, y = map(int, input().split())
    dt = t - ot
    di = abs(x-ox)+abs(y-oy)
    if di > dt:
        fg = False
    if di % 2 != dt % 2:
        fg = False
    ot = t
    ox = x
    oy = y

if fg:
    print('Yes')
else:
    print('No')
