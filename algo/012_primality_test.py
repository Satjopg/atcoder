import sys

n=int(input())
if n < 2:
  print('No')
elif n == 2:
  print('Yes')
elif n % 2 == 0:
  print('No')
else:
  i=3
  # √nで割れなければnでも割れないため√nまでの数字で割り切れないかをチェックする
  while i * i <= n:
    if n % i == 0:
      print('No')
      sys.exit()
    i+=1
  print('Yes')
