# https://www.acmicpc.net/problem/7785
import sys
ramge=int(sys.stdin.readline())
l=set()
for i in range(ramge):
    a,b=sys.stdin.readline().split()
    if b=="enter":
        l.add(a)
    else:
        l.remove(a)
l=sorted(list(l),reverse=True)
for i in l:
    print(i)
    
