# https://www.acmicpc.net/problem/10867
b=int(input())
a=list(set(map(int,input().split())))
#나누고 숫자로 바꾸고 중복을 없에고 리스트로
a.sort()
#오름차순 정렬
print(*a)
#리스트 모양 빼기