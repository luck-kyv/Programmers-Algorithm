import sys
inp = sys.stdin.readline

n = int(inp())

board = [list(inp().strip()) for _ in range(n)]

# 모든 칸 스왑 - 개수 세기(같은 건 제외) - 다시 복원 
# 개수 세기 함수
def cnt_max():
    longest = 1

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > longest:
                longest = cnt
    
    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if board[i][j] == board[i-1][j]:
                cnt += 1
            else:
                cnt = 1
            if cnt > longest:
                longest = cnt
    return longest

answer = cnt_max()

for i in range(n):
    for j in range(n):
        if j+1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 스왑
            answer = max(answer, cnt_max()) # 검사 
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 복원
        if i+1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j] # 스왑
            answer = max(answer, cnt_max()) # 검사 
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j] # 복원

print(answer)
# 다시 풀기
