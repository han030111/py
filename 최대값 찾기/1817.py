# https://www.acmicpc.net/problem/1817

n,m=map(int,input().split())#1우선인풋을 받고
count = 0#2수 설정 하고
if n == 0 : #30이면 어차피 값0이니 예외처리
    print(0)
else : 
    b = list(map(int,input().split()))#책 무게를 받는다
    a = 0
    count = 1
    for box in b:#책을 차례차례 넣는다
        if box+a <= m : #6책 무게가 전에 넣은거와 핮쳐 한계를 안넘으면 추가
            a += box
        else : #7넘는다면 새로운 박스 안 무게로 설정
            a = box 
            count +=1
    print(count)
