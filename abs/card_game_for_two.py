n = int(input())
r = [int(x) for x in input().split()]
a = []
b = []
 
while len(r) > 0:
    a.append(max(r))
    r. remove(max(r))
    if len(r) <= 0:
        break
    b.append(max(r))
    r. remove(max(r))
 
print(sum(a)-sum(b))
