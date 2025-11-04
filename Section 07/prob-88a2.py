def zigzag_level_order_dfs(root):
    result = []
 
    def dfs(node, level):
        if not node:
            return
 
        # Create a new level if it doesn't exist
        if len(result) == level:
            result.append([])
 
        # Insert the node's value based on the level's direction
        if level % 2 == 0:
            result[level].append(node.val)  # Left to right
        else:
            result[level].insert(0, node.val)  # Right to left
 
        # Recur for the left and right children
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
 
    dfs(root, 0)
    return result
