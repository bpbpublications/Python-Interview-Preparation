from collections import deque
 
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []
 
    while queue:
        node = queue.popleft()
        if node not in visited:
            result.append(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return result
