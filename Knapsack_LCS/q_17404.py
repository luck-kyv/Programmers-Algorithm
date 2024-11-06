import sys
input = sys.stdin.readline

INF = 1000 * 1000 * 1
n = int(input())
h=[]
cost = INF

for _ in range(n):
    h.append(list(map(int, input().split())))
#[[30, 19, 5], [64, 77, 64], [15, 19, 97], [4, 71, 57], [90, 86, 84], [93, 32, 91]]

for i in range(3):
    # 첫 번째 정해두기
    first_h = [[INF]*3 for _ in range(n)]
    first_h[0][i] = h[0][i] 
    for j in range(1, n):
        first_h[j][0] = min(first_h[j-1][1], first_h[j-1][2]) + h[j][0]
        first_h[j][1] = min(first_h[j-1][0], first_h[j-1][2]) + h[j][1]
        first_h[j][2] = min(first_h[j-1][0], first_h[j-1][1]) + h[j][2]

    for j in range(3):
        if i != j:
            cost = min(cost, first_h[-1][j])

print(cost)