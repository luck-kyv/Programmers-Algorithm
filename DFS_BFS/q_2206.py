import sys
from collections import deque
inp = sys.stdin.readline

n, m = map(int, inp().split())
field = [list(map(int, inp().strip())) for _ in range(n)]
visited = [[[False]*2 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0, 0, 1, 0)) # x, y, distance, wall_break(지금까지 벽을 부쉈는지 여부)
visited[0][0][0] = True

while queue:
  x, y, distance, wall_break = queue.popleft()

  if x == n - 1 and y == m - 1:
    print(distance)
    break

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < n and 0 <= ny < m:
      if field[nx][ny] == 0 and not visited[nx][ny][wall_break]:
        visited[nx][ny][wall_break] = True
        queue.append((nx, ny, distance + 1, wall_break))
      # 벽이 있고, 아직 벽을 부수지 않았고, 벽부순자리에 방문하지 않았을 때
      elif field[nx][ny] == 1 and wall_break == 0 and not visited[nx][ny][1]:
        visited[nx][ny][1] = True
        queue.append((nx, ny, distance + 1, 1))
  
else:
  print(-1)