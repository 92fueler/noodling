"""
3113. Find the Number of Subarrays Where Boundary Elements Are Maximum

You are given an array of positive integers nums.

Return the number of subarrays of nums where the first and the last elements of the subarray are
equal to the largest element in the subarray.

Example:
Input: nums = [1, 4, 3, 3, 2]
Output: 6

Explanation:
There are 6 subarrays where the first and last elements are equal to the largest element in the
subarray:
1. Subarray [1], with its largest element 1. The first and last elements are both 1.
2. Subarray [4], with its largest element 4. The first and last elements are both 4.
3. Subarray [3], with its largest element 3. The first and last elements are both 3.
4. Subarray [3], with its largest element 3. The first and last elements are both 3.
5. Subarray [2], with its largest element 2. The first and last elements are both 2.
6. Subarray [4, 3, 3, 2], with its largest element 4. The first and last elements are both 4.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

from typing import List
import pytest


class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        pass


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 4, 3, 3, 2], 6),
        ([1], 1),
        ([1, 2, 3], 3),
        ([3, 2, 1], 3),
    ],
)
def test_number_of_subarrays(nums, expected):
    s = Solution()
    result = s.numberOfSubarrays(nums)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
