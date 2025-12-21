"""
Graph Basics & Common Patterns

1. representation - adjacency list, adjacency matrix, edge list
2. create & build - from edges, from adjacency, weighted/unweighted
3. traversal - DFS (recursive/iterative), BFS
4. search & find - path finding, connected components, cycle detection
5. algorithms - shortest path (BFS, Dijkstra), topological sort
6. patterns - islands, connected components, bipartite, union-find
"""

# ============================================================================
# 1. REPRESENTATION
# ============================================================================

# Adjacency List (most common for sparse graphs)
# graph[node] = [neighbor1, neighbor2, ...]
graph_adj_list = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}

# Using defaultdict for easier graph building
from collections import defaultdict

graph = defaultdict(list)

# Adjacency Matrix (for dense graphs or fixed-size graphs)
# graph[i][j] = 1 if edge exists, 0 otherwise
graph_adj_matrix = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]

# Weighted graph (adjacency list with weights)
# graph[node] = [(neighbor, weight), ...]
weighted_graph = {
    0: [(1, 5), (2, 3)],
    1: [(0, 5), (3, 2)],
    2: [(0, 3), (3, 1)],
    3: [(1, 2), (2, 1)],
}

# Edge list
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]

# ============================================================================
# 2. CREATE & BUILD
# ============================================================================


# Build undirected graph from edge list
def build_graph(edges, directed=False):
    """Build graph from list of edges"""
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph


# Example: edges = [(0, 1), (1, 2), (2, 3)]
graph = build_graph([(0, 1), (1, 2), (2, 3)])


# Build weighted graph from edge list
def build_weighted_graph(edges, directed=False):
    """Build weighted graph from list of (u, v, weight) tuples"""
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        if not directed:
            graph[v].append((u, w))
    return graph


# Example
weighted_edges = [(0, 1, 5), (1, 2, 3), (2, 3, 1)]
weighted_g = build_weighted_graph(weighted_edges)


# Build from adjacency matrix
def matrix_to_adj_list(matrix):
    """Convert adjacency matrix to adjacency list"""
    n = len(matrix)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                graph[i].append(j)
    return graph


# ============================================================================
# 3. TRAVERSAL - DFS
# ============================================================================


# DFS Recursive
def dfs_recursive(graph, start, visited=None, result=None):
    """DFS traversal, returns list of visited nodes"""
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(start)
    result.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)

    return result


# DFS Iterative (using stack)
def dfs_iterative(graph, start):
    """DFS traversal using stack"""
    visited = set()
    result = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            # Push neighbors in reverse order to maintain left-to-right
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


# DFS with path tracking
def dfs_with_path(graph, start, target):
    """DFS to find path from start to target"""

    def dfs(node, path):
        if node == target:
            return path + [node]

        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                result = dfs(neighbor, path + [node])
                if result:
                    return result
        return None

    visited = set()
    return dfs(start, [])


# ============================================================================
# 4. TRAVERSAL - BFS
# ============================================================================

# BFS (using queue)
from collections import deque


def bfs(graph, start):
    """BFS traversal, returns list of visited nodes"""
    visited = set()
    result = []
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


# BFS with path finding (shortest path in unweighted graph)
def bfs_shortest_path(graph, start, target):
    """Find shortest path using BFS"""
    if start == target:
        return [start]

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        node, path = queue.popleft()

        for neighbor in graph[node]:
            if neighbor == target:
                return path + [neighbor]

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # No path exists


# BFS with distance tracking
def bfs_with_distance(graph, start):
    """BFS that returns distances from start node"""
    distances = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in distances:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    return distances


# ============================================================================
# 5. SEARCH & FIND
# ============================================================================


# Connected Components (undirected graph)
def connected_components(graph):
    """Find all connected components"""
    visited = set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)

    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)

    return components


# Check if two nodes are connected
def is_connected(graph, start, target):
    """Check if path exists from start to target"""
    visited = set()

    def dfs(node):
        if node == target:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False

    return dfs(start)


# Cycle Detection (undirected graph)
def has_cycle_undirected(graph):
    """Detect cycle in undirected graph using DFS"""
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True  # Back edge found
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False


# Cycle Detection (directed graph)
def has_cycle_directed(graph):
    """Detect cycle in directed graph using DFS with colors"""
    # Colors: 0 (white/unvisited), 1 (gray/visiting), 2 (black/visited)
    color = defaultdict(int)

    def dfs(node):
        if color[node] == 1:  # Gray - back edge found
            return True
        if color[node] == 2:  # Black - already processed
            return False

        color[node] = 1  # Mark as visiting
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        color[node] = 2  # Mark as visited
        return False

    for node in graph:
        if color[node] == 0:
            if dfs(node):
                return True
    return False


# Find all paths between two nodes
def find_all_paths(graph, start, target):
    """Find all paths from start to target"""
    paths = []

    def dfs(node, path):
        if node == target:
            paths.append(path + [node])
            return

        for neighbor in graph[node]:
            if neighbor not in path:  # Avoid cycles
                dfs(neighbor, path + [node])

    dfs(start, [])
    return paths


# ============================================================================
# 6. ALGORITHMS - SHORTEST PATH
# ============================================================================


# Shortest path in unweighted graph (BFS)
def shortest_path_bfs(graph, start, target):
    """Shortest path in unweighted graph"""
    return bfs_shortest_path(graph, start, target)


# Dijkstra's Algorithm (weighted graph, non-negative weights)
import heapq


