# Q7: Minimum Cost Path in a Grid
# Algorithm: Dynamic Programming (bottom-up)
# Time Complexity: O(m * n) | Space Complexity: O(n) auxiliary

def minimum_cost_path():
    """
    Find the minimum cost path from top-left to bottom-right
    in a grid, moving only right or down.
    Uses DP with O(n) space optimization.
    """
    # Read grid dimensions
    first_line = input().split()
    m = int(first_line[0])  # rows
    n = int(first_line[1])  # columns
    
    # Read the grid
    grid = []
    for i in range(m):
        row = list(map(int, input().split()))
        grid.append(row)
    
    # DP using a single row (space optimization)
    # dp[j] = minimum cost to reach cell (current_row, j)
    dp = [0] * n
    
    # Initialize first cell
    dp[0] = grid[0][0]
    
    # Fill first row: can only come from the left
    for j in range(1, n):
        dp[j] = dp[j - 1] + grid[0][j]
    
    # Fill remaining rows
    for i in range(1, m):
        # First column: can only come from above
        dp[0] = dp[0] + grid[i][0]
        
        # Other columns: min of coming from left or above
        for j in range(1, n):
            dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
    
    # The answer is the minimum cost to reach bottom-right
    print(dp[n - 1])


# ---- Main Program ----
minimum_cost_path()
