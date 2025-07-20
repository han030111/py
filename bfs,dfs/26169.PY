# https://www.acmicpc.net/problem/26169
board = []
for i in range(5):
    board.append(list(map(int, input().split())))

x, y = map(int, input().split())
bool = False

def dfs(x,y,move,cnt):
    global bool

    cnt = cnt
    if x > 4 or y > 4 or x < 0 or y < 0 or move > 3:
        return

    if board[x][y] == -1:
        return

    if board[x][y] == 1:
        cnt += 1

    temp = board[x][y]
    board[x][y] = -1

    if cnt == 2:
        bool = True
        return

    dfs(x+1, y, move+1, cnt)
    dfs(x-1, y, move+1, cnt)
    dfs(x, y+1, move+1, cnt)
    dfs(x, y-1, move+1, cnt)

    board[x][y] = temp

dfs(x,y,0,0)
if bool:
    print(1)
else:
    print(0)
#요즘들어 검색을 많이 하는것 같다 