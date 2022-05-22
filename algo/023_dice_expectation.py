from functools import reduce
from sys import stdin
import io

_INPUT = """\
3
1 2 3
10 20 30
"""

stdin = io.StringIO(_INPUT)

n=int(stdin.readline())
bs=reduce(lambda a,b:int(a)+int(b), stdin.readline().split())/n
rs=reduce(lambda a,b:int(a)+int(b), stdin.readline().split())/n
print(bs+rs)