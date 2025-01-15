# https://www.acmicpc.net/problem/25305
import sys
a,b=list(map(int,sys.stdin.readline().split()))
c=list(map(int,sys.stdin.readline().split()))
c.sort()
for i in range(b-1):
    c.pop()
print(c[-1])
#오름차순으로 하고N번째로 큰 수를 찾으려면 N-1번 POP을 하고 가장 마지막 값을 프린트하면 된다