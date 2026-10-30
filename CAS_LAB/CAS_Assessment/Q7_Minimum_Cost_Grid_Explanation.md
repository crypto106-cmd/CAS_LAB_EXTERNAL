# Q7: Minimum Cost Path in a Grid — Complete Explanation

---

## A. Understanding the Problem

### What is the question asking?
Given an m × n grid of positive integers (costs), find the **minimum total cost** to travel from the **top-left corner** (0,0) to the **bottom-right corner** (m-1, n-1). You can only move **right** or **down**.

### What input do we receive?
- First line: `m` (rows) and `n` (columns).
- Next m lines: n positive integers per line (the cost grid).

### What output do we produce?
- A single integer: the minimum path cost including both endpoints.

### Small Example
```
Grid:
1 3 1
1 5 1
4 2 1

Possible paths (showing costs):
Path 1: 1 → 3 → 1 → 1 → 1 = 7    (right, right, down, down)
Path 2: 1 → 1 → 5 → 1 → 1 = 9    (down, right, right, down)  -- wait, no.

Actually: Right/Down only:
1 → 3 → 1 → 1 → 1 = 7  (Right, Right, Down, Down)
1 → 1 → 4 → 2 → 1 = 9  (Down, Down, Right, Right)
1 → 1 → 5 → 2 → 1 = 10 (Down, Right, Right, Down - wait, not valid)

Minimum = 7
```

---

## B. Algorithm and Approach

### Approach: Dynamic Programming (Bottom-Up)

**Key Insight**: To reach cell (i, j), you can only come from:
- The cell above: (i-1, j)
- The cell to the left: (i, j-1)

So the minimum cost to reach (i, j) is:
```
dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
```

