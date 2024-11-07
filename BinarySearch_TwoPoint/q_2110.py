import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(int(input())) 

arr.sort()

min_dis, max_dis = 1, arr[-1] - arr[0]
ans = 0

def can_put(dis):
    cnt = 1
    last = arr[0] # 1st 집에 설치했다고 가정

    for i in range(1, N):
        if arr[i] - last >= dis :
            cnt += 1
            last = arr[i]
    
    return cnt >= C

while min_dis <= max_dis:
    mid = (min_dis + max_dis) // 2

    # 원하는 값 찾은 경우 인덱스 반환
    if can_put(mid):
        ans = mid
        min_dis = mid + 1
    else:
        max_dis = mid - 1

print(ans)