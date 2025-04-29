n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
houses = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
  if x < 0 or x >= n or y < 0 or y >= n:
    return 0

  if graph[x][y] == 0:
    return 0
  
  graph[x][y] = 0
  cnt = 1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    cnt += dfs(nx, ny)

  return cnt 

for i in range(n):
  for j in range(n):
    cnt = dfs(i, j)
    if cnt:
      houses.append(cnt)

houses.sort()
print(len(houses))
for house in houses:
  print(house)