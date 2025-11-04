from collections import deque
 
def max_depth_bfs(root):
    if not root:
        return 0
 
    queue = deque([root])
    depth = 0
 
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth += 1
 
    return depth
