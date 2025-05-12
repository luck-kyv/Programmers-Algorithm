import sys
sys.setrecursionlimit(10000)
inp = sys.stdin.readline

n = int(inp())
painting = [list(inp().strip()) for _ in range(n)]
# 적록색약용 그림
converted = [[c if c != 'G' else 'R' for c in row] for row in painting]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문처리
def dfs(x, y, graph, visited, color):
  visited[x][y] = True
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
      # 색이 같으면 
      if not visited[nx][ny] and graph[nx][ny] == color:
        dfs(nx, ny, graph, visited, color)

def cnt_area(graph):
  visited = [[False] * n for _ in range(n)]
  cnt = 0
  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        dfs(i, j, graph, visited, graph[i][j])
        cnt += 1
  return cnt

normal = cnt_area(painting)
abnormal = cnt_area(converted)

print(normal, abnormal)