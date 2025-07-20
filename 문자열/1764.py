# https://www.acmicpc.net/problem/1764
import sys
a,b=map(int,sys.stdin.readline().split())
l=[]
m=[]
for i in range(a):
    l.append(sys.stdin.readline().rstrip())
for k in range(b):
    m.append(sys.stdin.readline().rstrip())
an=list(set(l) & set(m))
an.sort()
print(len(an))
for w in an:
    print(w)
#파이썬에는 차집합 말고 교집합연산자도 있단걸 알게 되었다
#이상한 원인불명의 줄바꿈을 없에려면rstrip 함수가 필요하다