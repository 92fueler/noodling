"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

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


class solution:
    def same_tree_recursion(self, p: Optional[Node], q: Optional[Node]):
        if not p and not q:
            return True

        if (not p and q) or (p and not q):
            return False

        if p.val != q.val:
            return False

        return self.same_tree_recursion(p.left, q.left) and self.same_tree_recursion(
            p.right, q.right
        )

    def same_tree_bfs(self, p: Optional[Node], q: Optional[Node]):
        if not p and not q:
            return True

        if (not p and q) or (p and not q):
            return False

        queue = deque([(p, q)])

        while queue:
            p_node, q_node = queue.popleft()

            if (not p_node and q_node) or (p_node and not q_node):
                return False

            if p_node and q_node and p_node.val != q_node.val:
                return False

            if p_node and q_node:
                queue.append((p_node.left, q_node.left))
                queue.append((p_node.right, q_node.right))

        return True


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------
import pytest


@pytest.fixture
def sol():
    return solution()


def _tree(*vals):
    """Build a complete binary tree from a level-order list (None = missing node)."""
    if not vals or vals[0] is None:
        return None
    nodes = [Node(v) if v is not None else None for v in vals]
    for i, node in enumerate(nodes):
        if node is None:
            continue
        left_i, right_i = 2 * i + 1, 2 * i + 2
        if left_i < len(nodes):
            node.left = nodes[left_i]
        if right_i < len(nodes):
            node.right = nodes[right_i]
    return nodes[0]


# --- same_tree_recursion ---


def test_recursion_both_none(sol):
    assert sol.same_tree_recursion(None, None) is True


def test_recursion_one_none(sol):
    assert sol.same_tree_recursion(_tree(1), None) is False
    assert sol.same_tree_recursion(None, _tree(1)) is False


def test_recursion_single_node_equal(sol):
    assert sol.same_tree_recursion(_tree(42), _tree(42)) is True


def test_recursion_single_node_different(sol):
    assert sol.same_tree_recursion(_tree(1), _tree(2)) is False


def test_recursion_identical_trees(sol):
    #     1
    #    / \
    #   2   3
    assert sol.same_tree_recursion(_tree(1, 2, 3), _tree(1, 2, 3)) is True


def test_recursion_different_values(sol):
    assert sol.same_tree_recursion(_tree(1, 2, 3), _tree(1, 2, 4)) is False


def test_recursion_different_structure(sol):
    # [1, 2] vs [1, None, 2]  — same values, different shapes
    p = Node(1, left=Node(2))
    q = Node(1, right=Node(2))
    assert sol.same_tree_recursion(p, q) is False


def test_recursion_deeper_identical(sol):
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    p = _tree(1, 2, 3, 4, 5)
    q = _tree(1, 2, 3, 4, 5)
    assert sol.same_tree_recursion(p, q) is True


def test_recursion_deeper_different(sol):
    p = _tree(1, 2, 3, 4, 5)
    q = _tree(1, 2, 3, 4, 6)
    assert sol.same_tree_recursion(p, q) is False


# --- same_tree_bfs ---


def test_bfs_both_none(sol):
    assert sol.same_tree_bfs(None, None) is True


def test_bfs_one_none(sol):
    assert sol.same_tree_bfs(_tree(1), None) is False
    assert sol.same_tree_bfs(None, _tree(1)) is False


def test_bfs_single_node_equal(sol):
    assert sol.same_tree_bfs(_tree(42), _tree(42)) is True


def test_bfs_single_node_different(sol):
    assert sol.same_tree_bfs(_tree(1), _tree(2)) is False


def test_bfs_identical_trees(sol):
    assert sol.same_tree_bfs(_tree(1, 2, 3), _tree(1, 2, 3)) is True


def test_bfs_different_values(sol):
    assert sol.same_tree_bfs(_tree(1, 2, 3), _tree(1, 2, 4)) is False


def test_bfs_different_structure(sol):
    p = Node(1, left=Node(2))
    q = Node(1, right=Node(2))
    assert sol.same_tree_bfs(p, q) is False


def test_bfs_deeper_identical(sol):
    p = _tree(1, 2, 3, 4, 5)
    q = _tree(1, 2, 3, 4, 5)
    assert sol.same_tree_bfs(p, q) is True


def test_bfs_deeper_different(sol):
    p = _tree(1, 2, 3, 4, 5)
    q = _tree(1, 2, 3, 4, 6)
    assert sol.same_tree_bfs(p, q) is False
