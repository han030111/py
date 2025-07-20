import sys

a = sys.stdin.readline().strip()
l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
i = 0

while i < len(a):
    t = False

    if i + 2 < len(a) and a[i:i+3] == 'dz=':
        cnt += 1
        i += 3
        t = True
 
    elif i + 1 < len(a):
        two = a[i:i+2]
        if two in l:
            cnt += 1
            i += 2
            t = True


    if not t:
        cnt += 1
        i += 1

print(cnt)

