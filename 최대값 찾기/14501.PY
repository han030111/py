def max_profit_consulting(tasks, current_day, total_days):
    # 기본 케이스: 마지막 날짜를 넘어섰다면, 더 이상 이익을 추가할 수 없음
    if current_day >= total_days:
        return 0

    # 옵션 1: 현재 작업을 수행하지 않음
    # 다음 날짜로 이동하며 현재 작업을 건너뜀
    profit_not_taking = max_profit_consulting(tasks, current_day + 1, total_days)

    # 옵션 2: 현재 작업을 수행 (가능하다면)
    profit_taking = 0
    task_duration = tasks[current_day][0] # 작업 기간
    task_profit = tasks[current_day][1]   # 작업 이익

    # 현재 작업을 수행해도 총 일수를 초과하지 않는지 확인
    if current_day + task_duration <= total_days:
        # 이 작업을 수행한다면, 작업이 끝난 날짜부터 다시 재귀 호출
        profit_taking = task_profit + max_profit_consulting(tasks, current_day + task_duration, total_days)

    # 두 옵션 중 더 큰 이익 반환
    return max(profit_not_taking, profit_taking)

a = int(input())
l = []
for _ in range(a):
    # map 객체를 list 또는 tuple로 변환해야 합니다.
    l.append(list(map(int, input().split())))

result = max_profit_consulting(l, 0, a) # 0번째 날부터 시작
print(result)