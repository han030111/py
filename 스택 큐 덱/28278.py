a = []
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    
    b = sys.stdin.readline().split()
    
    if b[0] == '1':
        a.append(b[1])
    elif b[0] == '2':
        if a:
            print(a.pop())
        else:
            print(-1)
    elif b[0] == '3':
        print(len(a))
    elif b[0] == '4':
        if a:
            print(0)
        else:
            print(1)
    elif b[0] == '5':
        if a:
            print(a[-1])
        else:
            print(-1)