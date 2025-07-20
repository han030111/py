import sys

def solve():
    N = int(sys.stdin.readline())
    pillars = []
    for _ in range(N):
        L, H = map(int, sys.stdin.readline().split())
        pillars.append((L, H))

    # 기둥을 왼쪽 위치(L)를 기준으로 정렬
    pillars.sort()

    # 가장 높은 기둥 찾기
    max_height = 0
    max_height_idx = -1 # 가장 높은 기둥의 인덱스 (정렬된 리스트 기준)
    
    for i in range(N):
        if pillars[i][1] > max_height:
            max_height = pillars[i][1]
            max_height_idx = i

    total_area = 0

    # 1. 왼쪽에서 가장 높은 기둥까지 면적 계산
    # (max_height_idx 포함하지 않고 직전까지 계산)
    current_pillar_idx = 0
    max = pillars[0][1] # 현재까지 지나온 기둥 중 가장 높은 높이
    for i in range(max_height_idx):
        # 다음 기둥의 L 값까지 현재 max 높이로 채움
        total_area += (pillars[i+1][0] - pillars[i][0]) * max
        
        # 현재 기둥의 높이가 max보다 높다면 갱신
        if pillars[i+1][1] > max:
            max = pillars[i+1][1]

    # 2. 오른쪽에서 가장 높은 기둥까지 면적 계산
    # (max_height_idx 포함하지 않고 직전까지 계산)
    current_pillar_idx = N - 1
    max = pillars[N-1][1] # 현재까지 지나온 기둥 중 가장 높은 높이
    for i in range(N - 1, max_height_idx, -1): # max_height_idx의 다음까지만 계산
        # 이전 기둥의 L 값까지 현재 max 높이로 채움
        total_area += (pillars[i][0] - pillars[i-1][0]) * max
        
        # 현재 기둥의 높이가 max보다 높다면 갱신
        if pillars[i-1][1] > max:
            max = pillars[i-1][1]
            
    # 3. 가장 높은 기둥의 면적 추가 (폭 1)
    total_area += max_height

    print(total_area)

solve()