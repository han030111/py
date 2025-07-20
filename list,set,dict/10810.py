# https://www.acmicpc.net/problem/10810
a,b=map(int, input().split())
l=[]
for i in range(a):
    
    l.append(0)
for     i in range(b):
    c,d,e=map(int, input().split())
    for i in range(c-1,d):
        l[i]=e
print(*l)
