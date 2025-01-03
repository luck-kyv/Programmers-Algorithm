import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = 0

arr.sort()
for i in range(n):
    ans += arr[i] * (2 * i - (n - 1))

print(ans*2)