"""
3542. Minimum Operations to Make All Elements Zero

You are given an array nums of size n, consisting of non-negative integers. Your task is to apply
some (possibly zero) operations on the array so that all elements become 0.

In one operation, you can select a subarray [i, j] (where 0 <= i <= j < n) and set all occurrences
of the minimum non-negative integer in that subarray to 0.

Return the minimum number of operations required to make all elements in the array 0.

Example 1:
Input: nums = [0, 2]
Output: 1
Explanation:
- Select the subarray [1,1] (which is [2]), where the minimum non-negative integer is 2. Setting
  all occurrences of 2 to 0 results in [0,0].
- Thus, the minimum number of operations required is 1.

Example 2:
Input: nums = [3, 1, 2, 1]
Output: 3
Explanation:
- Select subarray [1,3] (which is [1,2,1]), where the minimum non-negative integer is 1. Setting
  all occurrences of 1 to 0 results in [3,0,2,0].
- Select subarray [2,2] (which is [2]), where the minimum non-negative integer is 2. Setting all
  occurrences of 2 to 0 results in [3,0,0,0].
- Select subarray [0,0] (which is [3]), where the minimum non-negative integer is 3. Setting all
  occurrences of 3 to 0 results in [0,0,0,0].
- Thus, the minimum number of operations required is 3.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
"""

from typing import List
import pytest


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        pass


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 2], 1),
        ([3, 1, 2, 1], 3),
        ([0], 0),
        ([1, 1, 1], 1),
    ],
)
def test_min_operations(nums, expected):
    s = Solution()
    result = s.minOperations(nums)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
