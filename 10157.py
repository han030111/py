# https://www.acmicpc.net/problem/10157
import sys
C, R = map(int, sys.stdin.readline().split())
a = [[0 for i in range(C+1)] for j in range(R+1)]
K = int(sys.stdin.readline())
if K > C*R:
    print(0)
else:
    for i in range(R+1):
        a[i][C] = -1
    for j in range(C+1):
        a[R][j] = -1
    cnt = 0
    n = 1
    i, j = 0, 0
    a[0][0] = 1
    while True:
        if n == K:
            break
        else:
            if cnt == 0:
                if a[i+1][j] == 0:
                    i += 1
                    n += 1
                    a[i][j] = n
                else:
                    cnt = 1
            elif cnt == 1:
                if a[i][j+1] == 0:
                    j += 1
                    n += 1
                    a[i][j] = n
                else:
                    cnt = 2
            elif cnt == 2:
                if a[i-1][j] == 0:
                    i -= 1
                    n += 1
                    a[i][j] = n
                else:
                    cnt = 3
            elif cnt == 3:
                if a[i][j-1] == 0:
                    j -= 1
                    n += 1
                    a[i][j] = n
                else:
                    cnt = 0
    print(j+1, i+1)

#리스트로 x,y를 어떻게 할지만 고민했는데 다른 사람의 답을 보니 아예 2차원을 구현해서 놀랐다다