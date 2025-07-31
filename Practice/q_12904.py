import sys
inp = sys.stdin.readline

S = inp().strip()
T = inp().strip()

# T -> S
# 끝이 A면 A제거
# B - B 제거 + 뒤집기 
while len(T) > len(S):
  if T[-1] == 'A':
    T = T[:-1]
  else:
    T = T[:-1][::-1]

print(1 if T == S else 0)