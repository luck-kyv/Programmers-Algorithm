# 구현
# 1. 상하좌우
n = int(input())
plans = list(input().split())

# L R U D
move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x, y = 1, 1

for plan in plans:
  for i in range(4):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
      if 1 <= nx <= n and 1 <= ny <= n:
        x, y = nx, ny
      break
print(x, y)

# 2. 시각

n = int(input())
cnt = 0
for hour in range(n+1):
  for minute in range(60):
    for second in range(60):
      if '3' in f'{hour}{minute}{second}':
        cnt += 1

print(cnt)

# 3. 왕실의 나이트
x, y = input()
cnt = 0

# 방향
dx = [-1, -1, 1, 1, -2, -2, 2, 2]
dy = [-2, 2, -2, 2, -1, 1, -1, 1]

for i in range(8):
  nx = ord(x) + dx[i]
  ny = int(y) + dy[i]
  if 97 <= nx <= 104 and 1 <= ny <= 8:
    cnt += 1

print(cnt)

# 4. 문자열 재정렬
data = input()
result = []
c_sum = 0

for c in data:
  if c.isalpha():
    result.append(c)
  else:
    c_sum += int(c)

result.sort()

if c_sum != 0:
  result.append(str(c_sum))
print(''.join(result))