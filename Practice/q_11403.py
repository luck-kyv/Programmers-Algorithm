import sys
input = sys.stdin.readline

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
# [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
visited = [0 for _ in range(N)]

def dfs(k):
    for i in range(N):
        if G[k][i] == 1 and visited[i] == 0:
            visited[i] = True
            dfs(i)

for i in range(N):
    dfs(i)
    for j in range(N):
        if visited[j] == 1:
            print(1, end = ' ')
        else:
            print(0, end = ' ')
    print()
    visited = [0 for _ in range(N)]