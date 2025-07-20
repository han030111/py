# https://www.acmicpc.net/problem/1269
import sys
c=sys.stdin.readline().split()
a=set(map(int,sys.stdin.readline().split()))
b=set(map(int,sys.stdin.readline().split())) 
d=a-b
e=b-a
print(len(d)+len(e))
#단순한 set 빼기 문제였다
