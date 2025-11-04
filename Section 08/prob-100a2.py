class SimpleDisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
 
    def find(self, x):
        """Find the root of the set containing x."""
        while self.parent[x] != x:
            x = self.parent[x]
        return x
 
    def union(self, x, y):
        """Union the sets containing x and y."""
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
 
# Example usage
ds = SimpleDisjointSet(5)
ds.union(0, 1)
ds.union(1, 2)
ds.union(3, 4)
print(ds.find(0))  # Output: 0
print(ds.find(4))  # Output: 3
print(ds.find(2))  # Output: 0
