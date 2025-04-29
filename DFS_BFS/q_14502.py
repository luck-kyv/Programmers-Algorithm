import sys
from itertools import combinations
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
max_area = 0
empty_space = []
virus_space = []

for i in range(n):
  for j in range(m):
    if lab[i][j] == 0:
      empty_space.append([i, j])
    if lab[i][j] == 2:
      virus_space.append([i, j])

# 바이러스 퍼뜨리기기
def virus(graph):
  queue = deque(virus_space)
  while queue:
    x, y = queue.popleft()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nx, ny = x + dx, y + dy
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
        graph[nx][ny] = 2
        queue.append((nx, ny))

# 벽 3개 세우는 모든 경우의 수
for wall in combinations(empty_space, 3):
  temp = deepcopy(lab)
  for x, y in wall:
    temp[x][y] = 1

  virus(temp)
  max_area = max(max_area, sum(row.count(0) for row in temp))

print(max_area)