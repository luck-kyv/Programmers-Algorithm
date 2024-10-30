n = int(input()) #컴퓨터 수
e = int(input()) #간선 수
graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(e):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]

visited = [False] * (n+1)
sum = 0

def dfs(v):
    global sum 
    visited[v] = True
    #미방문 + v번과 연결
    for u in graph[v]:
        if visited[u] == False:
            dfs(u)
            sum += 1

dfs(1)
print(sum)

