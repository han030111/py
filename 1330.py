#https://www.acmicpc.net/problem/1330
import sys
s,b=map(int,sys.stdin.readline().split())
if s==b:
    print("==")
elif s>b:
    print(">")
else:
    print("<")
    