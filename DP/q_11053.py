import sys
inp = sys.stdin.readline

n = int(inp())
array = list(map(int, inp().split()))

d = [1] * n

for i in range(1, n):
  for j in range(i):
    if array[i] > array[j]:
      d[i] = max(d[i], d[j] + 1)

print(max(d))