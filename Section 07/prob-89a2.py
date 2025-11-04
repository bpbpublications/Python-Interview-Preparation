from collections import deque
 
def numIslands(grid):
    if not grid:
        return 0
 
    def bfs(grid, i, j):
        queue = deque([(i, j)])
        grid[i][j] = '0'
 
        while queue:
            x, y = queue.popleft()
 
            # Check all 4 adjacent directions
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
 
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '1':
                    queue.append((new_x, new_y))
                    grid[new_x][new_y] = '0'  # Mark as visited
 
    island_count = 0
 
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':  # Found an unvisited island
                bfs(grid, i, j)    # Perform BFS to visit the entire island
                island_count += 1  # Increase the island count
 
    return island_count
