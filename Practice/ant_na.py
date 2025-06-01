import sys
inp = sys.stdin.readline

n = int(inp())
food = list(map(int, inp().split()))

d = [0] * n
d[0] = food[0]
d[1] = max(food[0], food[1])
# a_i = max(a_{i-1}, a_{i-2}+food[i])
for i in range(2, n):
  d[i] = max(d[i - 1], d[i - 2] + food[i])

print(max(d))