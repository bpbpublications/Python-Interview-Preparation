from collections import deque
 
def find_all_paths_bfs(graph, start, end):
    queue = deque([[start]])
    all_paths = []
 
    while queue:
        path = queue.popleft()
        node = path[-1]
 
        if node == end:
            all_paths.append(path)
        else:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
 
    return all_paths
