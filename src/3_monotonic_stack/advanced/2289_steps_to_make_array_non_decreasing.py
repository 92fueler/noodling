"""
2289. Steps to Make Array Non-decreasing

You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where
nums[i - 1] > nums[i] for all 0 < i < nums.length.

Return the number of steps performed until nums becomes a non-decreasing array.

Example 1:
Input: nums = [5,3,4,4,7,3,6,11,8,5,11]
Output: 3

Explanation:
- Step 1: [5,3,4,4,7,3,6,11,8,5,11] becomes [5,4,4,7,6,11,11]
- Step 2: [5,4,4,7,6,11,11] becomes [5,4,7,11,11]
- Step 3: [5,4,7,11,11] becomes [5,7,11,11]

The array [5,7,11,11] is now non-decreasing. Therefore, the function returns 3.

Example 2:
Input: nums = [4,5,7,7,13]
Output: 0
Explanation: The array is already non-decreasing, so no steps are needed.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

from typing import List
import pytest


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        pass


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11], 3),
        ([4, 5, 7, 7, 13], 0),
        ([1], 0),
        ([7, 14, 4, 14, 13, 2, 6, 13], 3),
    ],
)
def test_total_steps(nums, expected):
    s = Solution()
    result = s.totalSteps(nums)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
