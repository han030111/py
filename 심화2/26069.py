# https://www.acmicpc.net/problem/26069
import sys
ramge=int(sys.stdin.readline())
l=set("ChongChong")
for i in range(ramge):
    a,b=sys.stdin.readline().split()
    if a in l or b in l:
        l.add(a)
        l.add(b)

print(len(l))
    
