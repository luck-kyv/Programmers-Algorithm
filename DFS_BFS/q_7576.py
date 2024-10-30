from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
cnt = 0

#1인 위치
for x in range(N):
        for y in range(M):
            if graph[x][y] == 1:
                q.append([x,y])

#bfs
def bfs():    
    while q:
        x, y = q.popleft()
        for i in range(4):
            ix = x + dx[i]
            iy = y + dy[i]
            #0이라면 이동 후 +1
            if 0 <= ix < N and 0 <= iy < M:
                if graph[ix][iy] == 0:
                    graph[ix][iy] = graph[x][y] + 1
                    q.append([ix, iy])
bfs()
for i in graph:
    if 0 in i:
        #안 익은게 있으면 -1
        print(-1)
        exit(0)
    cnt = max(cnt, max(i))
print(cnt-1)