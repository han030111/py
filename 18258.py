# https://www.acmicpc.net/problem/18258
import sys
from collections import deque

l = deque()
#큐는 없으니 데큐로2
N = int(sys.stdin.readline())

for _ in range(N) :
    i = sys.stdin.readline().split()

    if i[0] == 'push' :
        l.append(int(i[1]))
    
    elif i[0] == 'pop' :
        if not l :
            print (-1)
        else :
            print(l[0])
            l.popleft()
    
    elif i[0] == 'size' :
        print(len(l))
    
    elif i[0] == 'empty' :
        if len(l) == 0 :
            print(1)
        else :
            print(0)
    
    elif i[0] == 'front' :
        if not l:
            print(-1)
        else :
            print(l[0])
    
    elif i[0] == 'back' :
        if not l :
            print(-1)
        else :
            print(l[-1])