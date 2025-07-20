#https://www.acmicpc.net/problem/2851
import sys
A=sys.stdin.readline()
B=set(map(int,sys.stdin.readline().split()))
c=sys.stdin.readline()
d=list(map(int,sys.stdin.readline().split()))
l=[]
for i in d:
    if i in B:
        print(1,end=" ")
    else:
        print(0,end=" ")
#전체적으로 쉽지만 시간줄이기가 어려웠다
#1차 시도 sys 시간초과
#2차 시도 문득 선생님이 데이터 순서를 말한게 떠올라set를 사용 후 성공