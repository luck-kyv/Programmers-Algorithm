import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 1000001
dp_path = [[] for _ in range(N+1)]
# f(1) 초기화
dp[1] = 0
dp_path[1] = [1]
# 2~N+1 ; 
for i in range(2,N+1):
    # f(x) = f(x-1) + 1
    dp[i] = dp[i-1] + 1
    dp_path[i] = dp_path[i-1] + [i]
    # x%3 ==0 ; f(x) = f(x//3) +1
    if i%3==0 and dp[i//3] +1 < dp[i]:
        dp[i]= dp[i//3] + 1
        dp_path[i] = dp_path[i//3] + [i]
    # x%2==0 ; f(x) = f(x//2) +1
    if i%2==0 and dp[i//2] +1 < dp[i]:
        dp[i]= dp[i//2] + 1
        dp_path[i] = dp_path[i//2] + [i]

dp_path[N].reverse()

print(dp[N])
print(' '.join(map(str, dp_path[N])))