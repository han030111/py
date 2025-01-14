# https://www.acmicpc.net/problem/25305
import sys
a,b=list(map(int,sys.stdin.readline().split()))
c=list(map(int,sys.stdin.readline().split()))
c.sort()
for i in range(b-1):
    c.pop()
print(c[-1])