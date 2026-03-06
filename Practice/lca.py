# Lowest common ancestor of binary tree 
def LCA(root, p, q):
    # base case
    if root is None:
        return None

    # postorder
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    
    # p, q
    if root == p or root == q:
        return root
    
    # left & right
    elif left and right:
        return root
    
    # other
    return left or right