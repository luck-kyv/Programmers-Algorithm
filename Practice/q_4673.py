def d(n):
  return n + sum(map(int, str(n)))

num = set(range(1, 10001))

for i in range(1, 10001):
  temp = d(i)
  if temp <= 10000:
    num.discard(temp)

for n in sorted(num):
  print(n)