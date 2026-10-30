# Q8: Network Shortest Path — Complete Explanation

---

## A. Understanding the Problem

### What is the question asking?
Given a **directed weighted graph** with non-negative edge weights (latencies) and a **source vertex S**, compute the **shortest distance** from S to every other vertex.

### What is a weighted graph?
A graph where each edge has a numerical weight (cost/distance/latency). Edge (U, V, W) means going from U to V costs W.

### What input do we receive?
- First line: V (vertices), E (edges), S (source vertex).
- Next E lines: U V W (edge from U to V with weight W).

### What output do we produce?
- V distances in vertex order (0, 1, 2, ..., V-1), separated by spaces.
- Print -1 for vertices unreachable from S.

### Small Example
```
4 vertices, source = 0
Edges: 0→1 (weight 4), 0→2 (weight 2), 2→1 (weight 1), 1→3 (weight 2), 2→3 (weight 5)

Shortest paths from 0:
  0 → 0: distance 0
  0 → 1: 0→2→1 = 2+1 = 3 (not direct 0→1 = 4)
  0 → 2: 0→2 = 2
  0 → 3: 0→2→1→3 = 2+1+2 = 5 (not 0→2→3 = 2+5 = 7)
Output: 0 3 2 5
```

---

## B. Algorithm and Approach

### Approach: Dijkstra's Algorithm with Min Heap

Dijkstra's algorithm is a **greedy** algorithm that finds the shortest path from a source to all vertices in a graph with non-negative weights.

### Step-by-Step Logic:
1. Set distance to source = 0, all others = infinity (∞).
2. Use a **min heap** (priority queue) initialized with (0, source).
3. Repeat until heap is empty:
   a. Pop the vertex with the smallest distance.
   b. If this distance is greater than the known shortest distance, skip it (stale entry).
   c. For each neighbor, calculate `new_dist = dist[u] + weight`.
   d. If `new_dist < dist[v]`, update `dist[v]` and push `(new_dist, v)` to the heap.
4. After the algorithm finishes, replace any remaining infinity with -1.

### Why Dijkstra's?
- The PDF explicitly says "Expected O((V + E) log V) using Dijkstra."
- Dijkstra's is the standard algorithm for shortest paths with non-negative weights.
- The min heap ensures we always process the closest unvisited vertex first.

### Why does the greedy approach work?
- Because all weights are non-negative, once we pop a vertex from the heap with distance d, no future path can reach it with a shorter distance. So we can "finalize" it.

---

## C. Complete Python Code

```python
import heapq

def dijkstra(V, adj, source):
    INF = float('inf')
    dist = [INF] * V
    dist[source] = 0
    heap = [(0, source)]
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > dist[u]:
            continue
        for v, weight in adj[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
    
    for i in range(V):
        if dist[i] == INF:
            dist[i] = -1
    return dist

first_line = input().split()
V = int(first_line[0])
E = int(first_line[1])
S = int(first_line[2])

adj = [[] for _ in range(V)]
for i in range(E):
    parts = input().split()
    u = int(parts[0])
    v = int(parts[1])
    w = int(parts[2])
    adj[u].append((v, w))

distances = dijkstra(V, adj, S)
print(' '.join(map(str, distances)))
```

---

## D. Public Test Cases

### Test Case 1
**Input:**
```
4 5 0
0 1 4
0 2 2
2 1 1
1 3 2
2 3 5
```
**Expected Output:**
```
0 3 2 5
```
**Explanation:**
- Start: dist = [0, ∞, ∞, ∞], heap = [(0, 0)]
- Pop (0, 0): process edges 0→1(4), 0→2(2)
  - dist[1] = 4, push (4, 1)
  - dist[2] = 2, push (2, 2)
  - dist = [0, 4, 2, ∞]
- Pop (2, 2): process edges 2→1(1), 2→3(5)
  - new_dist to 1 = 2+1 = 3 < 4 → update! dist[1] = 3, push (3, 1)
  - new_dist to 3 = 2+5 = 7 → dist[3] = 7, push (7, 3)
  - dist = [0, 3, 2, 7]
- Pop (3, 1): process edge 1→3(2)
  - new_dist to 3 = 3+2 = 5 < 7 → update! dist[3] = 5, push (5, 3)
  - dist = [0, 3, 2, 5]
- Pop (4, 1): current_dist 4 > dist[1]=3 → skip (stale)
- Pop (5, 3): no outgoing edges. Done.
- Pop (7, 3): stale. Done.
- Output: **0 3 2 5** ✓

