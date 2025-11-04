from collections import deque
 
def find_connected_components_bfs(graph):
    visited = set()
    components = []
 
    for node in graph:
        if node not in visited:
            component = []
            queue = deque([node])
            visited.add(node)
 
            while queue:
                current = queue.popleft()
                component.append(current)
 
                for neighbor in graph.get(current, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
 
            components.append(component)
 
    return components
