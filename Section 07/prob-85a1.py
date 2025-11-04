class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
def is_valid_bst(root):
    def inorder(node, prev):
        if not node:
            return True
        if not inorder(node.left, prev):
            return False
        if prev[0] is not None and node.val <= prev[0]:
            return False
        prev[0] = node.val
        return inorder(node.right, prev)
 
    return inorder(root, [None])
