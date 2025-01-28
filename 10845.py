from collections import deque
import sys


n = int(sys.stdin.readline())
deq = deque()

for _ in range(n):
    command = list(input().split())
    if command[0] == 'push':
        deq.append(command[1])
    elif command[0] == 'pop':
        if len(deq) > 0 :
            tmp = deq.popleft()
            print(tmp)
        else : print(-1)
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        if len(deq) > 0: print(0)
        else : print(1)
    elif command[0] == 'front':
        if len(deq) > 0: print(deq[0])
        else : print(-1)
    elif command[0] == 'back':
        if len(deq) > 0: print(deq[-1])
        else: print(-1)