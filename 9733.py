a=list(input().split())
l=[]
Cm=a.count("Cm")
l.append(Cm)
Pt=a.count("Pt")
l.append(Pt)
Re=a.count("Re")
l.append(Re)
Cc=a.count("Cc")
l.append(Cc)
Ea=a.count("Ea")
l.append(Ea)
Tb=a.count("Tb")
l.append(Tb)
Ex=a.count("Ex")
l.append(Ex)
b=len(a)
print("Re",Re,round(1/(b/Re),2))
print("Pt",Pt,round(1/(b/Pt),2))
print("Cc",Cc,round(1/(b/Cc),2))
print("Cm",Cm,round(1/(b/Cm),2))

print("Cc",Cc,1/(b/Cc))
print("Ea",Ea,1/(b/Ea))
print("Tb",Tb,1/(b/Tb))
print("Ex",Ex,1/(b/Ex))
#값을 다 받는다
#그 값하나하나를 리스트에서 센 함수를 만든다
#이름과 개수 전체에서의 백분율을 프린트한다