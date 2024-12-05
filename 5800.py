import sys

a=int(sys.stdin.readline())
for i in range(a):
    b=list(map(int,sys.stdin.readline().split()))
    b=b[1:]
    b.sort(reverse=True)
    c=b[0]-b[1]
    
    for j in range(2, len(b)):
        c= max(c, b[j - 1] - b[j])
    print("Class",i+1)
    print(f"Max {max(b)}, Min {min(b)}, Largest gap {c}")