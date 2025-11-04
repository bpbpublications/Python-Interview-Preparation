def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    result = []
 
    def dfs_recursive(node):
        if node not in visited:
            result.append(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
 
    dfs_recursive(start)
    return result
