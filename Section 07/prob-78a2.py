def has_cycle_directed(graph):
    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
 
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
 
        rec_stack.remove(node)
        return False
 
    visited = set()
    rec_stack = set()
 
    # Start DFS from every node to cover disconnected components
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False
