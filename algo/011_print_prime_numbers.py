n=int(input())

def is_prime(a):
  for x in range(2, a):
    if a % x == 0: return False
  return True

print(' '.join([str(x) for x in range(2, n+1) if is_prime(x)]))
