import sys
from bisect import bisect_left, bisect_right
inp = sys.stdin.readline

n = int(inp())
array1 = sorted(list(map(int, inp().split())))
m = int(inp())
array2 = list(map(int, inp().split()))

def binary_search(array, target):
  right_side = bisect_right(array, target)
  left_side = bisect_left(array, target)
  return right_side - left_side

for i in range(m):
  print(binary_search(array1, array2[i]), end=' ')