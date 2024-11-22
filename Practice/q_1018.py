import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [input() for _ in range(N)]
cnt = []
# 체스판 자르기 
for x in range(N-7):
    for y in range(M-7):
        start_W = 0 # W로 시작
        start_B = 0 # B로 시작
        for i in range(x, x+8):
            for j in range(y, y+8):
                # 짝수 = 시작 색, 홀수 != 시작 색 -> sum = cnt
                if (i + j) % 2 == 0:
                    if arr[i][j] == "B":
                        start_W += 1
                    else:
                        start_B += 1
                else:
                    if arr[i][j] == "B":
                        start_B += 1
                    else:
                        start_W += 1
        cnt.append(start_W)
        cnt.append(start_B)
print(min(cnt))
                    

    
    
    
