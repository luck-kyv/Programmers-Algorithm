import sys
from collections import deque

inp = sys.stdin.readline

m, n, h = map(int, inp().split())
tomato = [[list(map(int, inp().split())) for _ in range(n)] for _ in range(h)]

queue = deque()

# 익은 토마토 큐에 추가
for k in range(h):
  for j in range(n):
    for i in range(m):
      if tomato[k][j][i] == 1:
        queue.append((k, j, i))

# 익은 토마토 주위 + 1
while queue:
  z, y, x = queue.popleft()
  for dz, dy, dx in [(-1, 0, 0), (1, 0, 0), 
                     (0, -1, 0), (0, 1, 0), 
                     (0, 0, -1), (0, 0, 1)]: 
    nz, ny, nx = z + dz, y + dy, x + dx
    if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
      if tomato[nz][ny][nx] == 0:
        tomato[nz][ny][nx] = tomato[z][y][x] + 1
        queue.append((nz, ny, nx))

max_day = 0
for z in range(h):
  for y in range(n):
    for x in range(m):
      # 안익은 토마토 있으면 -1 출력
      if tomato[z][y][x] == 0:
        print(-1)
        sys.exit()
      # 없으면 max update
      max_day = max(max_day, tomato[z][y][x])

print(max_day - 1)
