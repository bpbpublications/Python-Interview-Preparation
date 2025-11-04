def find_connected_components(graph):
    def dfs(node, component):
        visited.add(node)
        component.append(node)
 
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, component)
 
    visited = set()
    components = []
 
    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)
 
    return components
