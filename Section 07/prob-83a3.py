from collections import deque
 
def invert_tree_bfs(root):
    if not root:
        return None
 
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left  # Swap children
            queue.append(node.left)
            queue.append(node.right)
 
    return root
