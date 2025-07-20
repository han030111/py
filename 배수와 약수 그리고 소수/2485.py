import sys
from math import gcd

# 이미 심어져 있는 가로수 수 
N = int(sys.stdin.readline())

# 첫 가로수 위치 
a = int(sys.stdin.readline())

# 가로수들 사이의 값을 저장할 배열
l = []

# 가로수들 사이의 간격 저장 
for i in range(N-1):
    num = int(sys.stdin.readline())
    l.append(num - a)
    a = num

# arr에 들어있는 모든 수들의 최대공약수 찾기
g = l[0]
for j in range(1, len(l)):
    g = gcd(g, l[j])

# 둘 사이에 심을 가로수 개수: 간격 // 최대공약수 - 1
value = 0
for each in l:
    value += each // g - 1
print(value)