"""
404. Sum of Left Leaves

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:
Input: root = [1]
Output: 0

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- -1000 <= Node.val <= 1000
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Your code here
        pass


@pytest.mark.parametrize(
    "root_list, expected",
    [
        ([3, 9, 20, None, None, 15, 7], 24),
        ([1], 0),
        ([1, 2, 3, 4, 5], 4),
        ([1, 2, 3, 4, 5, 6, 7], 10),
        ([3, 9, 20, None, None, 15, 7, None, None, None, None, 8], 17),
    ],
)
def test_sum_of_left_leaves(root_list, expected):
    """Test cases for sum of left leaves"""
    sol = Solution()
    root = list_to_tree(root_list)
    result = sol.sumOfLeftLeaves(root)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