### Step-by-Step Logic:
1. Create a DP array of size n (one row).
2. **First row**: Each cell can only be reached from the left, so `dp[j] = dp[j-1] + grid[0][j]`.
3. **First column** of each subsequent row: Can only come from above, so `dp[0] = dp[0] + grid[i][0]`.
4. **Other cells**: `dp[j] = min(dp[j], dp[j-1]) + grid[i][j]` where:
   - `dp[j]` (before update) = cost from above (previous row's value).
   - `dp[j-1]` (after update) = cost from the left (current row's value).
5. After processing all rows, `dp[n-1]` has the answer.

### Space Optimization
- A full 2D DP table would use O(m × n) space.
- Since we only need the previous row's values, we can reuse a single 1D array of size n.
- This gives us O(n) auxiliary space, as requested by the PDF.

---

## C. Complete Python Code

```python
def minimum_cost_path():
    first_line = input().split()
    m = int(first_line[0])
    n = int(first_line[1])
    
    grid = []
    for i in range(m):
        row = list(map(int, input().split()))
        grid.append(row)
    
    dp = [0] * n
    dp[0] = grid[0][0]
    
    for j in range(1, n):
        dp[j] = dp[j - 1] + grid[0][j]
    
    for i in range(1, m):
        dp[0] = dp[0] + grid[i][0]
        for j in range(1, n):
            dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
    
    print(dp[n - 1])

minimum_cost_path()
```

---

## D. Public Test Cases

### Test Case 1
**Input:**
```
3 3
1 3 1
1 5 1
4 2 1
```
**Expected Output:**
```
7
```
**Explanation:**
DP table construction:
```
Row 0: dp = [1, 4, 5]
  dp[0]=1, dp[1]=1+3=4, dp[2]=4+1=5

Row 1: 
  dp[0] = 1+1 = 2
  dp[1] = min(4, 2)+5 = 2+5 = 7
  dp[2] = min(5, 7)+1 = 5+1 = 6

Row 2:
  dp[0] = 2+4 = 6
  dp[1] = min(7, 6)+2 = 6+2 = 8
  dp[2] = min(6, 8)+1 = 6+1 = 7
```
Answer: dp[2] = **7**

The optimal path: (0,0)→(1,0)→(1,1) — wait, let me recalculate.

Path: 1 → 3 → 1 → 1 → 1 = 7 (Right, Right, Down, Down) ✓

### Test Case 2
**Input:**
```
2 3
1 2 3
4 5 6
```
**Expected Output:**
```
12
```
**Explanation:**
DP table:
```
Row 0: dp = [1, 3, 6]
  dp[0]=1, dp[1]=1+2=3, dp[2]=3+3=6

Row 1:
  dp[0] = 1+4 = 5
  dp[1] = min(3, 5)+5 = 3+5 = 8
  dp[2] = min(6, 8)+6 = 6+6 = 12
```
Answer: dp[2] = **12**

Path: 1 → 2 → 3 → 6 = 12 (Right, Right, Down) ✓

---

## E. Detailed Code Explanation

### Line: `dp = [0] * n`
- Creates a list of n zeros.
- This will store the minimum cost to reach each column in the current row.

### Line: `dp[0] = grid[0][0]`
- The cost to reach the starting cell is just its own value.

### Lines: First row initialization
```python
for j in range(1, n):
    dp[j] = dp[j - 1] + grid[0][j]
```
- In the first row, you can only move right.
- So the cost to reach column j = cost to reach column j-1 + grid value at (0, j).
- This builds cumulative costs: [1, 1+3=4, 4+1=5]

### Lines: Processing remaining rows
```python
for i in range(1, m):
    dp[0] = dp[0] + grid[i][0]
```
- First column: can only come from above.
- `dp[0]` already holds the cost from the previous row, so just add the current cell's value.

### Lines: Inner loop
```python
for j in range(1, n):
    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
```
- `dp[j]` (before update) = cost to reach (i-1, j) from above.
- `dp[j-1]` (already updated) = cost to reach (i, j-1) from the left.
- Take the minimum and add the current cell's cost.

### Line: `print(dp[n - 1])`
- After processing all rows, `dp[n-1]` holds the minimum cost to reach the bottom-right corner.

---

## F. Python Syntax Explanation

### `list(map(int, input().split()))`
- `input()` reads a line as a string.
- `.split()` splits by whitespace into a list of strings.
- `map(int, ...)` converts each string to an integer.
- `list(...)` collects the results into a list.
- Example: `"1 3 1"` → `[1, 3, 1]`

### `[0] * n`
- Creates a list of n zeros: `[0, 0, 0, ...]`.
- This is list multiplication.

### `min(a, b)`
- Returns the smaller of two values.
- `min(4, 2)` → `2`.

### `range(1, n)`
- Generates numbers from 1 to n-1 (inclusive).
- We start from 1 because index 0 is handled separately.

---

## G. Why This Method and Not Another Method?

### Why Dynamic Programming?
- The problem has **optimal substructure**: the optimal path to (i,j) depends on optimal paths to (i-1,j) and (i,j-1).
- The problem has **overlapping subproblems**: the cost to reach intermediate cells is reused.
- These two properties make DP the perfect approach.

### Alternative 1: Brute Force / Recursion
- Try all possible paths (right or down at each step).
- Number of paths = C(m+n-2, m-1) — exponential.
- **Rejected** — way too slow.

### Alternative 2: Recursion with Memoization (Top-Down DP)
- Define `cost(i, j)` = minimum cost to reach (i, j).
- Use memoization to avoid recomputing.
- Same O(m × n) time but uses O(m × n) space for the memo table + recursion stack.
- **Valid** but bottom-up DP with O(n) space is better.

### Alternative 3: Dijkstra's Algorithm
- Treat the grid as a graph and use Dijkstra.
- Would work but overkill — O(mn log(mn)) vs O(mn).
- **Rejected** because DP is simpler and faster.

### Why O(n) space?
- We process the grid row by row.
- To compute row i, we only need row i-1's values.
- So we reuse a single 1D array instead of a 2D table.
- The PDF specifically mentions O(n) auxiliary space is possible.

---

## H. Time and Space Complexity

### Time Complexity: O(m × n)
- We process each cell exactly once.
- m rows × n columns = m × n cells.
- Each cell requires O(1) work (min + add).

### Space Complexity: O(n) auxiliary
- The `dp` array has n elements.
- We also store the grid (O(m × n)), but the PDF asks for O(n) *auxiliary* space.
- "Auxiliary" means extra space beyond the input.

### Why not O(m × n) space?
- A full 2D DP table would be O(m × n).
- Since we only need one row at a time, we optimize to O(n).
- For m, n = 500, this saves 250,000 integers of space.

---

## I. Faculty Viva Questions and Answers

### Q1: What is dynamic programming?
**A:** Dynamic programming is a technique that solves complex problems by breaking them into smaller overlapping subproblems. It solves each subproblem once and stores the result to avoid redundant computation.

### Q2: What is optimal substructure?
**A:** A problem has optimal substructure if the optimal solution to the problem contains optimal solutions to its subproblems. Here, the minimum cost path to (i,j) must pass through either (i-1,j) or (i,j-1) with their own minimum costs.

### Q3: What is overlapping subproblems?
**A:** When the same subproblem is solved multiple times. Without DP, calculating the cost to reach (2,2) would recompute costs for (1,2), (2,1), (1,1), etc. DP stores these values to avoid recomputation.

### Q4: Why can we only move right or down?
**A:** This is a constraint given in the problem. It simplifies the problem to a DP problem because it ensures there are no cycles (you always move towards the bottom-right).

### Q5: How does the space optimization work?
**A:** We process the grid row by row. When computing row i, `dp[j]` (before update) contains the value from row i-1 (above), and `dp[j-1]` (after update) contains the value from the current row (left). So one array suffices.

### Q6: Could the grid have negative values?
**A:** The problem says "positive costs," so no. If it did, the algorithm would still work because we're just taking minimums. Negative values don't affect the DP logic.

### Q7: What is the difference between top-down and bottom-up DP?
**A:** Top-down uses recursion + memoization (start from the final answer and break down). Bottom-up uses iteration (start from base cases and build up). Bottom-up is usually more space-efficient and avoids recursion overhead.

### Q8: Can this problem be solved with greedy?
**A:** No. A greedy approach (always choosing the smaller neighbor) doesn't guarantee the global minimum. For example, a cheap cell might lead to expensive cells later.

### Q9: What is the base case?
**A:** `dp[0] = grid[0][0]` — the cost to reach the starting cell is just its own cost. The first row and first column are also base cases with cumulative sums.

### Q10: What if we could also move left and up?
**A:** Then DP wouldn't work directly because there would be cycles. We'd need Dijkstra's algorithm or BFS to handle all four directions.

### Q11: What does `min(dp[j], dp[j-1])` represent?
**A:** `dp[j]` = cost from above (row i-1, column j). `dp[j-1]` = cost from the left (row i, column j-1). We take the minimum because we want the cheapest way to reach (i, j).

### Q12: How many total paths exist in an m × n grid?
**A:** C(m+n-2, m-1) = (m+n-2)! / ((m-1)! × (n-1)!). For a 3×3 grid: C(4,2) = 6 paths. DP avoids enumerating all paths by building optimal solutions incrementally.

---

## J. VS Code Execution

### Terminal Example — Test Case 1:
```
PS C:\...\CAS_Assessment> python Q7_Minimum_Cost_Grid.py
3 3
1 3 1
1 5 1
4 2 1
7
```

### Terminal Example — Test Case 2:
```
PS C:\...\CAS_Assessment> python Q7_Minimum_Cost_Grid.py
2 3
1 2 3
4 5 6
12
```

---

## K. Quick Revision

| Item | Details |
|------|---------|
| **Algorithm** | Bottom-Up Dynamic Programming |
| **Data Structure** | 1D array (space-optimized DP) |
| **Core Logic** | 1. Initialize first row with cumulative sums. 2. For each subsequent row, dp[j] = min(from above, from left) + current cell. 3. Answer is dp[n-1]. |
| **Memory Trick** | "dp[j] = min(above, left) + cost. One row is enough!" |
| **One Sentence** | Use a 1D DP array to compute the minimum cumulative cost from top-left to bottom-right, choosing the cheaper path (from above or left) at each cell. |
