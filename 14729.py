# https://www.acmicpc.net/problem/14729
a=int(input())
#반복 횟수
l=[]
cnt=0
#7인 선정용
import sys
for i in range(a):

    l.append(float(sys.stdin.readline()))
    #시간 출이기용 소수 리스트에 추가
l.sort()
#오름차순 정렬
for i in l:
    print("{:.3f}".format(i))
    #낮은 수부터 차례대로 소수점3자리까지 출력
    cnt+=1
    if cnt==7:
        break
    #7명이 나왔다면 끝