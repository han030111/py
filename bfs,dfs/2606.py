import sys
from collections import deque


def bfs(graphs,start,visited):
    q=deque([start])
    cnt=0
    visited[start]=True
    while q:

        cur=q.popleft()
        for i in graphs[cur]:
            if not visited[i]:
                visited[i]=True
                cnt+=1
                q.append(i)
    return cnt
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
infected_count = bfs(graph, 1, visited)
print(infected_count)