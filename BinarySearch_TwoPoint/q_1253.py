import sys
inp = sys.stdin.readline

n = int(inp())
array = list(map(int, inp().split()))
array.sort()

cnt = 0
for k in range(n):
  target = array[k]
  start, end = 0, n - 1
  while start < end:
    if array[start] + array[end] == target:
      if start == k:
        start += 1
      elif end == k:
        end -= 1
      else:
        cnt += 1
        break
    elif array[start] + array[end] < target:
      start += 1
    else:
      end -= 1
  
print(cnt)