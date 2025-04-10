# 그리디
# 1. 거스름돈
N = int(input())
coins = [500, 100, 50, 10]
cnt = 0

for i in coins:
  cnt += N // i
  N %= i

print(cnt)

# 2. 1이 될 때까지
N, K = map(int, input().split())
cnt = 0

while (N != 1):
  if (N % K == 0):
    N /= K
  else:
    N -= 1
  cnt += 1

print(cnt)

# 3. 곱하기 또는 더하기
n = input()
result = int(n[0])

for i in range(1, len(n)):
  num = int(n[i])
  if result <= 1 or num < 1:
    result += num
  else:
    result *= num

print(result)

# 4. 모험가 길드
n = int(input())
adv = list(map(int, input().split()))
adv.sort()
result = 0
count = 0

for i in adv:
  count += 1
  if count >= i:
    result += 1
    count = 0

print(result)

