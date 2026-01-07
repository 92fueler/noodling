"""
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- -100 <= Node.val <= 100
"""

from typing import Optional
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Your code here
        pass


@pytest.mark.parametrize(
    "root_list, expected",
    [
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, None, 3], False),
        ([1], True),
        ([1, 2, 2], True),
        ([1, 2, 3], False),
        ([1, 2, 2, 2, None, 2], False),
    ],
)
def test_is_symmetric(root_list, expected):
    """Test cases for symmetric tree"""
    sol = Solution()
    root = list_to_tree(root_list)
    result = sol.isSymmetric(root)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

