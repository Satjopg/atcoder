from functools import reduce
print(reduce(lambda a,b: a*b, [int(x) for x in input().split()]))
