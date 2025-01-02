import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().split())
grid = [[0]*N for _ in range(M)]

# 직사각형 영역 표시
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] = 1

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    grid[x][y] = 1
    area_size = 0

    while q:
        ix, iy = q.popleft()
        area_size += 1

        for i in range(4):
            nx, ny = ix + dx[i], iy + dy[i]
            if 0<=nx<M and 0<=ny<N and grid[nx][ny] == 0:
                grid[nx][ny] = 1
                q.append((nx, ny))

    return area_size

areas = []
for i in range(M):
    for j in range(N):
        if grid[i][j] == 0:
            areas.append(bfs(i, j))

print(len(areas))
print(" ".join(map(str, sorted(areas))))
