import sys
input = sys.stdin.readline

n = int(input())

# f(n) = f(n-1) + f(n-2)
# 첫 항 초기화
def tile(n):
    if n==1:
        return 1
    if n==2:
        return 2

    tile = [0]*(n+1)
    tile[1] = 1
    tile[2] = 2

    for i in range(3, n+1):
        tile[i] = tile[i-1] + tile[i-2]
    
    return tile[n]

print(tile(n) % 10007)