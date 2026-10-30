# Q8: Network Shortest Path (Dijkstra's Algorithm)
# Algorithm: Dijkstra's with Min Heap (Priority Queue)
# Time Complexity: O((V + E) log V) | Space Complexity: O(V + E)

import heapq

def dijkstra(V, adj, source):
    """
    Compute shortest distances from source to all vertices
    using Dijkstra's algorithm with a min heap.
    Returns a list of distances. -1 for unreachable vertices.
    """
    # Initialize distances to infinity
    INF = float('inf')
    dist = [INF] * V
    dist[source] = 0
    
    # Min heap: (distance, vertex)
    # Start with the source vertex
    heap = [(0, source)]
    
    while heap:
        # Extract the vertex with the smallest distance
        current_dist, u = heapq.heappop(heap)
        
        # Skip if we already found a shorter path to u
        if current_dist > dist[u]:
            continue
        
        # Explore all neighbors of u
        for v, weight in adj[u]:
            new_dist = dist[u] + weight
            
            # If we found a shorter path to v, update it
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
    
    # Replace infinity with -1 for unreachable vertices
    for i in range(V):
        if dist[i] == INF:
            dist[i] = -1
    
    return dist


# ---- Main Program ----
# Read V (vertices), E (edges), S (source)
first_line = input().split()
V = int(first_line[0])
E = int(first_line[1])
S = int(first_line[2])

# Build adjacency list
adj = [[] for _ in range(V)]
for i in range(E):
    parts = input().split()
    u = int(parts[0])
    v = int(parts[1])
    w = int(parts[2])
    adj[u].append((v, w))

# Run Dijkstra and print distances
distances = dijkstra(V, adj, S)
print(' '.join(map(str, distances)))
