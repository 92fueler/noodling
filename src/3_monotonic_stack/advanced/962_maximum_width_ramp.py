"""
962. Maximum Width Ramp

Given an integer array nums, a ramp is a pair (i, j) where i < j and nums[i] <= nums[j]. The width
of such a ramp is j - i.

Return the maximum width of a ramp in nums. If no such ramp exists, return 0.

Example 1:
Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5), where nums[1] = 0 and nums[5] = 5.

Example 2:
Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9), where nums[2] = 1 and nums[9] = 1.

Constraints:
- 2 <= nums.length <= 50,000
- 0 <= nums[i] <= 50,000
"""

from typing import List
import pytest


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        pass


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([6, 0, 8, 2, 1, 5], 4),
        ([9, 8, 1, 0, 1, 9, 4, 0, 4, 1], 7),
        ([1], 0),
        ([1, 2, 3], 2),
    ],
)
def test_max_width_ramp(nums, expected):
    s = Solution()
    result = s.maxWidthRamp(nums)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
