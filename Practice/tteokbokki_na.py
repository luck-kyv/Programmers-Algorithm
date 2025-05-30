import sys
inp = sys.stdin.readline

n, m = map(int, inp().split())
tteok = list(map(int, inp().split()))

start = 0
end = max(tteok)

result = 0

while start <= end:
  mid = (start + end) // 2
  total = 0
  for x in tteok:
    if x > mid:
      total += x - mid

  if total >= m:
    result = mid
    start = mid + 1
  else: 
    end = mid - 1

print(result) 
