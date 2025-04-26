#https://www.acmicpc.net/problem/1439
import sys


a=sys.stdin.readline()
b=0
l=[[a[0]]]
for i in a[1:]:
    if i in l[b]:
        l[b].append(i)
    else:
        l.append([i])
        b+=1
if len(l)==1:
    print(0)
else:
    print(b//2)