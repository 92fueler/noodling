"""
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.

Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number 0 at index 2, a longest subarray of only 1's is [1,1,1], which has length 3.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number 0 at index 0, a longest subarray of only 1's is [1,1,1,1,1], which has length 5.

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
"""

from typing import List
import pytest

from collections import defaultdict


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        hash_map = defaultdict(int)

        left, right = 0, 0
        max_length = 0  # max length with one 0

        while right < len(nums):
            right_num = nums[right]
            hash_map[right_num] += 1

            while right_num == 0 and hash_map[right_num] > 1:
                hash_map[nums[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length - 1


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 1, 0, 1], 3),
        ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5),
        ([1, 1, 1], 2),
    ],
)
def test_longest_subarray(nums, expected):
    """Parametrized tests for multiple cases"""
    sol = Solution()
    result = sol.longestSubarray(nums)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
