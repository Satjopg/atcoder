# by https://qiita.com/ajim/items/4d350710ba70056f5f6f

import io
from sys import stdin

_INPUT = """\
2
1 2 3
aaa
"""

stdin = io.StringIO(_INPUT)

import io
from sys import stdin

_INPUT = """\
827847039317
"""

stdin = io.StringIO(_INPUT)

import io
from sys import stdin

_INPUT = """\
2
1 2 3
"""

stdin = io.StringIO(_INPUT)

print(int(input())) # 2
print(list(map(int, input().split())))  # [1, 2, 3]
print(list(input())) # ['a', 'a', 'a']
