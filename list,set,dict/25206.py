# https://www.acmicpc.net/problem/25206
dic={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0,
}
l=[]
n=[]
for i in range(20):
    a,b,c=input().split()
    if c=='P':
        continue
    else:
        l.append(dic[c]*float(b))
        n.append(float(b))
print(f"{sum(l)/sum(n):.6f}")
#딕셔너리를 처음으로 사용했다 딕셔너리의 기초같은 문제
# 20과목을 입력받고 P가 아닌 과목의 학점을 딕셔너리에서 찾아서 리스트에 넣고
# 학점과 과목수를 리스트에 넣고 평균을 구하는 문제
# ai가 공식을 다 짜서 놀랐다 심지어 주석도 써줬다
