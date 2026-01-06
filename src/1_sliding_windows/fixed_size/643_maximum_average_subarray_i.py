"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average
value and return this value. Any answer with a calculation error less than 10^-5
will be accepted.

Example 1:
Input: nums = [1, 12, -5, -6, 50, 3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
"""

from typing import List
import pytest


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pass


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 12, -5, -6, 50, 3], 4, 12.75000),
        ([5], 1, 5.00000),
        ([1, 2, 3, 4, 5], 3, 4.0),  # Average of [3, 4, 5]
        ([0, 4, 0, 3, 2], 1, 4.0),  # Single element maximum
    ],
)
def test_find_max_average_parametrized(nums, k, expected):
    """Parametrized tests for multiple cases"""
    s = Solution()
    result = s.findMaxAverage(nums, k)
    assert abs(result - expected) < 1e-5, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
