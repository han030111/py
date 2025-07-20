a=[]
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i!=j and j!=k and k!=i:
                a.append([i, j, k])# 각 자리의 값이 전부 다른 3자리 수를 리스트에 넣는다
# 1,2,3,4,5,6,7,8,9를 각각 i,j,k에 넣고 중복을 피하기 위해 if문을 사용했다
for _ in range(int(input())): # 문제의 수인데 이걸 보니 지금까지 변수선언 한게 필요 없어 보인다다
    b, c, d=map(int, input().split()) # b는 정답, c는 숫자와 위치가 맞는 개수, d는 숫자는 맞지만 위치가 틀린 개수
    b=[b//100, (b//10)%10, b%10] # b는 정답을 3자리로 나누어 리스트에 넣는다
    e=[] 
    for i in a:
        if int(b[0]==i[0])+int(b[1]==i[1])+int(b[2]==i[2])==c and int(b[0] in i[1:])+int(b[1] in [i[0], i[2]])+int(b[2] in i[:2])==d:
        # 정답의 각 자리와 i의 각 자리를 비교하여 c와 d를 만족하는 i를 e에 넣는다 int는 값이 true면 1, false면 0을 반환한다 
            e.append(i)
    a=e[:]
print(len(a))
# 제미나이의 해설을 받으니 이해되었다