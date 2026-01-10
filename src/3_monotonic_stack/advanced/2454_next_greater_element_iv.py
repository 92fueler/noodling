"""
2454. Next Greater Element IV

You are given a 0-indexed array of non-negative integers nums. For each integer in nums, you must
find its respective second greater integer.

The second greater integer of nums[i] is nums[j] such that:
- j > i
- nums[j] > nums[i]
- There exists exactly one index k such that nums[k] > nums[i] and i < k < j.

If there is no such nums[j], the second greater integer is considered to be -1.

Return an integer array answer, where answer[i] is the second greater integer of nums[i].

Example:
Input: nums = [2, 4, 0, 9, 6]
Output: [9, 6, 6, -1, -1]

Explanation:
- For nums[0] = 2: The first greater element is 4 at index 1, and the second greater element is
  9 at index 3.
- For nums[1] = 4: The first greater element is 9 at index 3, and the second greater element is
  6 at index 4.
- For nums[2] = 0: The first greater element is 9 at index 3, and the second greater element is
  6 at index 4.
- For nums[3] = 9 and nums[4] = 6: There are no greater elements to their right, so the result
  is -1 for both.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
"""

from typing import List
import pytest


class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        pass


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 4, 0, 9, 6], [9, 6, 6, -1, -1]),
        ([3, 3], [-1, -1]),
        ([1, 2, 3], [-1, -1, -1]),
    ],
)
def test_second_greater_element(nums, expected):
    s = Solution()
    result = s.secondGreaterElement(nums)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
