# https://www.acmicpc.net/problem/1920
import sys
b=sys.stdin.readline()
a=set(sys.stdin.readline().split())

c=sys.stdin.readline()
d=sys.stdin.readline().split()
for i in d:
    if i in a:
        print(1)
    else:
        print(0)
#이미 비슷한 문제를 많이 풀어서 꽤나 쉬웠다
#join을 이용한 새로운 시도를 해봤지만 시간초과가 나서 결국set로
# in이 count보다 빠르다는 것과 set가 list나 문자열보다 빠르다는 것만 알고
# 있다면 쉬운 문제인것 같다 