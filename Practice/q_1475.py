import sys, math
from collections import Counter 

inp = sys.stdin.readline 

n = inp().strip()
counter = Counter(n)

# 6, 9 호환
counter['6'] = math.ceil((counter['6'] + counter['9']) / 2)
counter['9'] = 0

print(max(counter.values()))
