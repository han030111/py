a=int(input())
l=[]
cnt=0
import sys
for i in range(a):
    l.append(float(sys.stdin.readline()))
l.sort()
for i in l:
    print("{:.3f}".format(i))
    cnt+=1
    if cnt==7:
        break