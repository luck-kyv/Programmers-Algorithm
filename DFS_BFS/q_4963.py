import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(y, x, graph, w, h):
  if x < 0 or x >= w or y < 0 or y >= h:
    return False
  if graph[y][x] == 1:
    graph[y][x] = 0
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1),
                   (-1, -1), (-1, 1), (1, 1), (1, -1)]:
      dfs(y + dy, x + dx, graph, w, h)
    return True
  return False

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break

  graph = [list(map(int, input().split())) for _ in range(h)]
  
  cnt = 0
  for y in range(h):
    for x in range(w):
      if dfs(y, x, graph, w, h):
        cnt += 1
  print(cnt)
