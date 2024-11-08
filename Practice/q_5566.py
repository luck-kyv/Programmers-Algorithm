import sys
input = sys.stdin.readline

N, M = map(int, input().split())
game = []
dice = []
for _ in range(N):
    game.append(int(input()))
for _ in range(M):
    dice.append(int(input()))

pos = 0
cnt = 0

for i in range(M):
    cnt += 1
    pos += dice[i]
    if pos >= N-1 :
        break    
    pos += game[pos]
    if pos >= N-1:
        break

print(cnt)