# https://www.acmicpc.net/problem/2798
a,c=list(map(int,input().split()))
#카드의 수와 목표값 입력
b=list(map(int,input().split())) 
#카드 목록
r=0
#프린트할 목표값의 근접값
for i in range(a):
#첫번째 카드의 값
    n=b[i]
    
    if n>c:
    # 값이 목표값보다 크면 넘기기
        continue
    for j in range(i+1,a):
        if n+b[j]<=c:
            m=n+b[j]
            for k in range(j+1,a):
                if r<=m+b[k]<=c:
                    r=m+b[k]
                #지금까지 나온 값이상이고 목표값 이하인 조합이 나오면 그 값으로 
print(r)
#값이 더해지는 모든 경우의 수를 계산한다
