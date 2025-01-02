import sys
from collections import deque
input = sys.stdin.readline

dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(l, start, end):
    if start == end:
        return 0
    
    visited = [[False] * l for _ in range(l)]
    q = deque()
    x = start[0]
    y = start[1]
    q.append((x, y, 0))
    visited[x][y] = True

    while q:
        ix, iy, cnt= q.popleft()

        for i in range(8):
            nx, ny = ix + dx[i], iy + dy[i]
            if 0<=nx<l and 0<=ny<l and not visited[nx][ny]:
                if (nx, ny) == end: # 도착하면
                    return cnt+1    # 이동 횟수 반환 
                visited[nx][ny] = True
                q.append((nx, ny, cnt+1))

    return -1 # 도착 못할 경우 

t = int(input())
results = []

for _ in range(t):
    l = int(input()) # 체스판 한 변의 길이 
    start = tuple(map(int, input().split())) # 현재 칸
    end = tuple(map(int, input().split())) # 목표표

    results.append(bfs(l, start, end))

for result in results:
    print(result)
