# https://www.acmicpc.net/problem/3711
import sys
a=int(sys.stdin.readline())
#케이스의 수
for _ in range(a):
    li = []
    #원래값을 담은 리스트 만들기
    n = int(sys.stdin.readline())
    for __ in range(n):
        li.append(int(sys.stdin.readline()))
    if n == 1:
        print(1)
        #학생이 한명이면 1프린트
    else:
        cnt = 2
        #나눌값 
        while 1:
            divli = []
            for i in range(len(li)):
                divli.append(li[i] % cnt)
                #리스트의 모든 값을 나눈값의 나머지를 세로운 리스트에 넣기
            dd = set(divli)
            dd = list(dd)
            if len(li) == len(dd):
                print(cnt)
                break
            #중복값이 없으면 출력후 탈출
            else:
                cnt += 1
                #중복되면 값 1 놓이기

