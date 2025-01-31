# https://www.acmicpc.net/problem/1934
import sys
import math
d=int(input())



for i in range(d):
    A,B=list(map(int,sys.stdin.readline().split()))

    c=math.lcm(A,B)



        
    print(c)
    #요즘 비슷한 문제만 풀고 실력이 안느는것 같다