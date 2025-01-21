N = 1000 - int(input())

coins = (500, 100, 50, 10, 5, 1)
cnt = 0

for coin in coins:
    cnt += N//coin
    N %= coin

print(cnt)