from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(N)]
# [[101111], [101010], [101011], [111011]]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#bfs
def bfs(graph, N, M):
    # 큐 생성
    q = deque()
    q.append((0,0))

    while q:
        x, y = q.popleft()

        for i in range(4):
            ix = x + dx[i]
            iy = y + dy[i]

            if 0 <= ix < N and 0 <= iy < M:
                if graph[ix][iy] == 1:
                    graph[ix][iy] = graph[x][y] + 1
                    q.append((ix, iy))

    return graph[N-1][M-1]

print(bfs(graph, N, M))

