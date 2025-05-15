# pypy3으로 제출하니 성공 (python3는 시간초과 뜸)
import sys
sys.setrecursionlimit(10000)
inp = sys.stdin.readline

r, c = map(int, inp().split())
alphabet = [list(inp().strip()) for _ in range(r)]

max_cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, visited, cnt):
  global max_cnt
  max_cnt = max(max_cnt, cnt)

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < c and 0 <= ny < r:
      alpha = ord(alphabet[ny][nx]) - ord('A')
      if not(visited & (1 << alpha)):
        dfs(nx, ny, visited | (1 << alpha), cnt+1)

start = ord(alphabet[0][0]) - ord('A')
dfs(0, 0, 1 << start, 1)
print(max_cnt)    
