import sys
a=int(sys.stdin.readline())
cnt=0
b=0
while cnt<a :
    b+=1
    if "666" in str(b):
        cnt+=1
print(b)