import sys
input = sys.stdin.readline

n = int(input())
h=[]

for _ in range(n):
    h.append(list(map(int, input().split())))
#[[30, 19, 5], [64, 77, 64], [15, 19, 97], [4, 71, 57], [90, 86, 84], [93, 32, 91]]

for i in range(1, n):
    h[i][0] = min(h[i-1][1], h[i-1][2]) + h[i][0]
    h[i][1] = min(h[i-1][0], h[i-1][2]) + h[i][1]
    h[i][2] = min(h[i-1][0], h[i-1][1]) + h[i][2]

print(min(h[n-1][0],h[n-1][1],h[n-1][2]))