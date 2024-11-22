import sys
input = sys.stdin.readline

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]
# [[0, 0, 1, 0, 0], [0, 0, 2, 0, 1], [0, 1, 2, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 2]] 
ans = float("inf")
home = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])


def cal_dis(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

arr = []

def dfs(n, cnt):
    global ans
    if n > len(chicken): # n = 치킨집 index
        return
    if cnt == M:
        dis_total = 0
        for h in home:
            dis = float("inf")
            for i in arr:
                c = chicken[i]
                dis = min(dis, cal_dis(h, c))
            dis_total += dis
        ans = min(ans, dis_total)

    arr.append(n)
    dfs(n+1, cnt+1) # 현재 n 선택
    arr.pop()
    dfs(n+1, cnt) # 현재 n 선택 X
    return ans

print(dfs(0,0))