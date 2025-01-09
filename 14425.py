# https://www.acmicpc.net/problem/14425
import sys
a,b=list(map(int,sys.stdin.readline().split()))
cnt=0
l=[]

for i in range(a):
    l.append(sys.stdin.readline())
l=set(l)
for i in range(b):
    if sys.stdin.readline() in l:
        cnt+=1
print(cnt)
