# https://www.acmicpc.net/problem/1065
import sys
num = int(sys.stdin.readline())

cnt = 0
for i in range(1, num+1):
    n = list(map(int, str(i)))
    if i < 100:
        #100이하의 수는 무조건 등차수열을 이룬다
        cnt += 1 
    elif n[0]-n[1] == n[1]-n[2]:
        cnt += 1  
print(cnt)
#1000은 한수가 아니고1000을넘는 수는 나오지 않으니3자리 수만 판별하면 된다