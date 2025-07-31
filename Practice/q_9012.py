import sys
inp = sys.stdin.readline

n = int(inp())
for _ in range(n):
  arr = inp().strip()
  stack = []
  is_vps = True

  for c in arr:
    if c == '(':
      stack.append(c)
    elif c == ')':
      if not stack:
        is_vps = False
      else:
        stack.pop()
  print(stack)
  if stack:
    is_vps = False
  print("YES" if is_vps else "NO")
