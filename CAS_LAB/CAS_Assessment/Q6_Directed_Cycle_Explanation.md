# Q6: Detect a Cycle in a Directed Graph — Complete Explanation

---

## A. Understanding the Problem

### What is the question asking?
Given a **directed graph** with V vertices and E edges, determine whether the graph contains a **cycle**.

### What is a directed graph?
A graph where edges have a direction. An edge from A to B means you can go from A to B but NOT from B to A (unless there's another edge).

### What is a cycle?
A cycle exists when you can start from a vertex, follow edges, and return to the same vertex. For example: 0 → 1 → 2 → 0 is a cycle.

### What input do we receive?
- First line: V (number of vertices) and E (number of edges).
- Next E lines: `u v` representing a directed edge from u to v.
- Vertices are numbered from 0 to V-1.

### What output do we produce?
- Print `YES` if the graph contains a cycle.
- Print `NO` otherwise.

### Small Example
```
Graph: 0 → 1 → 2 → 0 (3 vertices, 3 edges)
This forms a cycle: 0 → 1 → 2 → 0
Output: YES

Graph: 0 → 1 → 2 → 3 (4 vertices, 3 edges)
No cycle — it's a straight path.
Output: NO
```

---

## B. Algorithm and Approach

### Approach: DFS with Three Colors (White-Gray-Black)

We use DFS (Depth-First Search) with a **coloring scheme**:
- **WHITE (0)**: Not visited yet.
- **GRAY (1)**: Currently being explored (in the current DFS path).
- **BLACK (2)**: Fully processed (all descendants explored).

### Key Insight:
If during DFS we encounter a **GRAY** node (a node currently in the DFS stack), it means we've found a **back edge** — we've come back to a node we're still exploring. This means there's a cycle.

### Step-by-Step Logic:
1. Build an adjacency list from the edges.
2. Initialize all vertices as WHITE.
3. For each unvisited (WHITE) vertex, start a DFS:
   a. Mark the vertex GRAY.
   b. Visit all neighbors:
      - If neighbor is GRAY → cycle found! Return True.
      - If neighbor is WHITE → recursively DFS on it.
      - If neighbor is BLACK → skip (already fully processed).
   c. After processing all neighbors, mark the vertex BLACK.
4. If no cycle is found after all DFS traversals, return False.

### Why not just use a "visited" boolean?
In directed graphs, a simple visited check doesn't work. Consider: 0 → 1 and 0 → 2 → 1. Node 1 is visited twice but there's no cycle. The three-color scheme distinguishes between "currently exploring" (GRAY) and "fully done" (BLACK).

---

## C. Complete Python Code

```python
import sys
sys.setrecursionlimit(200010)

def detect_cycle(V, edges):
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
    
    color = [0] * V
    
    def dfs(node):
        color[node] = 1
        for neighbor in adj[node]:
            if color[neighbor] == 1:
                return True
            if color[neighbor] == 0:
                if dfs(neighbor):
                    return True
        color[node] = 2
        return False
    
    for node in range(V):
        if color[node] == 0:
            if dfs(node):
                return True
    return False

first_line = input().split()
V = int(first_line[0])
E = int(first_line[1])

edges = []
for i in range(E):
    parts = input().split()
    u = int(parts[0])
    v = int(parts[1])
    edges.append((u, v))

if detect_cycle(V, edges):
    print("YES")
else:
    print("NO")
```

---

## D. Public Test Cases

### Test Case 1
**Input:**
```
3 3
0 1
1 2
2 0
```
**Expected Output:**
```
YES
```
**Explanation:**
- Graph: 0 → 1 → 2 → 0
- DFS from 0: mark 0 GRAY → go to 1 (mark GRAY) → go to 2 (mark GRAY) → try to go to 0 → 0 is GRAY!
- Back edge detected → cycle exists.
- **Output: YES**

### Test Case 2
**Input:**
```
4 3
0 1
1 2
2 3
```
**Expected Output:**
```
NO
```
**Explanation:**
- Graph: 0 → 1 → 2 → 3 (a straight chain)
- DFS from 0: 0(GRAY) → 1(GRAY) → 2(GRAY) → 3(GRAY)
- 3 has no neighbors → mark 3 BLACK → backtrack
- 2 done → BLACK, 1 done → BLACK, 0 done → BLACK.
- No GRAY node encountered → no cycle.
- **Output: NO**

---

## E. Detailed Code Explanation

### Line: `sys.setrecursionlimit(200010)`
- Python's default recursion limit is 1000.
- With up to 10^5 vertices, DFS could recurse deeply.
- We increase the limit to 200010 to avoid `RecursionError`.

### Line: `adj = [[] for _ in range(V)]`
- Creates an adjacency list: a list of V empty lists.
- `adj[u]` will contain all vertices that u has an edge to.
- List comprehension creates V independent lists (not copies).

### Line: `color = [0] * V`
- Creates a list of V zeros, one for each vertex.
- 0 = WHITE = not visited.

### Lines: DFS function
```python
def dfs(node):
    color[node] = 1  # Mark GRAY
    for neighbor in adj[node]:
        if color[neighbor] == 1:  # GRAY = cycle!
            return True
        if color[neighbor] == 0:  # WHITE = explore
            if dfs(neighbor):
                return True
    color[node] = 2  # Mark BLACK (done)
    return False
```
- Mark current node GRAY (entering DFS).
- Check each neighbor:
  - GRAY → cycle detected (return True immediately).
  - WHITE → recurse into it (if recursion finds cycle, propagate True back).
  - BLACK → already fully processed, skip.
- After all neighbors: mark BLACK and return False (no cycle from this node).

### Line: Outer loop
```python
for node in range(V):
    if color[node] == 0:
        if dfs(node):
            return True
```
- Graph may be disconnected, so we must try DFS from every unvisited vertex.
- If any DFS finds a cycle, return True immediately.

---

## F. Python Syntax Explanation

### `sys.setrecursionlimit()`
- Sets the maximum depth of the Python interpreter stack.
- Needed when recursion goes deeper than the default 1000 levels.

### Nested Functions
- `dfs()` is defined inside `detect_cycle()`.
- It can access variables from the outer function (`adj`, `color`) — this is called a **closure**.

### List Comprehension `[[] for _ in range(V)]`
- Creates V independent empty lists.
- `_` is used when we don't need the loop variable.
- Warning: `[[]] * V` would create V references to the SAME list — a common bug!

### Tuple Unpacking `for u, v in edges:`
- If `edges = [(0,1), (1,2)]`, this unpacks each tuple into `u` and `v`.

### `append()`
- Adds an element to the end of a list.

---

## G. Why This Method and Not Another Method?

### Why DFS Coloring?
- O(V + E) time — visits each vertex and edge exactly once.
- Natural fit for cycle detection in directed graphs.
- The three-color scheme precisely identifies back edges.

### Alternative 1: BFS (Kahn's Algorithm / Topological Sort)
- Count in-degrees, process nodes with in-degree 0.
- If all nodes are processed, no cycle. Otherwise, cycle exists.
- Also O(V + E) time.
- **Equally valid** — but DFS coloring is more intuitive for understanding back edges.

### Alternative 2: Simple DFS with Visited + Recursion Stack
- Use two boolean arrays: `visited[]` and `rec_stack[]`.
- `rec_stack[node] = True` when entering DFS, `False` when leaving.
- If a neighbor is in `rec_stack`, there's a cycle.
- **Equivalent** to our color approach (GRAY = in rec_stack, BLACK = visited but not in stack).

### Alternative 3: Union-Find
- Union-Find is typically used for **undirected** graph cycle detection.
- Does NOT work correctly for **directed** graphs.
- **Rejected** because this is a directed graph problem.

### Advantages of Our Approach:
- O(V + E) time — optimal.
- Clear, intuitive coloring scheme.
- Handles disconnected graphs.
- Works for any directed graph.

---

## H. Time and Space Complexity

### Time Complexity: O(V + E)
- Building adjacency list: O(V + E).
- DFS visits each vertex once: O(V).
- DFS traverses each edge once: O(E).
- Total: O(V + E).

### Space Complexity: O(V + E)
- Adjacency list: O(V + E) — V lists, E total entries.
- Color array: O(V).
- Recursion stack: O(V) in the worst case (a long chain).
- Total: O(V + E).

### What do V and E represent?
- V = number of **vertices** (nodes) in the graph.
- E = number of **edges** (connections) in the graph.

---

## I. Faculty Viva Questions and Answers

### Q1: What is a directed graph?
**A:** A graph where each edge has a direction. Edge (u, v) means you can go from u to v but not necessarily from v to u.

### Q2: What is a back edge?
**A:** In DFS, a back edge is an edge from a node to one of its ancestors in the DFS tree. In our coloring scheme, it's an edge to a GRAY node. Back edges indicate cycles.

### Q3: Why do we need three colors instead of two?
**A:** In directed graphs, reaching a visited node doesn't always mean a cycle. Consider edges 0→1 and 2→1. Both reach node 1, but there's no cycle. Three colors distinguish between "still exploring" (GRAY = cycle) and "done exploring" (BLACK = no cycle).

### Q4: What is an adjacency list?
**A:** A way to represent a graph where each vertex has a list of its neighbors. `adj[0] = [1, 2]` means vertex 0 has edges to vertices 1 and 2. It's space-efficient for sparse graphs.

### Q5: What happens if the graph is disconnected?
**A:** The outer loop ensures we start DFS from every unvisited vertex. Even if the graph has multiple disconnected components, we check each one for cycles.

### Q6: Why did you increase the recursion limit?
**A:** Python's default recursion limit is 1000. With up to 100,000 vertices, a long chain graph could cause recursion depth > 1000, crashing with `RecursionError`. We increase it to handle the worst case.

### Q7: Can this algorithm find the actual cycle (not just detect it)?
**A:** Yes, by tracking the parent/path during DFS. When a back edge is found, we can trace back from the current node to the GRAY node to reconstruct the cycle.

### Q8: What is topological sort and how is it related?
**A:** Topological sort is an ordering of vertices where every edge goes from earlier to later in the ordering. It's possible only if the graph has NO cycle. So detecting a cycle is equivalent to checking if topological sort is possible.

### Q9: Could you use BFS instead of DFS?
**A:** Yes, Kahn's algorithm uses BFS for cycle detection. It repeatedly removes nodes with in-degree 0. If all nodes are removed, no cycle. Otherwise, the remaining nodes form a cycle. Both approaches are O(V + E).

### Q10: What is the difference between cycle detection in directed vs undirected graphs?
**A:** In undirected graphs, simply checking if we visit an already-visited node (that isn't the parent) is enough. In directed graphs, we need the three-color scheme because reaching a visited node doesn't always mean a cycle.

### Q11: What is DFS?
**A:** Depth-First Search is a graph traversal algorithm that explores as deep as possible along each branch before backtracking. It uses a stack (or recursion) and visits nodes in a depth-first manner.

### Q12: What would happen without `sys.setrecursionlimit`?
**A:** For graphs with more than ~1000 vertices in a chain, Python would raise a `RecursionError: maximum recursion depth exceeded`. The program would crash instead of giving the correct output.

---

## J. VS Code Execution

### Terminal Example — Test Case 1:
```
PS C:\...\CAS_Assessment> python Q6_Directed_Cycle.py
3 3
0 1
1 2
2 0
YES
```

### Terminal Example — Test Case 2:
```
PS C:\...\CAS_Assessment> python Q6_Directed_Cycle.py
4 3
0 1
1 2
2 3
NO
```

---

## K. Quick Revision

| Item | Details |
|------|---------|
| **Algorithm** | DFS with White-Gray-Black Coloring |
| **Data Structure** | Adjacency list + Color array |
| **Core Logic** | 1. Color nodes WHITE initially. 2. DFS: mark GRAY on enter. 3. If neighbor is GRAY → cycle. 4. Mark BLACK on exit. 5. Try all components. |
| **Memory Trick** | "White=unvisited, Gray=exploring, Black=done. Gray meets Gray = Cycle!" |
| **One Sentence** | Use DFS with three-color marking to detect back edges (GRAY to GRAY connections) which indicate cycles in the directed graph. |
