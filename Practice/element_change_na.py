import sys
inp = sys.stdin.readline

n, k = map(int, inp().split())
a = list(map(int, inp().split()))
b = list(map(int, inp().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]

print(sum(a))