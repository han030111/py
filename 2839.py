#https://www.acmicpc.net/problem/2839
n = int(input())

if n % 5 == 0:  
    #5로 나누어떨어지는 수면 그냥 나누기5로 값 출력
    print(n // 5)
else:
    p = 0
    while n > 0:
        n -= 3
        #일단 5로 안나눠지면 그 수가 3보다는 클테니 3을 빼고 계산
        p += 1
        if n % 5 == 0:  
            p += n // 5
            #이렇게 뺀값이 5로 나누어 떨어지면 그값을 더하여 출력 예:18
            print(p)
            break
        elif n == 1 or n == 2: 
            #1이나 2가 나온다는건 조합이 불가능한 거니 -1출력
            print(-1)
            break
        elif n == 0:
            print(p)
            break
#while은 오랜만이었다 