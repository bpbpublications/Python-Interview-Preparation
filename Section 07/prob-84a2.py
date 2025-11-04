def serialize_dfs(root):
    def dfs(node):
        if not node:
            return "null,"
        return str(node.val) + "," + dfs(node.left) + dfs(node.right)
 
    return dfs(root)
 
def deserialize_dfs(data):
    def dfs(nodes):
        val = nodes.pop(0)
        if val == "null":
            return None
        node = TreeNode(int(val))
        node.left = dfs(nodes)
        node.right = dfs(nodes)
        return node
 
    node_list = data.split(",")
    return dfs(node_list)
