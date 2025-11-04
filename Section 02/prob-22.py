class Node:
    def __init__(self, data):
        # Each node has data and pointers to its left and right children
        self.data = data
        self.left = None
        self.right = None
 
class BinaryTree:
    def __init__(self, root):
        # Initialize the binary tree with a root node
        self.root = Node(root)
 
    def insert(self, data):
        # Insert data into the binary tree (level-order insertion)
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = Node(data)
                return
            else:
                queue.append(current.left)
            if not current.right:
                current.right = Node(data)
                return
            else:
                queue.append(current.right)
 
    def inorder_traversal(self, node, result):
        # Perform in-order traversal (Left, Root, Right)
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)
 
    def preorder_traversal(self, node, result):
        # Perform pre-order traversal (Root, Left, Right)
        if node:
            result.append(node.data)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
 
    def postorder_traversal(self, node, result):
        # Perform post-order traversal (Left, Right, Root)
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.data)
 
    def print_traversal(self):
        # Print the results of all three traversals
        inorder_result = []
        preorder_result = []
        postorder_result = []
 
        self.inorder_traversal(self.root, inorder_result)
        self.preorder_traversal(self.root, preorder_result)
        self.postorder_traversal(self.root, postorder_result)
 
        print(f"In-order Traversal: {' -> '.join(map(str, inorder_result))}")
        print(f"Pre-order Traversal: {' -> '.join(map(str, preorder_result))}")
        print(f"Post-order Traversal: {' -> '.join(map(str, postorder_result))}")
