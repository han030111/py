i=int(input())
l=[]
m=[]
a=input().split()
for _ in range(i):
    a=input().split()
    for i in a:
        l.append(a)
for i in a:
    print(i)
    m.append(i,l.count(a))