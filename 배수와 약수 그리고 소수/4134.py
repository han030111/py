# https://www.acmicpc.net/problem/4134
import sys, math
def is_Prime(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    while True:
        if is_Prime(num) == True:
            print(num)
            break
        else:
            num += 1
#찾아본 답중 제곱근 빼곤 이해할수 없어서 그걸로 풀었다