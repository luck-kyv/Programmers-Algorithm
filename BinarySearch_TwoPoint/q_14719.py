import sys

inp = sys.stdin.readline

h, w = map(int, inp().split())
block = list(map(int, inp().split()))

# two-point
# 작은쪽부터 갱신 (max값, cnt값 추가)

left, right = 0, w-1
left_max, right_max = block[left], block[right]
cnt = 0

while left < right:
  if left_max < right_max:
    left += 1
    left_max = max(left_max, block[left])
    cnt += max(0, left_max - block[left])
  else:
    right -= 1
    right_max = max(right_max, block[right])
    cnt += max(0, right_max - block[right])
  
print(cnt)

