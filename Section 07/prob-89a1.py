def numIslands(grid):
    if not grid:
        return 0
 
    def dfs(grid, i, j):
        # Base case: if out of bounds or at water ('0'), return
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
 
        # Mark the current cell as visited by setting it to '0'
        grid[i][j] = '0'
 
        # Visit all 4 adjacent cells (up, down, left, right)
        dfs(grid, i-1, j)  # Up
        dfs(grid, i+1, j)  # Down
        dfs(grid, i, j-1)  # Left
        dfs(grid, i, j+1)  # Right
 
    island_count = 0
 
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':  # Found an unvisited island
                dfs(grid, i, j)    # Perform DFS to visit the entire island
                island_count += 1  # Increase the island count
 
    return island_count
