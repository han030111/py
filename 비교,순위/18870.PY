A=int(input())
b=list(map(int,input().split()))
l=[]
d=dict()
c=sorted(list(set(b)))
cnt=0
for i in c :
    d[i]=cnt
    cnt+=1
for i in b:
    print(d[i],end=' ')
