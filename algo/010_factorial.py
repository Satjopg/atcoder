from functools import reduce
n=int(input())
print(reduce(lambda a,b:a*b, range(1,n+1)))
