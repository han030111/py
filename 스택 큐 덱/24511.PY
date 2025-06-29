import sys
from collections import deque

def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    C = list(map(int, sys.stdin.readline().split()))

    listt = deque()
    for i in range(N):
        if A[i] == 0:
            listt.append(B[i])

    results = []
    for val_c in C:
        if listt:
            value = listt.popleft()
            results.append(value)
            listt.append(val_c)
        else:
            results.append(val_c)
         
    print(*results)

main()