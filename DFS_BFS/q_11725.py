import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
visited = [False] * (n + 1)
parents = [0] * (n + 1)

# dfs 1을 기준으로 타고 내려가기
stack = [1]
while stack:
  v = stack.pop()
  visited[v] = True
  for neighbor in graph[v]:
    if not visited[neighbor]:
      visited[neighbor] = True
      parents[neighbor] = v
      stack.append(neighbor)

for i in range(2, n+1):
  print(parents[i])