n = int(input())
n_list = []
for _ in range(n):
    x, y = map(int, input().split())
    n_list.append([x,y])

n_list.sort(key=lambda x:(x[0], x[1]))
for _ in n_list:
    print(*_)