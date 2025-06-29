# https://www.acmicpc.net/problem/9498
import sys
b=int(sys.stdin.readline())
if b>=90:
    print("A")
elif b>=80:
    print("B")
elif b>=70:
    print("C")
elif b>=60:
    print("D")
elif b>=0:
    print("F")
