#https://www.acmicpc.net/problem/2753
a=int(input())
if a%400==0 or not a%100==0 and a%4==0:
    print(1)
else:
    print(0)