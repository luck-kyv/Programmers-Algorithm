import sys
from itertools import permutations
input = sys.stdin.readline

words = [input().strip() for _ in range(6)]
results = []

for rows in permutations(words, 3):
    cols = words[:]
    for word in rows:
        cols.remove(word)

    if (rows[0][0] + rows[1][0] + rows[2][0] == cols[0] and
        rows[0][1] + rows[1][1] + rows[2][1] == cols[1] and
        rows[0][2] + rows[1][2] + rows[2][2] == cols[2]):
        results.append(rows)

if results:
    results.sort()
    for row in results[0]:
        print(row)
else:
    print(0)