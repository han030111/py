# https://www.acmicpc.net/problem/11723
import sys
from collections import deque

N = int(sys.stdin.readline())
l= deque()
#데큐를
for i in range(N):
    command = list(map(int, sys.stdin.readline().split()))
    #명령문을 받는다
    n = command[0]
    #보기 편하게 분리
    if n == 1:
        l.appendleft(command[1])
    elif n == 2:
        l.append(command[1])
    elif n==3:
        if len(l) == 0:
            print(-1)
        else:
            print(l.popleft())
    elif n ==4:
        if len(l) == 0:
            print(-1)
        else:
            print(l.pop())
    elif n == 5:
        print(len(l))
    elif n ==6:
        if len(l) == 0:
            print(1)
        else:
            print(0)
    elif n == 7:
        if len(l) == 0:
            print(-1)
        else:
            print(l[0])
    elif n == 8:
        if len(l) == 0:
            print(-1)
        else:
            print(l[-1])