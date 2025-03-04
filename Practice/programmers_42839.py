"""
  for문 & 순열
  1. 모든 경우의 수 
  2. 소수만 sum
  시간 복잡도 : O(N^2)
"""
from itertools import permutations

def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def solution(numbers):
  answer = set()
  for i in range(1, len(numbers) + 1):
    for perm in permutations(numbers, i):
      num = int("".join(perm))
      answer.add(num)
  return sum(1 for num in answer if is_prime(num))

print(solution("17"))