import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

x = list(input().rstrip())
y = list(input().rstrip())

def lcs(x,y):
	x, y = [' '] + x, [' '] + y
	m, n = len(x), len(y)
	c = [[0 for _ in range(n+1)] for _ in range(m+1)]
	b = [[0 for _ in range(n+1)] for _ in range(m+1)]
	
	for i in range(1, m):
		for j in range(1, n):
			if x[i] == y[j]:
				c[i][j] = c[i-1][j-1] + 1
				# 대각선으로 오면 1 저장 (같을 경우)
				b[i][j] = 1
			else:
				c[i][j] = max(c[i][j-1], c[i-1][j]) 
				# (max)왼쪽에서 오면 2, 위에서 오면 3(다를 경우)
				b[i][j] = 2 if (c[i][j-1] > c[i-1][j]) else 3
	return c, b

def get_lcs(i,j,b,x):
		if i==0 or j==0:
			return ""
		else:
			if b[i][j]==1:
				return get_lcs(i-1, j-1, b, x) + x[i] # 1인 경우에만 리턴
			elif b[i][j] == 2:
				return get_lcs(i,j-1,b,x)
			elif b[i][j] == 3:
				return get_lcs(i-1,j,b,x)

c, b = lcs(x, y)
print(c[len(x)][len(y)])
print(get_lcs(len(x), len(y), b, [' '] + x))