import sys
inp = sys.stdin.readline

n = int(inp())
tree = {}
for _ in range(n):
    root, left, right = inp().split()
    tree[root] = (left, right)

def preorder(node):
    if node == '.':
        return None
    print(node, end='')
    left, right = tree[node]
    preorder(left)
    preorder(right)

def inorder(node):
    if node == '.':
        return None
    left, right = tree[node]
    inorder(left)
    print(node, end='')
    inorder(right)

def postorder(node):
    if node == '.':
        return None
    left, right = tree[node]
    postorder(left)
    postorder(right)
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')