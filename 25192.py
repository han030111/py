import sys



n = int(sys.stdin.readline())
l = set()
cnt = 0

for _ in range(n):
    i = sys.stdin.readline().strip()
    if i == 'ENTER':
        cnt += len(l)
        l = set()
    else:
        l.add(i)

cnt += len(l)
print(cnt)