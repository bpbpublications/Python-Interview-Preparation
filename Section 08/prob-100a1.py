class DisjointSet:
    def __init__(self, n):
        # Initialize parent and rank arrays for n elements
        self.parent = [i for i in range(n)]  # Each element is its own parent initially
        self.rank = [1] * n  # Rank is initialized to 1 for all sets
 
    def find(self, x):
        """Find the representative of the set that x belongs to, with path compression."""
        if self.parent[x] != x:
            # Recursively find the parent and apply path compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
 
    def union(self, x, y):
        """Union the sets containing x and y using union by rank."""
        root_x = self.find(x)
        root_y = self.find(y)
 
        if root_x != root_y:
            # Union by rank: attach smaller rank tree under the larger rank tree
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                # If ranks are equal, arbitrarily choose one root and increment its rank
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
        else:
            print(f"{x} and {y} are already in the same set")
