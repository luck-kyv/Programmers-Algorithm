from collections import deque
N, K = map(int, input().split())

#bfs 함수
def bfs(N, K):
    #bfs -> 큐 생성
    q = deque()
    q.append(N)
    # 방문 시간 표시
    visited = [0] * 100000

    while q:
        x = q.popleft()

        if x == K:
            print(visited[x])
            break
        
        for move in [x + 1, x - 1, 2 * x]:
            if 0<= move<=100000 and not visited[move]:
                visited[move] = visited[x] + 1
                q.append(move)

bfs(N, K)


