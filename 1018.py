# https://www.acmicpc.net/problem/1018
N, M = map(int, input().split())
board = list()
for i in range(N):
    board.append(input())
list = list()

for i in range(N-7):
    for j in range(M-7):
        w = 0
        b = 0
        for k in range(i,i+8):
            for l in range(j,j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] == 'B':
                        w +=1
                    if board[k][l] == 'W':
                        b+=1
                else:
                    if board[k][l] == 'W':
                        w +=1
                    if board[k][l] == 'B':
                        b+=1
        list.append(w)
        list.append(b)
list.append(w)
list.append(b)
print(min(list))
#오늘의 교훈 브루트 포스 풀거면 그냥 for문 쓰자
