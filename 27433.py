# https://www.acmicpc.net/problem/27433
import sys
cnt=1
for i in range(1,int(sys.stdin.readline())+1):
    cnt*=i
print(cnt)