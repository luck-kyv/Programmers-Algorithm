import sys
inp = sys.stdin.readline

n = int(inp())
papers = [list(map(int, inp().split())) for _ in range(n)]

# 100x100 배열에 색종이 부분을 1로 채우기
field = [[0]*100 for _ in range(100)]

for a, b in papers:
    for i in range(10):
        for j in range(10):
            field[a+i][b+j] = 1

total = 0
for row in field:
    total += sum(row)

print(total)