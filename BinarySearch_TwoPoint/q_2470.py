import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

ans = []

def binary_search(arr, num):
    start, end = 0, len(ans)-1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < num:
            start = mid + 1
        # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
        else:
            end = mid - 1

    return start

for num in arr:
    pos = binary_search(ans, num) # num이 들어갈 위치 반환 
    
    if pos < len(ans):
        ans[pos] = num
    else:
        ans.append(num)

print(len(ans))
