a,b,c,n=[int(input()) for _ in range(4)]
print(sum(500*i+100*j+50*k==n for i in range(a+1) for j in range(b+1) for k in range(c+1)))