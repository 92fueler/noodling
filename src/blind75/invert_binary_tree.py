"""
Given the root of a binary tree, invert the tree and return the root
"""

from typing import Optional

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node(val={self.val}, left={self.left}, right={self.right})"


class Solution:
    def invert_bt_dfs(self, root: Optional[Node]):
        if not root:
            return

        root.left, root.right = root.right, root.left

        self.invert_bt(root.left)
        self.invert_bt(root.right)

        return root

    def invert_bt_bfs(self, root: Optional[Node]):
        if not root:
            return root

        queue = deque([root])

        while queue:
            curr_size = len(queue)

            for _ in range(curr_size):
                node = queue.popleft()
                node.left, node.right = node.right, node.left

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root

    def invert_bt_iterative_dfs(self, root: Optional[Node]):
        if not root:
            return root

        stack = [root]

        while stack:
            node = stack.pop()

            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root


root = Node(
    2,
    left=Node(1, left=None, right=Node(10, left=None, right=None)),
    right=Node(
        3, left=Node(21, left=None, right=None), right=Node(100, left=None, right=None)
    ),
)

print(root)
s = Solution()
result = s.invert_bt_iterative_dfs(root)
print(result)
