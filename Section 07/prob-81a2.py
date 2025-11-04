def lowest_common_ancestor_iterative(root, p, q):
    parent = {root: None}
    stack = [root]
 
    while p not in parent or q not in parent:
        node = stack.pop()
 
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
 
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
 
    ancestors = set()
 
    while p:
        ancestors.add(p)
        p = parent[p]
 
    while q not in ancestors:
        q = parent[q]
 
    return q
