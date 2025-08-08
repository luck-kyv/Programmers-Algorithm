import sys

inp = sys.stdin.readline

k = int(inp())

arr = [int(inp()) for _ in range(k)]

result = []
for i in arr:
  if i == 0 and result:
    result.pop()
  else:
    result.append(i)
  
print(sum(result))