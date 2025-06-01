import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))

def is_possible(size):
  cnt = 1
  total = 0
  for l in lectures:
    if total + l > size:
      cnt += 1
      total = l
    else:
      total += l
  return cnt <= m


start = max(lectures)
end = sum(lectures)
answer = end

while start <= end:
  mid = (start + end) // 2
  if is_possible(mid):
    answer = mid
    end = mid - 1
  else:
    start = mid + 1

print(answer)