A,B=map(int,input().split())
c,d=map(int,input().split())
e=A*d+c*B
f=B*d
from fractions import Fraction
 
w=Fraction(e, f) # 결과를 기약분수로 출력

print(w.numerator, w.denominator) # 분자와 분모를 출력