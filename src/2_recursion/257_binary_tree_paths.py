"""
257. Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- -100 <= Node.val <= 100
"""

from typing import Optional, List
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def list_to_tree(arr):
    """Helper function to convert list representation to binary tree"""
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    
    while queue and i < len(arr):
        node = queue.pop(0)
        
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Your code here
        pass


@pytest.mark.parametrize(
    "root_list, expected",
    [
        ([1, 2, 3, None, 5], ["1->2->5", "1->3"]),
        ([1], ["1"]),
        ([1, 2, 3, 4, 5], ["1->2->4", "1->2->5", "1->3"]),
        ([1, 2, 3, 4, None, None, 5], ["1->2->4", "1->3->5"]),
    ],
)
def test_binary_tree_paths(root_list, expected):
    """Test cases for binary tree paths"""
    sol = Solution()
    root = list_to_tree(root_list)
    result = sol.binaryTreePaths(root)
    # Sort both lists since order doesn't matter
    assert sorted(result) == sorted(expected), f"Expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

