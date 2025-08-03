# https://www.acmicpc.net/problem/9506
import sys

def solve_problem_9506():
    while True:
        n = int(sys.stdin.readline())

        if n == -1: 
            break

        divisors = []
        sum_of_divisors = 0 

       
        for i in range(1, n):
            if n % i == 0: 
                divisors.append(i) 
                sum_of_divisors += i 

        
        if sum_of_divisors == n:
            
            print(f"{n} = {' + '.join(map(str, divisors))}")
        else:
            
            print(f"{n} is NOT perfect.")


solve_problem_9506()