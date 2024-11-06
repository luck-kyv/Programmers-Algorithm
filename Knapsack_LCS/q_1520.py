import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
#[[50, 45, 37, 32, 30], [35, 50, 40, 20, 25], [30, 30, 25, 17, 28], [27, 24, 22, 15, 10]]

dp = [[-1]*N for _ in range(M)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 현pos > ix : 이동
# graph[M-1][N-1]에 도달하면 cnt += 1

def cnt(x, y):
    if x == M-1 and y == N-1:
        return 1
    if dp[x][y] == -1:
        dp[x][y]=0

        for i in range(4):
            ix = x + dx[i]
            iy = y + dy[i]

            if 0 <= ix < M and 0 <= iy < N:
                if graph[ix][iy] < graph[x][y]:
                    dp[x][y] += df(ix, iy)
    return dp[x][y]

print(cnt(0,0))
