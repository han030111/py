n = int(input())
l=[]
for i in range(n):
    k=int(input())
    if k==0 :
        del l[-1]
    else:
        l.append(k)
print(sum(l))