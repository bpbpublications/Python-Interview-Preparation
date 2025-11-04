def invert_tree_iterative(root):
    if not root:
        return None
 
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left  # Swap children
            stack.append(node.left)
            stack.append(node.right)
 
    return root
