import sys
inp = sys.stdin.readline

n = int(inp())

d = [0] * (n + 1)

# a_i = min(a_{i-1}, a_{i//2}, a_{i//3})
for i in range(2, n + 1):
  d[i] = d[i - 1] + 1
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)
  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1)

print(d[n])