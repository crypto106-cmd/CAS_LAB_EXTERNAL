# Q6: Detect a Cycle in a Directed Graph
# Algorithm: DFS with coloring (White-Gray-Black)
# Time Complexity: O(V + E) | Space Complexity: O(V + E)

import sys
sys.setrecursionlimit(200010)

def detect_cycle(V, edges):
    """
    Detect if a directed graph contains a cycle.
    Uses DFS with three colors:
      WHITE (0) = not visited
      GRAY (1)  = currently in the DFS stack (being explored)
      BLACK (2) = fully processed
    A cycle exists if we encounter a GRAY node during DFS.
    """
    # Build adjacency list
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
    
    # Color array: 0 = WHITE, 1 = GRAY, 2 = BLACK
    color = [0] * V
    
    def dfs(node):
        """
        Perform DFS from the given node.
        Returns True if a cycle is detected.
        """
        # Mark current node as GRAY (being explored)
        color[node] = 1
        
        # Visit all neighbors
        for neighbor in adj[node]:
            if color[neighbor] == 1:
                # Found a GRAY neighbor = back edge = cycle!
                return True
            if color[neighbor] == 0:
                # WHITE neighbor: explore it
                if dfs(neighbor):
                    return True
        
        # All neighbors processed: mark as BLACK
        color[node] = 2
        return False
    
    # Run DFS from every unvisited node
    # (graph may be disconnected)
    for node in range(V):
        if color[node] == 0:
            if dfs(node):
                return True
    
    return False


# ---- Main Program ----
# Read V (vertices) and E (edges)
first_line = input().split()
V = int(first_line[0])
E = int(first_line[1])

# Read all edges
edges = []
for i in range(E):
    parts = input().split()
    u = int(parts[0])
    v = int(parts[1])
    edges.append((u, v))

# Detect cycle and print result
if detect_cycle(V, edges):
    print("YES")
else:
    print("NO")
