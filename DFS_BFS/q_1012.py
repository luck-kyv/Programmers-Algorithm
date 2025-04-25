import sys
sys.setrecursionlimit(10000)

def dfs(x, y, field, n, m):
  if x < 0 or x >= n or y < 0 or y >= m:
    return False
  if field[x][y] == 1:
    field[x][y] = 0
    dfs(x - 1, y, field, n, m)
    dfs(x + 1, y, field, n, m)
    dfs(x, y - 1, field, n, m)
    dfs(x, y + 1, field, n, m)
    return True
  return False

t = int(input())
for _ in range(t):
  m, n, k = map(int, input().split())
  field = [[0] * m for _ in range(n)]
  for _ in range(k):
    x, y = map(int, input().split())
    field[y][x] = 1

  cnt = 0
  for i in range(n):
    for j in range(m):
      if dfs(i, j, field, n, m):
        cnt += 1
  print(cnt)

