import sys
inp = sys.stdin.readline

n = int(inp())
a = set(map(int, inp().split()))

m = int(inp())
b = list(map(int, inp().split()))

for num in b:
  print(1 if num in a else 0)