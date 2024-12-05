import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(w, h, area):
    min_time = float('inf')
    fire_q = deque()
    sanggeun_q = deque()
    fire_t = [[-1] * w for _ in range(h)]
    sanggeun_t = [[-1] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if area[i][j] == '*':
                fire_q.append((i, j))
                fire_t[i][j] = 0
            elif area[i][j] == '@':
                sanggeun_q.append((i, j))
                sanggeun_t[i][j] = 0
    
    while fire_q:
        x, y = fire_q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<h and 0<=ny<w and fire_t[nx][ny] == -1 and area[nx][ny] != '#':
                fire_t[nx][ny] = fire_t[x][y] + 1
                fire_q.append((nx, ny))

    while sanggeun_q:
        x, y = sanggeun_q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                return sanggeun_t[x][y] + 1
            if 0<=nx<h and 0<=ny<w and sanggeun_t[nx][ny] == -1 and area[nx][ny] != '#':
                if fire_t[nx][ny] == -1 or fire_t[nx][ny] > sanggeun_t[x][y] + 1:
                    sanggeun_t[nx][ny] = sanggeun_t[x][y] + 1
                    sanggeun_q.append((nx, ny))
    
    for i in range(h):
        for j in range(w):
            if (i == 0 or j == 0 or i == h-1 or j == w-1) and sanggeun_t[i][j] != -1:
                min_time = min(min_time, sanggeun_t[i][j])
    
    if min_time == float('inf'):
        return "IMPOSSIBLE"

for _ in range(N):
    w, h = map(int, input().split())
    area = [list(input().strip()) for _ in range(h)]
    print(bfs(w, h, area))