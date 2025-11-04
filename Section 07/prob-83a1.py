class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left  # Swap children
    invert_tree(root.left)  # Recursively invert left subtree
    invert_tree(root.right)  # Recursively invert right subtree
    return root
