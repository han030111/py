# https://www.acmicpc.net/problem/5347
import sys
import math
d=int(input())
#반복횟수


for i in range(d):
    A,B=list(map(int,sys.stdin.readline().split()))
    #나눠서 빋기
    c=math.lcm(A,B)
    #왠만한 for문으로 하는 공식은 math에 있다


        
    print(c)