### Test Case 2
**Input:**
```
5 4 2
2 0 7
2 1 2
1 3 3
3 4 1
```
**Expected Output:**
```
7 2 0 5 6
```
**Explanation:**
- Source = 2. dist = [∞, ∞, 0, ∞, ∞]
- Pop (0, 2): edges 2→0(7), 2→1(2)
  - dist[0] = 7, dist[1] = 2
- Pop (2, 1): edge 1→3(3)
  - dist[3] = 2+3 = 5
- Pop (5, 3): edge 3→4(1)
  - dist[4] = 5+1 = 6
- Pop (7, 0): no outgoing edges.
- Output: **7 2 0 5 6** ✓

---

## E. Detailed Code Explanation

### Line: `INF = float('inf')`
- Creates a positive infinity value.
- Used to represent "unreachable" distances initially.
- Any number compared to infinity is smaller.

### Line: `dist = [INF] * V`
- All vertices start with infinite distance (unreachable).
- As we discover shorter paths, we update these values.

### Line: `dist[source] = 0`
- The distance from the source to itself is 0.

### Line: `heap = [(0, source)]`
- Initialize the min heap with the source vertex at distance 0.
- `heapq` in Python is a min heap — the smallest element is popped first.
- Tuples are compared element-by-element, so (distance, vertex) is sorted by distance first.

### Line: `current_dist, u = heapq.heappop(heap)`
- Pops the element with the smallest distance from the heap.
- `current_dist` = distance at which we reached u.
- `u` = the vertex.

### Line: `if current_dist > dist[u]: continue`
- **Lazy deletion**: Since we push new entries to the heap without removing old ones, there may be stale (outdated) entries.
- If we already know a shorter distance to u, skip this entry.
- This is crucial for correctness and performance.

### Line: `new_dist = dist[u] + weight`
- Calculate the distance to neighbor v through u.
- This is the "relaxation" step.

### Line: `if new_dist < dist[v]:`
- Only update if we found a strictly shorter path.
- This prevents unnecessary heap pushes.

---

## F. Python Syntax Explanation

### `heapq` Module
- `heapq.heappush(heap, item)`: Push item onto the heap, maintaining heap property. O(log n).
- `heapq.heappop(heap)`: Pop and return the smallest item. O(log n).
- Python's heapq is a **min heap** — the smallest element is at the top.

### `float('inf')`
- Creates positive infinity.
- `float('inf') > 10**18` → True.
- `float('inf') + 5` → still `inf`.
- Used when we need a value that's guaranteed to be larger than any real distance.

### Tuple Unpacking
- `current_dist, u = heapq.heappop(heap)` unpacks the tuple `(distance, vertex)` into two variables.
- `for v, weight in adj[u]` unpacks each `(neighbor, weight)` tuple.

### `continue`
- Skips the rest of the current loop iteration and moves to the next one.
- Used here to skip stale heap entries.

---

## G. Why This Method and Not Another Method?

### Why Dijkstra's?
- Standard algorithm for single-source shortest paths with non-negative weights.
- O((V + E) log V) with a min heap — matches the expected complexity.
- Greedy approach is intuitive and efficient.

### Alternative 1: Bellman-Ford
- Works with negative weights too.
- Time: O(V × E) — much slower than Dijkstra.
- **Rejected** because all weights are non-negative, so Dijkstra is sufficient and faster.

### Alternative 2: Floyd-Warshall
- Finds shortest paths between ALL pairs of vertices.
- Time: O(V³) — much slower for single-source.
- **Rejected** because we only need shortest paths from one source.

### Alternative 3: BFS (unweighted version)
- Only works when all weights are equal (or 1).
- **Rejected** because we have different weights.

### Alternative 4: Dijkstra with adjacency matrix
- Would make neighbor iteration O(V) instead of O(degree).
- Total: O(V²) — could be faster for dense graphs but doesn't use a heap.
- **Rejected** because the heap-based approach is O((V+E) log V), which is better for sparse graphs.

### Lazy Deletion vs Decrease-Key
- Some implementations use a "decrease-key" operation to update heap entries.
- Python's heapq doesn't support decrease-key.
- We use "lazy deletion" instead: push new entries and skip stale ones when popped.
- Both approaches have the same asymptotic complexity.

---

## H. Time and Space Complexity

