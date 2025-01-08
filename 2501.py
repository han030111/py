#https://www.acmicpc.net/problem/2501
n, m = map(int, input().split())

result = 0
#기본값을0으로 설정

for i in range(1, n + 1):
    if n % i == 0:
        m -= 1
        #약수가 나올때마다 m을 하나씩 빼줌
        if m == 0:
            #m이 영이 되어야 변수값을 바뀌게 해서 m이 너무 클때의 상황 대비
            result = i
            break

print(result)
#만약 m이 약수의 수보다 크면 0이 되지 않아 대신 기본값인 0이 나오게  