import sys
inp = sys.stdin.readline 

n = int(inp())
soldiers = list(map(int, inp().split()))
soldiers.reverse()

d = [1] * n

for i in range(1, n):
  for j in range(i):
    if soldiers[i] > soldiers[j]:
      d[i] = max(d[i], d[j] + 1)

print(n - d[n-1])