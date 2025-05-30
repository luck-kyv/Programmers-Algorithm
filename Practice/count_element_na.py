from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

def binary_search(array, target):
  left_side = bisect_left(array, target)
  right_side = bisect_right(array, target)
  return right_side - left_side

cnt = binary_search(array, x)

# x인 원소가 존재하지 않는다면 
if cnt == 0:
	print(-1)
else:
	print(cnt)