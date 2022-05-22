import sys
n,y=[int(x) for x in input().split(' ')]
for a in range(n+1):
    for b in range(0, (n-a)+1):
        if a * 10000 + b * 5000 + (n-(a+b)) * 1000 == y:
            print(a, b, (n-(a+b)))
            sys.exit()
print('-1 -1 -1')