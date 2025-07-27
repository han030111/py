A, B = map(int, input().split())
lis = list(map(int, input().split()))

cnt = 0
start = 0
end = 0
current_sum = 0

while end < A:
    # end 포인터를 이동시키며 current_sum에 값을 더함
    current_sum += lis[end]
    end += 1

    # current_sum이 B보다 크거나 같으면 start 포인터를 이동시켜 current_sum을 줄임
    while current_sum >= B:
        if current_sum == B:
            cnt += 1
        
        # start 포인터를 이동시키며 current_sum에서 값을 뺌
        current_sum -= lis[start]
        start += 1
        
print(cnt)