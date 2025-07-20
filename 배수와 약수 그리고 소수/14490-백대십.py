# https://www.acmicpc.net/problem/14490
import sys
import math
a,b=list(map(int,sys.stdin.readline().split(":")))
c=math.gcd(a,b)
print(f"{a//c}:{b//c}")
#math 모듈로 공약수를 찾아서 나누었다
#split로 :를 기준으로 갈랐다