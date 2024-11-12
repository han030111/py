a,b,c=list(map(int,input().split()))
h=list(map(int,input().split()))
s=list(map(int,input().split()))
d=list(map(int,input().split()))
h=sorted(h,reverse=True)
s=sorted(s,reverse=True)
d=sorted(d,reverse=True)
l=0
o=sum(h)+sum(s)+sum(d)
for i in range(min(len(h),len(s),len(d))):
    hh=h[0]
    ss=s[0]
    dd=d[0]

    l+=int((ss+hh+dd)*0.9)
    h.pop(0)
    s.pop(0)
    d.pop(0)
for i in h:
    l+=i
for i in s:
    l+=i
for i in d:
    l+=i
print(o)
print(l)

