#https://www.acmicpc.net/problem/14681
import sys
a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
if a>0 and b>0:
    print(1)
elif a<0 and b>0:
    print(2)
elif a<0 and b<0:   
    print(3)
elif a>0 and b<0:  
    print(4)