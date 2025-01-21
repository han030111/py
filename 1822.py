# https://www.acmicpc.net/problem/1822
import sys
c=sys.stdin.readline().split()
a=list(map(int,sys.stdin.readline().split()))
b=set(map(int,sys.stdin.readline().split()))
l=[]
for i in a:
    if not i in b:
        l.append(i)
if len(l)==0:
    print(0)
else:
    print(len(l))
    l.sort()
    print(*l)