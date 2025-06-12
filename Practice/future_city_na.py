import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
company = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(n+1):
  for b in range(n+1):
    if a == b:
      company[a][b] = 0

for _ in range(m):
  a, b = map(int, input().split())
  company[a][b] = 1
  company[b][a] = 1
x, k = map(int, input().split())

for k in range(1, n + 1): 
  for a in range(1, n + 1): 
    for b in range(1, n + 1): 
      company[a][b] = min(company[a][b], company[a][k] + company[k][b])

distance = company[1][k] + company[k][x]

if distance >= INF:
  print("-1")
else:
  print(distance)
