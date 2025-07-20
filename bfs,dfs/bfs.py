import sys
from collections import deque 
value,line,start=list(map(int,sys.stdin.readline().split()))
linelist=[]
print(value)
for i in range(line):
    linelist.append(list(map(int,sys.stdin.readline().split())))
visited=[False]*(value+1)
connect=[[] for _ in range(value+1)]
for i in linelist:
    connect[i[0]].append(i[1])
    connect[i[1]].append(i[0])
for i in range(len(connect)):
    connect[i].sort()
def dfs(visited,start,connect):
    visited[start]=True
    print(start, end=" ")
    for i in connect[start]:
        if not visited[i]:
            dfs(visited,i,connect)
dfs(visited,start,connect)