
e,s,m = map(int, input().split())
a,b,c = 1, 1, 1
year = 1
while(1):
    if e == a and s == b and m == c:
        print(year)
        break
    year+=1
    a += 1
    b += 1
    c  += 1
    if a == 16:
        a = 1
    if b == 29:
        b = 1
    if c == 20:
        c = 1
