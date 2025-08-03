# https://www.acmicpc.net/problem/5568
import sys
import itertools

a = int(sys.stdin.readline())
k = int(sys.stdin.readline())
l = [sys.stdin.readline().rstrip() for _ in range(a)]

allcase = itertools.combinations(l, k)

mainset = set()

for combo_tuple in allcase:
    case = "".join(combo_tuple)
    mainset.add(case)

print(len(mainset))
