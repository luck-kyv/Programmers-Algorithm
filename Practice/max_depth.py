# Maximum Depth of binary tree
# 1. Level Order 방식
from collections import deque

def maxDepth1(root):
	max_depth = 0
	if root is None:
		return max_depth
	q = deque()
	q.append((root, 1))
	while q:
		cur_node, cur_depth = q.popleft()
		max_depth = max(max_depth, cur_depth)
		if cur_node.left:
			q.append((cur_node.left, cur_depth + 1))
		if cur_node.right:
			q.append((cur_node.right, cur_depth + 1))
	
	return max_depth

# 2. Post Order 방식
# def maxDepth2(root):
# 	max_depth = 0
	
#     if root is None:
#         return max_depth

#     left_depth = maxDepth2(root.left)
#     right_depth = maxDepth2(root.right)
#     max_depth = max(left_depth, right_depth) + 1
#     return max_depth

# root = [3, 9, 20, None, None, 15, 7] 직접 구현
class TreeNode:
	def __init__(self, l=None, r=None, v=0):
		self.left = l
		self.right = r
		self.val = v 

root = TreeNode(v=3)
root.left = TreeNode(v=9)
root.right = TreeNode(v=20)
root.right.left = TreeNode(v=15)
root.right.right = TreeNode(v=7)

print(maxDepth2(root))