import sys
inp = sys.stdin.readline

n, k = map(int, inp().split())
cnt = 0
# coins 리스트 
coins = [int(inp()) for _ in range(n)]
coins.reverse()
# for -> 몫 cnt에 저장, 나머지 k에 저장
for i in coins:
  cnt += k//i
  k %= i

print(cnt)
