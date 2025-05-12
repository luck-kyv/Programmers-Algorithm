import sys
inp = sys.stdin.readline

n = int(inp())
t = list(map(int, inp().split()))
t.sort()

result = 0
# 오름차순 정렬 -> (* n ... 1)
for i in range(n):
  result += t[i] * (n - i)

print(result)
