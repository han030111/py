# https://www.acmicpc.net/problem/1769
n = input()
#인풋 받고
c=0
#몇번 과정을 반복하는지 확인해줄 카운트
while int(n)>=10:
#한자리수가 될때까지 반복
    t = 0
    #n은 문자열 상태여야 하니 n의 값을 잠시 받아줄 변수 만들기
    for i in n:
        #i 에 문자열을 한글자씩 넣기
        t+=int(i)
        #자리수 값 다 더하기
    n=str(t)
    #다시 문자로 바꾸어 N으로
    c+=1
print(c)
if int(n)%3==0:
    print("YES")
    #배수면
else:   
    print('NO')
    #배수가 아니면