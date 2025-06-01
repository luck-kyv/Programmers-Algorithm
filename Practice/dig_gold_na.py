import sys
input = sys.stdin.readline

for tc in range(int(input())):
  n, m = map(int, input().split())
  array = list(map(int, input().split()))
  d = []
  idx = 0
  for i in range(n):
    d.append(array[idx:idx+m])
    idx += m
  
  for j in range(1, m):
    for i in range(n):
      left_up = d[i-1][j-1] if i > 0 else 0
      left = d[i][j-1]
      left_down = d[i+1][j-1] if i < n - 1 else 0

      d[i][j] += max(left_up, left, left_down)

  print(max(d[i][m-1] for i in range(n)))