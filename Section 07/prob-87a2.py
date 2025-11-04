def level_order_traversal_dfs(root):
    result = []
 
    def dfs(node, level):
        if not node:
            return
 
        # If the current level does not exist, create it
        if len(result) == level:
            result.append([])
 
        # Add the current node's value to the current level
        result[level].append(node.val)
 
        # Recur for the left and right children
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
 
    # Start DFS from the root
    dfs(root, 0)
    return result
