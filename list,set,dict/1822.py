# https://www.acmicpc.net/problem/1822
import sys
c=sys.stdin.readline().split()
a=list(map(int,sys.stdin.readline().split()))
b=set(map(int,sys.stdin.readline().split()))
l=[]
for i in a:
    if not i in b:
        l.append(i)
if len(l)==0:
    print(0)
else:
    print(len(l))
    l.sort()
    print(*l)
#오름차순 정렬을 하란 말을 못보고 2번 틀렸다
#not을 이용해 set인 b에a에 있는 값이 없는것을 true로 하는 in문을 만들어서 리스트 만듬
#아무것도 업을때의 처리는 len을 이용한 기본적인if,else로