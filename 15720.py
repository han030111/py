a,b,c=list(map(int,input().split()))
h=list(map(int,input().split()))
s=list(map(int,input().split()))
d=list(map(int,input().split()))
#음료,버거,사이드의 값 각각 받기
h=sorted(h,reverse=True)
s=sorted(s,reverse=True)
d=sorted(d,reverse=True)
#전부 내림차순 정렬하기
l=0
#할인가 넣을 변수
o=sum(h)+sum(s)+sum(d)
#비할인가 넣어줄 변수
for i in range(min(len(h),len(s),len(d))):
    #셋중 가장 적은걸 기준으로 세트 만들기
    hh=h[0]
    ss=s[0]
    dd=d[0]
    #각각 첫값을 복사하는 변수 만들기
    l+=int((ss+hh+dd)*0.9)
    #세트로 해서 더해주기
    h.pop(0)
    s.pop(0)
    d.pop(0)
    #이미 더한값 빼기
for i in h:
    l+=i
for i in s:
    l+=i
for i in d:
    l+=i
#남은 값들 더해주기
print(o)
print(l)

