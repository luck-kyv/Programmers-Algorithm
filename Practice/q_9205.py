import sys
from collections import deque
inp = sys.stdin.readline

def cal_distance(a, b):
  return abs(distance[a][0] - distance[b][0]) + abs(distance[a][1] - distance[b][1])

for tc in range(int(inp())):
  n = int(inp()) # 편의점 개수
  distance = [list(map(int, inp().split())) for _ in range(n+2)] # 집, 편의점, 락 페스티벌 
  # [[0,0], [1000, 0],[1000, 1000],[2000, 1000]]
  visited = [False] * (n + 2)

  q = deque()
  q.append(0)
  visited[0] = True

  while q:
    now = q.popleft()

    for i in range(n + 2):
      if not visited[i]:
        if cal_distance(now, i) <= 1000:
          visited[i] = True
          q.append(i)

  if visited[-1]:
    print("happy")
  else:
    print("sad")