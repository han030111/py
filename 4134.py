import sys
cnt=int(sys.stdin.readline())
for i in range(cnt):
    case=int(sys.stdin.readline())
    a=2
    while True:
        for j in range(2,case+1):
            if case%j==0:
                break
        if case==j:
            print(case)
            break
        else:
            case+=1