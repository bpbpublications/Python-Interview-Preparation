def dfs(maze, x, y, visited):
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        return 1  # Reached the destination
 
    visited.add((x, y))
 
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    min_path = float('inf')
 
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and (nx, ny) not in visited and maze[nx][ny] == 0:
            path_length = dfs(maze, nx, ny, visited)
            if path_length != -1:
                min_path = min(min_path, path_length + 1)
 
    visited.remove((x, y))
 
    return min_path if min_path != float('inf') else -1
