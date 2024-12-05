import sys
l=[]
k=[]
cnt=0
for i in range(8):
    a=int(input())
    l.append(a)

n=l
n.sort(reverse=True)
print(l)
for i in n:
    k.append(l.index(i))
    cnt+=1
    if cnt==5:
        break
print(k)