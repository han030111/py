# https://www.acmicpc.net/problem/15904
#생각한 순서는 앞 숫자로 표기
s = input()#1우선 인풋을 받는다
ans = 'UCPC'#3순서가 있는비교군을 만든다
idx = 0#4비교할때 전부 비교하면 끝내는 것과 몇번째 문자를 비교할지 고민하다 만듬
for i in s:#2하나하나 나누어서 대조한다
    if i == ans[idx]:#5이제 비교할 대조군을 만들었으니 비교되었을때 같으면 다음 글자로 넘어가게 만듬
        idx+=1
    if idx==4:
        print('I love UCPC')
        break
else:
    print('I hate UCPC')