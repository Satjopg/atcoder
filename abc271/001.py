from sys import stdin
import io

_INPUT = """\
99
"""

stdin = io.StringIO(_INPUT)

mp = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
n=int(stdin.readline().rstrip())
a = mp[int(n / 16)]
b = mp[int(n % 16)]
print(a+b)
