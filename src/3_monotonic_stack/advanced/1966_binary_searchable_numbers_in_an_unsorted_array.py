"""
1966. Binary Searchable Numbers in an Unsorted Array (Premium)

Given an array nums of n integers, return the number of indices that can be found using binary
search in nums, even though nums is not sorted.

An index i is binary searchable if there exists a target value such that binary search on nums
will find the element at index i.

Note: This is a premium problem.

Example:
Input: nums = [2, 1, 3, 4, 5]
Output: 3

Explanation:
- Index 0 (value 2) is searchable: search for 2
- Index 1 (value 1) is searchable: search for 1
- Index 2 (value 3) is searchable: search for 3
- Index 3 (value 4) is not searchable: if we search for 4, binary search might go to index 2 first
- Index 4 (value 5) is not searchable

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

from typing import List
import pytest


class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        pass


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 1, 3, 4, 5], 3),
        # Add more test cases as needed
    ],
)
def test_binary_searchable_numbers(nums, expected):
    s = Solution()
    result = s.binarySearchableNumbers(nums)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