def dijkstra(graph, start):
    """Dijkstra's algorithm - returns shortest distances from start"""
    # graph: dict[node] = [(neighbor, weight), ...]
    distances = {start: 0}
    pq = [(0, start)]  # (distance, node)
    visited = set()

    while pq:
        dist, node = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in distances or distances[neighbor] > dist + weight:
                distances[neighbor] = dist + weight
                heapq.heappush(pq, (distances[neighbor], neighbor))

    return distances


# Dijkstra with path reconstruction
def dijkstra_with_path(graph, start, target):
    """Dijkstra's with path reconstruction"""
    distances = {start: 0}
    parents = {}
    pq = [(0, start)]
    visited = set()

    while pq:
        dist, node = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == target:
            break

        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if neighbor not in distances or distances[neighbor] > new_dist:
                distances[neighbor] = new_dist
                parents[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))

    # Reconstruct path
    if target not in parents and start != target:
        return None

    path = []
    node = target
    while node is not None:
        path.append(node)
        node = parents.get(node)

    return list(reversed(path))


# ============================================================================
# 7. ALGORITHMS - TOPOLOGICAL SORT
# ============================================================================


# Topological Sort (for DAG - Directed Acyclic Graph)
def topological_sort(graph):
    """Topological sort using DFS"""
    visited = set()
    result = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        result.append(node)  # Add to result after processing all neighbors

    for node in graph:
        if node not in visited:
            dfs(node)

    return list(reversed(result))  # Reverse to get correct order


# Topological Sort (Kahn's Algorithm - BFS)
def topological_sort_kahn(graph):
    """Topological sort using Kahn's algorithm (BFS)"""
    # Calculate in-degrees
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Add nodes with in-degree 0 to queue
    queue = deque([node for node in graph if in_degree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if all nodes were processed (cycle detection)
    if len(result) != len(graph):
        return None  # Cycle exists

    return result


# ============================================================================
# 8. PATTERNS - ISLANDS / GRID PROBLEMS
# ============================================================================


# Number of Islands (2D grid)
def num_islands(grid):
    """Count number of islands in 2D grid (1=land, 0=water)"""
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0

    def dfs(r, c):
        if (
            r < 0
            or r >= rows
            or c < 0
            or c >= cols
            or (r, c) in visited
            or grid[r][c] == "0"
        ):
            return

        visited.add((r, c))
        # Check all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                dfs(r, c)
                count += 1

    return count


# ============================================================================
# 9. PATTERNS - BIPARTITE CHECK
# ============================================================================


# Check if graph is bipartite
def is_bipartite(graph):
    """Check if graph can be colored with 2 colors (bipartite)"""
    color = {}  # 0 or 1 for each node

    def dfs(node, c):
        if node in color:
            return color[node] == c
        color[node] = c
        for neighbor in graph[node]:
            if not dfs(neighbor, 1 - c):
                return False
        return True

    for node in graph:
        if node not in color:
            if not dfs(node, 0):
                return False
    return True


# Bipartite using BFS
def is_bipartite_bfs(graph):
    """Check bipartite using BFS"""
    color = {}

    for node in graph:
        if node not in color:
            queue = deque([node])
            color[node] = 0

            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[curr]
                        queue.append(neighbor)
                    elif color[neighbor] == color[curr]:
                        return False

    return True


# ============================================================================
# 10. PATTERNS - UNION-FIND
# ============================================================================


# Union-Find (Disjoint Set Union)
class UnionFind:
    """Union-Find data structure for connected components"""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """Find root with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union two sets by rank"""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same set

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

    def connected(self, x, y):
        """Check if two elements are in same set"""
        return self.find(x) == self.find(y)


# Number of connected components using Union-Find
def num_components_union_find(n, edges):
    """Count connected components using Union-Find"""
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)

    # Count distinct roots
    roots = set()
    for i in range(n):
        roots.add(uf.find(i))
    return len(roots)


# ============================================================================
# 11. UTILITY FUNCTIONS
# ============================================================================


# Count nodes and edges
def graph_stats(graph):
    """Get number of nodes and edges"""
    nodes = len(graph)
    edges = sum(len(neighbors) for neighbors in graph.values())
    # For undirected graph, divide by 2
    return nodes, edges // 2 if all(
        (v in graph.get(u, []) for u in graph for v in graph[u])
    ) else edges


# Get all nodes
def get_all_nodes(graph):
    """Get set of all nodes in graph"""
    nodes = set(graph.keys())
    for neighbors in graph.values():
        nodes.update(neighbors)
    return nodes


# Check if graph is empty
def is_empty_graph(graph):
    """Check if graph is empty"""
    return len(graph) == 0


# Clone graph
def clone_graph(graph):
    """Deep copy of graph"""
    from copy import deepcopy

    return deepcopy(graph)


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Create graph
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (4, 5)]
    graph = build_graph(edges)

    # Traversal
    print("DFS:", dfs_recursive(graph, 0))
    print("BFS:", bfs(graph, 0))

    # Connected components
    print("Components:", connected_components(graph))

    # Shortest path
    print("Shortest path 0->3:", bfs_shortest_path(graph, 0, 3))

    # Cycle detection
    print("Has cycle:", has_cycle_undirected(graph))

    # Dijkstra example
    weighted_edges = [(0, 1, 4), (0, 2, 2), (1, 3, 5), (2, 3, 1)]
    w_graph = build_weighted_graph(weighted_edges)
    print("Dijkstra distances:", dijkstra(w_graph, 0))
