from collections import deque
 
def is_symmetric(root):
    # A tree is symmetric if the left and right subtrees are mirrors
    if not root:
        return True
 
    # Use a queue to store the pairs of nodes to compare
    queue = deque([(root.left, root.right)])
 
    while queue:
        left, right = queue.popleft()
 
        # If both are None, continue
        if not left and not right:
            continue
        # If one is None or values are different, the tree is not symmetric
        if not left or not right or left.val != right.val:
            return False
 
        # Enqueue the children in reverse order to check for mirror symmetry
        queue.append((left.left, right.right))
        queue.append((left.right, right.left))
 
    return True
