"""
3555. Sort Smallest Subarray for Each Sliding Window (Premium)

Given an array nums and an integer k, for each sliding window of size k, find the smallest
subarray within that window that needs to be sorted to make the entire window sorted.

Return an array answer where answer[i] is the length of the smallest subarray that needs to be
sorted for the window starting at index i.

Note: This is a premium problem and requires a non-brute force approach.

Example:
Input: nums = [1,3,2,4,5], k = 3
Output: [2, 0, 0]

Explanation:
- Window [1,3,2]: Need to sort [3,2] to get [1,2,3], length is 2
- Window [3,2,4]: Already sorted, length is 0
- Window [2,4,5]: Already sorted, length is 0

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= nums.length
"""

from typing import List
import pytest


class Solution:
    def minSubarrayLength(self, nums: List[int], k: int) -> List[int]:
        pass


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 3, 2, 4, 5], 3, [2, 0, 0]),
        # Add more test cases as needed
    ],
)
def test_min_subarray_length(nums, k, expected):
    s = Solution()
    result = s.minSubarrayLength(nums, k)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
