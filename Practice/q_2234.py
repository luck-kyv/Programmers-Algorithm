import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def has_wall(wall, direction):
    return wall & direction > 0

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    area = 1

    while q:
        ix, iy = q.popleft()

        for i in range(4):
            nx, ny = ix+dx[i], iy+dy[i]

            if 0<=nx<M and 0<=ny<N and not visited[nx][ny]:
                if not has_wall(arr[ix][iy], 1<<i):
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    area += 1
    
    return area

def max_room_area(arr):
    visited =[[False]*N for _ in range(M)]
    max_area, cnt = 0, 0

    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                temp = bfs(i, j, visited)
                max_area = max(max_area, temp)
                cnt += 1
    return max_area, cnt

def sub_wall(arr):
    add_area = 0

    for i in range(M):
        for j in range(N):
            for d in range(4):
                nx, ny = i+dx[d], j+dy[d]
                if 0<=nx<M and 0<=ny<N and has_wall(arr[i][j], 1<<d): # wall제거
                    arr[i][j] -= (1 << d)
                    visited =[[False]*N for _ in range(M)]
                    add_area = max(add_area, bfs(i, j, visited))
                    arr[i][j] += (1 << d)
    return add_area

max_area, cnt = max_room_area(arr)
add_area = sub_wall(arr)

print(cnt)
print(max_area)
print(add_area)