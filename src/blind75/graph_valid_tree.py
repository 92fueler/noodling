"""
You are given n nodes labeled from 0 to n - 1 and a list of undirected edges edges,
where each edge is a pair [ai, bi] indicating an undirected edge between nodes ai and bi.

Return true if these edges form a valid tree, and false otherwise.

Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
"""

from typing import List
from collections import defaultdict


from collections import deque


class Solution:
    def validTree_bfs(self, n: int, edges: List[List[int]]) -> bool:
        if n != len(edges) + 1:
            return False

        # build adjacent map
        adj_map = {i: [] for i in range(n)}  # n nodes labeled from 0 to n - 1

        for a, b in edges:
            adj_map[a].append(b)
            adj_map[b].append(a)

        queue = deque([0])
        visited = set([0])

        while queue:
            node = queue.popleft()
            for neighbor in adj_map[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return len(visited) == n

    def valid_tree_iterative_dfs(self, n: int, edges: List[List[int]]) -> bool:
        # Necessary condition for a tree
        if len(edges) != n - 1:
            return False

        # Build adjacency list
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set([0])
        stack = [(0, -1)]  # (current_node, parent)

        while stack:
            node, parent = stack.pop()

            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False  # cycle found
                visited.add(nei)
                stack.append((nei, node))

        # Must be connected
        return len(visited) == n

    def valid_tree_recursive_dfs(self, n: int, edges: List[List[int]]) -> bool:
        # Necessary condition for a tree
        if len(edges) != n - 1:
            return False

        # Build adjacency list
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node: int, parent: int) -> bool:
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False  # cycle found
                if not dfs(nei, node):
                    return False
            return True

        # Start DFS from node 0
        dfs(0, -1)
        # Must be connected
        return len(visited) == n
