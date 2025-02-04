import sys
n = int(sys.stdin.readline())
value = 0
for i in range(1, n+1):
    nums = list(map(int, str(i)))
    value = sum(nums) + i
    if value == n:
        print(i)
        break
    if i == n:
        print(0)
#답이 나오지 않아 다른 게시물을 참고했다
#map를 통해 문자열도 분해가 가능하단걸 알게 되었다