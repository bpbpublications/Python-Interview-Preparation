from collections import deque
 
def shortest_path_in_maze(maze):
    rows, cols = len(maze), len(maze[0])
 
    # Directions for moving up, down, left, right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
 
    # Check if the start or end point is blocked
    if maze[0][0] == 1 or maze[rows-1][cols-1] == 1:
        return -1
 
    # Initialize BFS queue with starting position (0, 0) and step count 1
    queue = deque([(0, 0, 1)])  # (row, col, steps)
    visited = set((0, 0))
 
    while queue:
        x, y, steps = queue.popleft()
 
        # If we've reached the bottom-right corner, return the steps
        if x == rows - 1 and y == cols - 1:
            return steps
 
        # Explore the four possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
 
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and maze[nx][ny] == 0:
                queue.append((nx, ny, steps + 1))
                visited.add((nx, ny))
 
    # If no path is found, return -1
    return -1
