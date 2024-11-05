import sys
input=sys.stdin.readline

n = int(input())
n_list = []
for _ in range(n):
    n_list.append(int(input()))

for _ in sorted(n_list):
    print(_)