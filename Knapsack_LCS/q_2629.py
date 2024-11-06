import sys
input = sys.stdin.readline

n, w = int(input()), list(map(int, input().split()))
a, b = int(input()), list(map(int, input().split()))

dp = [[0]*15001 for _ in range(n+1)]
ans = []

def cal(N, weight):
    if N > n:
        return
    
    if dp[N][weight] == True:
        return
    
    dp[N][weight] = True

    cal(N+1, weight + w[N-1]) # 오른쪽
    cal(N+1, abs(weight - w[N-1])) # 왼
    cal(N+1, weight) # 안 넣었을 때

cal(0,0)

for bead in b:
    if bead > 15000:
        print("N", end=" ")
    elif dp[n][bead] == True:
        print("Y", end=" ")
    else:
        print("N", end=" ")