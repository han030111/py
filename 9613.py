# https://www.acmicpc.net/problem/9613
import sys
import math
a=int(input())

for i in range(a):
    l=list(map(int, sys.stdin.readline().split()))
    value=[]
    for i in range(1,len(l)):
        for k in range(i+1,len(l)):
            value.append(math.gcd(l[i],l[k]))
            print(sum(value))
   
#블랙잭의 겹치지 않게 모든 경우의 수를 찾는 경험이 도움된것 같다
#이중 for문이라 시간이 불안했지만 다행히 시간 문제는 없었다