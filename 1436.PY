# https://www.acmicpc.net/problem/1436
import sys
a=int(sys.stdin.readline())
cnt=0  
value=0
#차례대로 먗번째로 작은 값을 세어줄지,카운트,값
while cnt<a:
    #카운트와 목표가 같으면 종료
    value+=1
    #0이 필요할리는 없으니 시작에 값 높여주기
    if "666" in str(value):
        #특정 문자열을 찾지 못해 검색해서IN 을 찾음
            cnt+=1
            #카운트 높이기
    
print(value)