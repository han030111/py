#https://www.acmicpc.net/problem/1543
import sys
box = sys.stdin.readline()
value = sys.stdin.readline()
i = 0
cnt = 0
while i < len(box):
    if box[i:i+len(value)] == value:
        i += len(value)
        cnt += 1
    else :
        i += 1
print(cnt)
#슬라이스를 이용해서 만약 i에서 찾는값의 길이까지 탐색했을때 갔다면 그 구간을 넘기고 카운트를 올린다