### Time Complexity: O((V + E) log V)
- Each vertex is popped from the heap at most once with its final shortest distance: O(V log V).
- Each edge is relaxed at most once, potentially pushing to the heap: O(E log V).
- Total: O((V + E) log V).

### Space Complexity: O(V + E)
- Adjacency list: O(V + E).
- Distance array: O(V).
- Heap: O(V + E) in the worst case (lazy deletion may have multiple entries).
- Total: O(V + E).

### What do V, E mean?
- V = number of vertices (nodes/routers in the network).
- E = number of edges (connections/links).
- log V comes from the heap operations.

---

## I. Faculty Viva Questions and Answers

### Q1: What is Dijkstra's algorithm?
**A:** Dijkstra's is a greedy algorithm that finds the shortest path from a single source to all vertices in a graph with non-negative edge weights. It uses a priority queue to always process the closest unfinished vertex next.

### Q2: Why doesn't Dijkstra work with negative weights?
**A:** Dijkstra assumes that once a vertex is finalized (popped from the heap), no shorter path to it can be found. Negative weights can violate this assumption — a longer path through a negative edge could end up shorter.

### Q3: What is a priority queue?
**A:** A data structure where elements are removed in order of priority (smallest first for a min heap, largest first for a max heap). In Dijkstra, the priority is the tentative shortest distance.

### Q4: What is the "lazy deletion" approach?
**A:** Instead of updating existing heap entries when a shorter path is found, we push a new entry with the updated distance. When popping, we check if the distance is stale (greater than known shortest) and skip it. This avoids the complexity of a decrease-key operation.

### Q5: What is edge relaxation?
**A:** Checking if going through vertex u to reach vertex v gives a shorter path than the current known distance to v. If `dist[u] + weight < dist[v]`, we "relax" the edge by updating dist[v].

### Q6: What is an adjacency list?
**A:** A graph representation where each vertex stores a list of its neighbors and edge weights. `adj[0] = [(1, 4), (2, 2)]` means vertex 0 connects to vertex 1 (weight 4) and vertex 2 (weight 2).

### Q7: Why use a heap instead of a simple array?
**A:** Finding the minimum in an array is O(V). With a heap, it's O(log V). Over V iterations, a heap saves O(V²) vs O(V log V) total time.

### Q8: What does -1 in the output mean?
**A:** It means the vertex is unreachable from the source. There's no path from S to that vertex in the graph.

### Q9: Can Dijkstra handle undirected graphs?
**A:** Yes! For undirected graphs, add each edge in both directions: `adj[u].append((v, w))` and `adj[v].append((u, w))`.

### Q10: What is the difference between Dijkstra and BFS?
**A:** BFS finds shortest paths in unweighted graphs (or when all weights are 1). Dijkstra handles different weights. BFS uses a queue (FIFO), Dijkstra uses a priority queue (min heap).

### Q11: What real-world problems use Dijkstra's algorithm?
**A:** GPS navigation (shortest route), network routing (fastest data path), airline scheduling (cheapest flights), and logistics/supply chain optimization.

### Q12: Why is the source distance set to 0?
**A:** The distance from any vertex to itself is 0. This is the base case of the algorithm — we start from the source with zero cost.

---

## J. VS Code Execution

### Terminal Example — Test Case 1:
```
PS C:\...\CAS_Assessment> python Q8_Network_Shortest_Path.py
4 5 0
0 1 4
0 2 2
2 1 1
1 3 2
2 3 5
0 3 2 5
```

### Terminal Example — Test Case 2:
```
PS C:\...\CAS_Assessment> python Q8_Network_Shortest_Path.py
5 4 2
2 0 7
2 1 2
1 3 3
3 4 1
7 2 0 5 6
```

---

## K. Quick Revision

| Item | Details |
|------|---------|
| **Algorithm** | Dijkstra's Algorithm with Min Heap |
| **Data Structure** | Adjacency List + Min Heap (heapq) + Distance Array |
| **Core Logic** | 1. Init all distances to ∞, source to 0. 2. Pop min from heap. 3. Relax all edges from popped vertex. 4. Push updated distances. 5. Repeat until heap empty. |
| **Memory Trick** | "Pop closest, relax neighbors, push updates — greedy always works with non-negative weights" |
| **One Sentence** | Use Dijkstra's greedy algorithm with a min heap to always process the closest vertex first, relaxing edges to find shortest paths from the source to all vertices. |
