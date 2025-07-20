# https://www.acmicpc.net/problem/10989
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dict = {}
for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])
#우연히 선택문제가 둘다 dict가 되었다다
#리스트배우면 그거느리다고 set쓰라하고 set쓰면 그거 느리다고 dict쓰라하고