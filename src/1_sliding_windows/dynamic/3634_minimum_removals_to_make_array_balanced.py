"""
3634. Minimum Removals to Make Array Balanced

You are given a 0-indexed array nums of n integers.

You can perform the following operation any number of times:
- Choose an index i (0 <= i < n) and change nums[i] to any positive integer.

Return the minimum number of operations required to make the array balanced.

An array is balanced if:
- nums[0] <= nums[1] <= ... <= nums[i - 1] <= nums[i]
- AND nums[i] >= nums[i + 1] >= ... >= nums[n - 1]

In other words, an array is balanced if it is non-decreasing from the start up to some index i, and non-increasing from index i to the end.

Example 1:
Input: nums = [1,2,3,4,1]
Output: 1
Explanation: Change nums[4] to 4. The array becomes [1,2,3,4,4], which is balanced.

Example 2:
Input: nums = [1,2,3,4,5]
Output: 0
Explanation: The array is already balanced.

Example 3:
Input: nums = [5,4,3,2,1]
Output: 1
Explanation: Change nums[0] to 1. The array becomes [1,4,3,2,1], which is balanced.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

from typing import List
import pytest


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Your code here
        pass


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4, 1], 1),
        ([1, 2, 3, 4, 5], 0),
        ([5, 4, 3, 2, 1], 1),
        ([1, 1, 1, 1, 1], 0),
        ([1, 3, 2, 4, 1], 1),
    ],
)
def test_minimum_operations(nums, expected):
    """Parametrized tests for multiple cases"""
    sol = Solution()
    result = sol.minimumOperations(nums)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
