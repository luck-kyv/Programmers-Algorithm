import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, current_sum = 0, 0
ans = float('inf')

for right in range(N):
    current_sum += arr[right]
    
    while current_sum >= S: # S 보다 크면
        ans = min(ans, right-left+1)
        current_sum -= arr[left] # left 빼고 이동
        left += 1
        
if ans == float('inf'):
    print(0)
else:
    print(ans)
