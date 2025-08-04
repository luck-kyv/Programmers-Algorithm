import sys
from collections import deque

inp = sys.stdin.readline

T = int(inp())

for _ in range(T):
  p = inp().strip()
  n = int(inp())
  arr_temp = inp().strip()
  
  if arr_temp == "[]":
    arr = deque()
  else: 
    arr = deque(map(int, arr_temp[1:-1].split(",")))
  
  error_flag = False
  reverse_flag = False

  # R : 뒤집기 D : 빼기 -> reverse_flag T : pop F : popleft
  # not arr : print("error"), error_flag = True, break
  for cmd in p:
    if cmd == "R":
      reverse_flag = not reverse_flag
    else:
      if not arr:
        print("error")
        error_flag = True
        break
      
      if reverse_flag:
        arr.pop()
      else:
        arr.popleft()
      
  if not error_flag:
    if reverse_flag:
      arr.reverse()
    print("["+",".join(map(str, arr))+"]")
