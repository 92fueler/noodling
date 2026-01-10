"""
654. Maximum Binary Tree

Given an integer array nums with no duplicates, construct a maximum binary tree using the following
algorithm:

1. The root is the maximum number in nums.
2. The left subtree is the maximum tree constructed from the subarray to the left of the maximum number.
3. The right subtree is the maximum tree constructed from the subarray to the right of the maximum number.

Return the maximum binary tree built from nums.

Note: This problem requires an O(n) solution.

Example:
Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explanation: The maximum tree is:
      6
    /   \
   3     5
    \    /
     2  0
      \
       1

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 1000
- All integers in nums are unique.
"""

from typing import List, Optional
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        pass


# Note: Tree comparison tests would require a helper function
# For now, we'll test with basic structure validation
@pytest.mark.parametrize(
    "nums",
    [
        ([3, 2, 1, 6, 0, 5]),
        ([1]),
        ([1, 2, 3]),
        ([3, 2, 1]),
    ],
)
def test_construct_maximum_binary_tree(nums):
    s = Solution()
    result = s.constructMaximumBinaryTree(nums)
    assert result is not None, "Tree should not be None"
    # Basic validation: root should be the maximum value
    assert result.val == max(nums), f"Root should be {max(nums)}, got {result.val}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
