# https://www.acmicpc.net/problem/1057
n,b,c=map(int, input().split())

cnt=0
while b!=c:
  b -= b//2
  c -= c//2
  cnt+=1
print(cnt)
#첫번째 코드
# import sys
# import math
# a,b,c=map(int,sys.stdin.readline().split())
# cnt=1
# while   min([b,c])%2!=1 or b-c!=-1:
#     b=math.ceil(b/2)
#     c=math.ceil(c/2)
#     cnt+=1
# print(cnt)
#시간 초과로 한두번 바꾸었지만 여전히 시관 초과 
#다른 코드를 보니 시작 카운트를 줄이고 한번더 나누는 코드가 더 간편함
#그 코드를 참고
