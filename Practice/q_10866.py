import sys
from collections import deque

inp = sys.stdin.readline

q = deque()

N = int(inp())

for _ in range(N):
    command = inp().split()

    if command[0] == "push_front":
        q.appendleft(int(command[1]))
    elif command[0] == "push_back":
        q.append(int(command[1]))
    elif command[0] == "pop_front":
        print(q.popleft() if len(q) != 0 else -1)
    elif command[0] == "pop_back":
        print(q.pop() if len(q) != 0 else -1)
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        print(1 if len(q) == 0 else 0)
    elif command[0] == "front":
        print(q[0] if len(q) != 0 else -1)
    elif command[0] == "back":
        print(q[-1] if len(q) != 0 else -1)