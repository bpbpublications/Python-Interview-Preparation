def has_cycle_undirected(graph):
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
 
    visited = set()
 
    # Check for cycles starting from each node
    for node in graph:
        if node not in visited:
            if dfs(node, -1):  # Start DFS with no parent (-1)
                return True
    return False
