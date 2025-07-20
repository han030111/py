# https://www.acmicpc.net/problem/26169
import sys

def solve():
    N, B = map(int, sys.stdin.readline().split())
    H = []
    for _ in range(N):
        H.append(int(sys.stdin.readline()))


    min_excess =1000001

    def find_min_height(index, current_sum):
        nonlocal min_excess # 바깥 스코프의 min_excess 변수를 수정하기 위함

        # 모든 소를 고려했으면 재귀 종료
        if index == N:
            # 현재 합계가 책장 높이 B 이상인지 확인
            if current_sum >= B:
                # 최소 초과 높이 업데이트
                min_excess = min(min_excess, current_sum - B)
            return

        find_min_height(index + 1, current_sum + H[index])

        # 2. 현재 소 (H[index])를 스택에 포함시키지 않는 경우
        find_min_height(index + 1, current_sum)

    # 재귀 함수 초기 호출: 0번째 소부터 시작, 현재 합계는 0
    find_min_height(0, 0)

    print(min_excess)

solve()