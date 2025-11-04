from collections import deque
 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
def zigzag_level_order(root):
    if not root:
        return []
 
    # Initialize the queue for BFS
    queue = deque([root])
    result = []
    left_to_right = True  # Start with left-to-right traversal
 
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
 
            # Enqueue left and right children
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
 
        # If we are traversing right to left, reverse the current level
        if not left_to_right:
            level.reverse()
 
        # Add the level to the result and toggle the direction
        result.append(level)
        left_to_right = not left_to_right  # Toggle the direction for next level
 
    return result
