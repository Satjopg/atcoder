n=int(input())
# √nまで調べればよい
# iで割り切れたらn/iでも割り切れる
i=1
while i ** 2 <= n:
  if n % i == 0:
    print(i)
    print(int(n/i))
  i+=1
