# https://www.acmicpc.net/problem/1181
n = int(input())
l = []

for i in range(n):
    l.append(input())
    #단어 넣기
l=list(set(l))
l.sort()	
#옛날에 정렬 검색을 많이 해서 abc순 정렬을 알고 있었다
l.sort(key = len)	
#길이순 정렬을 알아보다 찾아냈다


for i in l:
    print(i)
    #하나씩 출력
