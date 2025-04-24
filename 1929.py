# https://www.acmicpc.net/problem/1929
import sys, math
def is_Prime(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

while True:
    fi = int(sys.stdin.readline())
    cnt=0
    for i in range(1,fi):
        if is_Prime(i) == True:
            print(i)
            