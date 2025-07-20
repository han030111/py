#https://www.acmicpc.net/problem/11098
import sys
n=int(sys.stdin.readline())
for i in range(n):
    b=int(sys.stdin.readline())
    l=[]
    for j in range(b):
        l.append(sys.stdin.readline().split())
    l.sort(key=lambda x: (int(x[0])))
    print(l[-1][1])