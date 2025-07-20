# https://www.acmicpc.net/problem/7568
import sys

n = int(sys.stdin.readline())
people = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    people.append([x, y])  # 리스트 저장

ranks = []
for i in range(n):
    rank = 1
    for j in range(n):
        if  people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    ranks.append(rank)

print(*ranks)  # 공백으로 구분하여 출력