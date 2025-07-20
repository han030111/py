# https://www.acmicpc.net/problem/3036
import sys
import math
from collections import deque
a=sys.stdin.readline()
b=deque(map(int,sys.stdin.readline().split()))
c=b.popleft()
for i in b:
    gcd=math.gcd(c,i)
    print(f"{c//gcd}/{i//gcd}")
#인덱스 넣기보다 그냥 가장 앞의 값을 다른 변수에 넣는게 빨라보여 데큐와 popleft를 사용
#최대공약수를 이용한 통분을 한뒤 포맷으로 띄어쓰기 없이 출력
#점점 수학문제가 많아지는 느낌이다