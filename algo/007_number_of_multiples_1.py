n,x,y=[int(i) for i in input().split()]
print(sum([i%x==0 or i%y==0 for i in range(1,n+1)]))
