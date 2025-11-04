def find_all_paths(graph, start, end):
    def dfs(node, path):
        path.append(node)
 
        if node == end:
            # If the current node is the destination, add the path to the results
            all_paths.append(list(path))
        else:
            # Explore all neighbors
            for neighbor in graph.get(node, []):
                dfs(neighbor, path)
 
        # Backtrack: remove the current node from the path
        path.pop()
 
    all_paths = []
    dfs(start, [])
    return all_paths
