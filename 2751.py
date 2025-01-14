# https://www.acmicpc.net/problem/2751
import sys
a=int(sys.stdin.readline())
l=[]
for i in range(a):
    l.append(int(sys.stdin.readline()))
l.sort()
for i in l:
    print(i)