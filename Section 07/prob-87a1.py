from collections import deque
 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
def level_order_traversal(root):
    if not root:
        return []
 
    # Initialize a queue for BFS
    queue = deque([root])
    result = []
 
    while queue:
        level = []
        # Process all nodes at the current level
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
 
            # Enqueue left and right children
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
 
        # Add the current level to the result
        result.append(level)
 
    return result
