"""
1852. Distinct Numbers in Each Subarray

Given an integer array nums and an integer k, return an array answer where
answer[i] is the number of distinct numbers in the subarray nums[i:i+k].

Example 1:
Input: nums = [1,2,3,2,2,1,2], k = 3
Output: [3,2,2,2,3]

Example 2:
Input: nums = [1,1,1,1,2,3,4], k = 4
Output: [1,2,3,4]
"""

from typing import List
import pytest 

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        pass


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1,2,3,2,2,1,2], 3, [3,2,2,2,3]),
        ([1, 1, 1,1,2,3,4], 4, [1, 2, 3, 4])
    ]
)
def test_distinct_numbers(nums, k, expected):
    s = Solution()
    result = s.distinctNumbers(nums, k)
    assert result == expected, f"Expected: {expected}, got result: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
