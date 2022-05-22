import sys
 
n = int(input())
arr = [int(x) for x in input().split()]
if len([x for x in arr if x % 2 == 0]) != n:
    print(0)
    sys.exit()
else:
    print(min([(x ^ (x - 1)).bit_length() - 1 for x in arr]))
