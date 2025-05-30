import sys
inp = sys.stdin.readline

n = int(inp())
array = [int(inp()) for _ in range(n)]
array.sort()

for i in range(n):
  print(array[i])