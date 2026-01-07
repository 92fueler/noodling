"""
112. Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a
root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The path is 5 -> 4 -> 11 -> 2, which gives 22.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths: 1 -> 2 (sum = 3) and 1 -> 3 (sum = 4).
There is no path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false

Constraints:
- The number of nodes in the tree is in the range [0, 5000].
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Your code here
        pass


@pytest.mark.parametrize(
    "root_list, targetSum, expected",
    [
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),
        ([1, 2, 3], 5, False),
        ([], 0, False),
        ([1, 2], 1, False),
        ([1, 2], 3, True),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 27, True),
        ([1], 1, True),
        ([1], 2, False),
    ],
)
def test_has_path_sum(root_list, targetSum, expected):
    """Test cases for path sum"""
    sol = Solution()
    root = list_to_tree(root_list)
    result = sol.hasPathSum(root, targetSum)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
