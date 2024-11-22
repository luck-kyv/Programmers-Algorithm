import sys
from collections import deque
input = sys.stdin.readline

n_case = int(input())
test_cases = []
for _ in range(n_case):
    n_gs = int(input())
    pos = [list(map(int, input().split())) for _ in range(n_gs + 2)]
    test_cases.append({
        "n_gs" : n_gs,
        "pos": pos
    })

#print(pos)
def cal_dis(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for t in test_cases:
    n_gs = t["n_gs"]
    pos = t["pos"]

    visited = [False] * (n_gs + 2)
    q = deque([0])
    visited[0] = True

    while q:
        current = q.pop(0)
        for idx in range(n_gs + 2):
            if not visited[idx] and cal_dis(pos[current], pos[idx]) <= 1000:
                visited[idx] = True
                q.append(idx)

    if visited[-1]:
        print("happy")
    else:
        print("sad")