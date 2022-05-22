import sys
 
sys.setrecursionlimit(10**6)
arr = ['dream', 'dreamer', 'erase', 'eraser']
s = input()
 
def recursive(n):
    if n == len(s):
        return True
    for x in arr:
        if len(x) + n <= len(s) and s[n:n+len(x)] == x:
            if recursive(len(x) + n):
                return True
    return False
 
def main():
    if recursive(0):
        print('YES')
    else:
        print('NO')
 
main()