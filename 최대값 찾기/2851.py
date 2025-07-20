#https://www.acmicpc.net/problem/2851

score = 0
#점수를 저장해줄 변수 만들기
mushroom = []
#버섯의 값을 저장할 리스트

for _ in range(10):
    mushroom.append(int(input()))
    #10개의 값을 버섯 리스트로

for i in mushroom:
    #하나씩 리스트에서 꺼내기
    score += i
    #일단 스코어에 더한다
    if score >= 100:
        if score - 100 > 100 - (score - i):
            #만약 값이 100을 초과하면 초과된 값과 원래값의 차가 같은지 테스트
            score -= i
            #차가 큰쪽이 크다면 빼고
            break
    #큰쪽과 작은쪽의 차가 같으면 그대로
print(score)





