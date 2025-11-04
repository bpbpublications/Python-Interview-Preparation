from collections import deque
 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
def serialize(root):
    if not root:
        return "null"
 
    result = []
    queue = deque([root])
 
    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")
 
    return ",".join(result)
 
def deserialize(data):
    if data == "null":
        return None
 
    values = data.split(",")
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1
 
    while queue:
        node = queue.popleft()
 
        if values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1
 
        if values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1
 
    return root
