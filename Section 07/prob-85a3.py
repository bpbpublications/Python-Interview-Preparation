def is_valid_bst(root):
    stack = []
    prev = None
 
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev is not None and root.val <= prev:
            return False
        prev = root.val
        root = root.right
 
    return True
