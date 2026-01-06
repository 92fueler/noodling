"""
2958. Length of Longest Subarray With at Most K Frequency

You are given an integer array nums and an integer k.

The frequency of an element is the number of times it occurs in an array.

Return the length of the longest subarray such that the frequency of each element in that subarray is less than or equal to k.

Example 1:
Input: nums = [1,2,3,1,2,3,1,2], k = 2
Output: 6
Explanation: The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most 2 times in this subarray. Note that the subarray [1,2,3,1,2,3,1,2] has a frequency of 3 for the value 1, so it is not a valid subarray.

Example 2:
Input: nums = [1,2,1,2,1,2,1,2], k = 1
Output: 2
Explanation: The longest possible good subarray is [1,2] since the values 1 and 2 occur at most once in this subarray.

Example 3:
Input: nums = [5,5,5,5,5,5,5], k = 4
Output: 4
Explanation: The longest possible good subarray is [5,5,5,5] since the value 5 occurs 4 times in this subarray.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= nums.length
"""

from typing import List
import pytest


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # Your code here
        pass


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 3, 1, 2, 3, 1, 2], 2, 6),
        ([1, 2, 1, 2, 1, 2, 1, 2], 1, 2),
        ([5, 5, 5, 5, 5, 5, 5], 4, 4),
        ([1, 1, 1, 1, 1], 2, 2),
        ([1, 2, 3, 4, 5], 1, 1),
    ],
)
def test_max_subarray_length(nums, k, expected):
    """Parametrized tests for multiple cases"""
    sol = Solution()
    result = sol.maxSubarrayLength(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

