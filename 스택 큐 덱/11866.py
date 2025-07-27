import sys
from collections import deque
a,b=map(int,sys.stdin.readline().split())
l=[]
for i in range(a):
    l.append(i+1)
l=deque(l)

if len(l)==1:
      print(f"<{l.pop()}>")
else:
    l.rotate(-b)
    print(f"<{l.pop()}",end=", ")
    while len(l)>1:
        l.rotate(-b)
        print(f"{l.pop()}",end=", ")
    print(f"{l.pop()}>")  