# https://www.acmicpc.net/problem/2587
l=[]
for i in range(5):
    l.append(int(input()))
print(sum(l)//5)
l.sort()


print(l[2])
