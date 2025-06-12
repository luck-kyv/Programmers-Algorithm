import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
  q = heapq()
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop()
    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

n, m, start= map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))
  
dijkstra(start)
cnt = 0
max_distance = 0
for d in distance:
	if d != 1e9:
		cnt += 1
		max_distance = max(max_distance, d)
		
print(cnt - 1, max_distance)