# https://www.acmicpc.net/problem/2670
import sys
 
N = int(sys.stdin.readline())
 
DP = [float(sys.stdin.readline().strip()) for _ in range(N)]
 
for i in range(1, N):
    DP[i] = max(DP[i], DP[i] * DP[i - 1])
 
print('%0.3f' % max(DP))
