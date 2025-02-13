
value = 0
l=[]
m=[]
for i in range(1,10001):
    nums = list(map(int, str(i)))
    value = sum(nums) + i
    l.append(value)
for i in range(1,10001):
    m.append(i)
n=list(set(m)-set(l))
n=sorted(n)
for i in n:
    print(i)