n,a,b=map(int, input().split(' '))
print(sum([x for x in range(1, n+1) if sum(list(map(int, str(x)))) >= a and sum(list(map(int, str(x)))) <= b]))
