class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
def is_symmetric(root):
    # Helper function to compare two subtrees
    def is_mirror(left, right):
        # Base case: if both nodes are None, they are symmetric
        if not left and not right:
            return True
        # If one is None and the other is not, they are not symmetric
        if not left or not right:
            return False
        # Check if the values are the same and the subtrees are mirrors
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))
 
    # An empty tree is symmetric
    if not root:
        return True
 
    # Start comparing the left and right subtrees
    return is_mirror(root.left, root.right)
