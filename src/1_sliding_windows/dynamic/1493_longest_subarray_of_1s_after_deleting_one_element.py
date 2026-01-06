"""
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.

Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number 0 at index 2, a longest subarray of only 1's is [1,1,1], which has length 3.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number 0 at index 0, a longest subarray of only 1's is [1,1,1,1,1], which has length 5.

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
"""

from typing import List
import pytest


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Your code here
        pass


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 1, 0, 1], 3),
        ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5),
        ([1, 1, 1], 2),
        ([0, 0, 0], 0),
        ([1, 0, 1, 0, 1, 0, 1], 1),
        ([1, 1, 0, 0, 1, 1, 1, 0, 1, 1], 4),
    ],
)
def test_longest_subarray(nums, expected):
    """Parametrized tests for multiple cases"""
    sol = Solution()
    result = sol.longestSubarray(nums)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

