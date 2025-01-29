# https://www.acmicpc.net/problem/9417
import math
import sys
a=int(input())
for i in range(a):
    l=list(map(int,sys.stdin.readline().split()))
    value=[]
    for i in range(len(l)):
        for k in range(i+1,len(l)):
            value.append(math.gcd(l[i],l[k]))
    print(max(value))
#이제는 문제 푼 코드 복붙하고 sum max로 바꾸고 for문 약간 고치니까 풀렸다
