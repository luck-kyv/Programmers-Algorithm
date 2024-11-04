import heapq
import sys

N = int(sys.stdin.readline())
t_list = []

for _ in range(N):
    S, T = map(int, sys.stdin.readline().split())
    t_list.append([S,T])

t_list.sort(key=lambda x : x[0]) #시작 기준 정렬 
end_time=[]
heapq.heappush(end_time, t_list[0][1])

for i in range(1, N):
    start, end = t_list[i]
    # 시작시간>=end_time -> 추가
    if start >= end_time[0]:
        heapq.heappop(end_time)
    
    heapq.heappush(end_time, end)

print(len(end_time))