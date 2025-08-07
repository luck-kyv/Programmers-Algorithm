import sys
from collections import deque

inp = sys.stdin.readline

n = int(inp())
k = int(inp())

board = [[0] * n for _ in range(n)]
apple_pos = [tuple(map(int, inp().split()) for _ in range(k))]

for r, c in apple_pos:
  board[r-1][c-1] = 1

l = int(inp())

turns = {}
for _ in range(l):
  a, b = inp().split()
  turns[int(a)] = b

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 동 남 서 북
p_dir = 0

snake = deque([(0, 0)])
snake_set = set(snake)
time = 0

while True:
  time += 1
  # 머리 이동
  py, px = snake[-1]
  dy, dx = directions[p_dir]
  next_head = (py+dy, px+dx)

  # 충돌 확인
  if not (0 <= next_head[0] < n and 0 <= next_head[1] < n):
    break
  if next_head in snake_set:
    break

  snake.append(next_head)
  snake_set.add(next_head)

  # 사과 
  if board[next_head[0]][next_head[1]] == 1:
    board[next_head[0]][next_head[1]] = 0
  else:
    tail = snake.popleft()
    snake_set.remove(tail)

  # 방향 전환
  if time in turns:
    if turns[time] == 'L':
      p_dir = (p_dir - 1) % 4
    else:      
      p_dir = (p_dir + 1) % 4

print(time)
