from collections import deque

def solve():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue: 
        r, c = queue.popleft()
        jump = board[r][c]

        # 오른쪽 이동
        nr, nc = r, c + jump
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            if nr == n - 1 and nc == n - 1:
                print("HaruHaru")
                return
            visited[nr][nc] = True
            queue.append((nr, nc))

        # 아래쪽 이동
        nr, nc = r + jump, c
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            if nr == n - 1 and nc == n - 1:
                print("HaruHaru")
                return
            visited[nr][nc] = True
            queue.append((nr, nc))
            

    print("Hing")

solve()