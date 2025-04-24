# https://www.acmicpc.net/problem/1065
# 한수(등차수열을 이루는 숫자)를 구하는 프로그램

num = int(input())  # 입력받은 숫자
cnt = 0  # 한수의 개수를 저장할 변수

for i in range(1, num + 1):
    n = list(map(int, str(i)))  # 숫자를 자릿수별로 나눔
    if i < 100:
        # 100 이하의 수는 모두 한수
        cnt += 1
    elif n[0] - n[1] == n[1] - n[2]:
        # 세 자리 수에서 등차수열을 이루는 경우
        cnt += 1

print(cnt)  # 한수의 개수 출력