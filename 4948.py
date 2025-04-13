import sys, math

def is_Prime(num):



    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 0
    return 1
while True:
    cnt=0
    fi = int(sys.stdin.readline())
    if fi==0:
        break 
    for i in range(fi,fi*2):
        cnt+=is_Prime(i)


    print(cnt)
            