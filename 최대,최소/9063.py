a=int(input())
x=[]
y=[]
for i in range(a):
    if a == 1:
        break
    b,c=map(int, input().split())

    x.append(b)
    y.append(c)
if x:
    print((max(x)-min(x))*(max(y)- min(y)))
else:
    print(0)