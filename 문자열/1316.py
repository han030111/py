#https://www.acmicpc.net/problem/1316
n = int(input())
answer = 0

for _ in range(n):
    word = input()
    l = set()
    b = ''
    value = True

    for char in word:
        if char != b:
            if char in l:
                value = False
                break
            l.add(char)
        b = char

    if value:
        answer += 1

print(answer)
#만약 전의 값과 같다면 무고건 그룹이니 넘기고 아니라면 set에 넣어준다 만약 if문에 걸리면 전의 값과도 다르고 그 안에 있다는 거니 그룹이 아니다다
#그룹이 아니라면 value를 false로 바꿔준다