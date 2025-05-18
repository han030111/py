import sys
from collections import deque
value,line,start=list(map(int,sys.stdin.readline().split()))
board = [list(map(int, input().split())) for _ in range(line)]
visited=[False]*(value+1)
graphs = [[] for _ in range(value + 1)]
for i in range(len(graphs)):
    graphs[i].sort()
for connect in board:
    graphs[connect[0]].append(connect[1])
    graphs[connect[1]].append(connect[0])
def dfs(vidsited,graphs,start):
    visited[start]=True
    print(start,end=" ")
    for i in graphs[start]:
        if not visited[i]:
            dfs(vidsited,graphs,i)

def bfs(visited,graphs,start):
    q=deque([start])
    visited[start]=True
    while q:
        cur=q.popleft()
        print(cur,end=" ")
        for i in graphs[cur]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
dfs(visited,graphs,start)
print()
visited=[False]*(value+1)
bfs(visited,graphs,start)

