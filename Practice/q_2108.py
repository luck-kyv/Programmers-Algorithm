import sys
from collections import Counter

inp = sys.stdin.readline

n = int(inp())
arr = [int(inp()) for _ in range(n)]

mean = round(sum(arr)/n)

arr.sort()
median = arr[n//2]

counter = Counter(arr)
mode_list = counter.most_common() # (원소, 등장 횟수)
max_freq = mode_list[0][1] # 등장 횟수
modes = [num for num, freq in mode_list if freq == max_freq] # 최빈값 리스트
modes.sort()
mode = modes[0] if len(modes) == 1 else modes[1]

_range = arr[-1] - arr[0]

print(mean)
print(median)
print(mode)
print(_range)