import sys
a=sys.stdin.readline()
list_1=list(map(int,sys.stdin.readline().split()))
list_2=list(map(int,sys.stdin.readline().split()))
cnt=0
list_1.sort()
for i in list_1:
    cnt+=i*max(list_2)
    list_2.remove(max(list_2))
print(cnt)