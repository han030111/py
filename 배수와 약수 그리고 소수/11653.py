#https://www.acmicpc.net/problem/11653
import sys
n=int(sys.stdin.readline())
m=2
l=[]
while n!=1:
    if n==1 or n==0:
        break
    if n%m==0:
        l.append(m)
        n=n//m
    else:
        m+=1
l.sort()
for i in l:
    print(i)