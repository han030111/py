a,c=list(map(int,input().split()))
b=list(map(int,input().split()))
r=0
for i in range(a):

    n=b[i]
    
    if n>c:
        continue
    for j in range(i+1,a):
        if n+b[j]<=c:
            m=n+b[j]
            for k in range(j+1,a):
                if r<=m+b[k]<=c:
                    r=m+b[k]
print(r)
#값이 더해지는 모든 경우의 수를 계산한다
