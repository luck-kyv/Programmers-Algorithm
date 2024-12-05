import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def dfs(x, y, h):
    q = deque()
    q.append((x, y))

    while q:
        ix, iy = q.popleft()

        for i in range(4):
            nx, ny = ix+dx[i], iy+dy[i]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and area[nx][ny] > h:
                    visited[nx][ny] = True
                    q.append((nx, ny))

max_height = max(map(max, area))

max_cnt = 1
#100까지 
for h in range(max_height):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    # 영역별 cnt 세기(bfs)
    for i in range(N):
        for j in range(N):
            if area[i][j] > h and not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                dfs(i, j, h)
    max_cnt = max(max_cnt, cnt)

print(max_cnt)