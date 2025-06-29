import sys
a,b,c,d,e,f = map(int, sys.stdin.readline().split())

for x in range(-999,1000):
    for y in range(-999,1000):
        if (a*x)+(b*y) == c and (d*x)+(e*y) == f:
            print(x,y)
            break
#연립방정식이 뭔지 배웠지만 구혀 방법을 찾지 못해 다른 답을 찾아봤는데 이중 FOR문을 보고 할말을 잃었다
#이걸 쓰고 시간남는 데까지 정공법을 해볼 것이다