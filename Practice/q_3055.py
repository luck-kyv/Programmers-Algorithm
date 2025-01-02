import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split())
area = [list(input().strip()) for _ in range(R)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(R, C, area):
    water_q = deque()
    s_q = deque()
    water_t = [[-1] * C for _ in range(R)]
    s_t = [[-1] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if area[i][j] == '*': # 물 위치
                water_q.append((i, j))
                water_t[i][j] = 0
            elif area[i][j] == 'S': # 고슴도치 위치
                s_q.append((i, j))
                s_t[i][j] = 0
    
    while water_q:
        x, y = water_q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<R and 0<=ny<C and water_t[nx][ny] == -1 and area[nx][ny] not in ('X', 'D'):
                water_t[nx][ny] = water_t[x][y] + 1
                water_q.append((nx, ny))

    while s_q:
        x, y = s_q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<R and 0<=ny<C and s_t[nx][ny] == -1:
                if area[nx][ny] == 'D': # 굴 도착 
                    return s_t[x][y] + 1
                if area[nx][ny] == '.' and (water_t[nx][ny] == -1 or water_t[nx][ny] > s_t[x][y] + 1):
                        s_t[nx][ny] = s_t[x][y] + 1
                        s_q.append((nx, ny))
    
    return "KAKTUS"

print(bfs(R, C, area))
