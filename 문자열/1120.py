# https://www.acmicpc.net/problem/1120
#백테스트용 adaabc aababbc
import sys
a,b=sys.stdin.readline().split()
c=len(b)-len(a)
cntlist=[]
ccnt=0
if c!=0:
    for i in range(c+1):
        cnt=0
        bb=b[i:len(a)+i]
        for j in range(len(a)):
            if bb[j]!=a[j]:
                cnt+=1

        cntlist.append(cnt)
    
    print(min(cntlist))
else:
    for j in range(len(a)):
        if b[j]!=a[j]:
            ccnt+=1
    print(ccnt)
#3문제중 가장 낫다
#앞뒤에 붙이는걸 어떻게할지 고민하다 붙일거면 어차피 그 부분은 카운트 안한다 라는 생각이 났다
#앞뒤에 붙이는건 0카운트니 어떤 방향에 붙이는게 카운트에 이득인지 찾는 방향으로 풀었다다