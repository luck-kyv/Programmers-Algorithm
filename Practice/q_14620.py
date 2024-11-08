from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
base = [list(map(int, input().split())) for _ in range(N)]
answer = float("inf")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 주변에 있는지 확인
def can_seed(i, j, visited):
	for idx in range(4):
		nx = i + dx[idx]
		ny = j + dy[idx]
		if (nx, ny) in visited:
			return False
	return True

def dfs(visited, sum):
	global answer # 최소비용
	
	if len(visited) == 15: # 3개의 꽃->15평
		answer = min(answer, sum)
		return
	else:
		for i in range(1, N-1):
			for j in range(1, N-1):
				if can_seed(i, j, visited) and (i, j) not in visited:
					# 현 위치
					visited.append((i, j))
					sum+=base[i][j]
					# 주변 위치
					temp = []
					for idx in range(4):
						nx = i + dx[idx]
						ny = j + dy[idx]
						temp.append((nx, ny))
						visited.append((nx, ny))
						sum+=base[nx][ny]
					dfs(visited, sum)
					visited.pop()
					sum -= base[i][j]
					for nx, ny in temp:
						visited.pop()
						sum -= base[nx][ny]

dfs([], 0)
print(answer)

