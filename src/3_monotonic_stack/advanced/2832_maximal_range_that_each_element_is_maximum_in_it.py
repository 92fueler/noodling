"""
2832. Maximal Range That Each Element Is Maximum In It (Premium)

Given an array nums of n integers, for each element nums[i], find the maximum range [l, r] such that
nums[i] is the maximum element in the subarray nums[l...r].

Return an array answer where answer[i] = [l, r] represents the maximal range for nums[i].

Note: This is a premium problem.

Example:
Input: nums = [1, 5, 4, 3, 1]
Output: [[0, 1], [0, 4], [2, 4], [2, 4], [4, 4]]

Explanation:
- For nums[0] = 1: Maximum range is [0, 1] where 1 is the max
- For nums[1] = 5: Maximum range is [0, 4] where 5 is the max
- For nums[2] = 4: Maximum range is [2, 4] where 4 is the max
- For nums[3] = 3: Maximum range is [2, 4] where 3 is the max (but 4 is also max, so range is [2, 4])
- For nums[4] = 1: Maximum range is [4, 4] where 1 is the max

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

from typing import List
import pytest


class Solution:
    def maximumRange(self, nums: List[int]) -> List[List[int]]:
        pass


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 5, 4, 3, 1], [[0, 1], [0, 4], [2, 4], [2, 4], [4, 4]]),
        # Add more test cases as needed
    ],
)
def test_maximum_range(nums, expected):
    s = Solution()
    result = s.maximumRange(nums)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
