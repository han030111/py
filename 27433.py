# https://www.acmicpc.net/problem/27433
a,b=0,1
c=int(input())
if c==0:
    print(0)
elif c==1:
    print(1)
else:

    for i in range(c-1):
        a,b=b,a+b
    print(b)