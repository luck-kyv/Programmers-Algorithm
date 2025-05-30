import sys
inp = sys.stdin.readline

n = int(inp())
words = set(inp() for _ in range(n))
sort_words = sorted(words, key=lambda x: (len(x), x))
for word in sort_words:
  print(word, end='')