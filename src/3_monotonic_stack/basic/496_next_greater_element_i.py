"""
496. Next Greater Element I

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of
nums2. For each element in nums1, find the next greater element in nums2.

The next greater element of an element x in nums1 is the first greater element to its right in
nums2. If no such element exists, return -1 for that element.

Example 1:
Input: nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
Output: [-1, 3, -1]
Explanation:
- For number 4 in nums1, there is no greater number to its right in nums2, so the output is -1.
- For number 1 in nums1, the next greater number in nums2 is 3.
- For number 2 in nums1, there is no greater number to its right in nums2, so the output is -1.

Example 2:
Input: nums1 = [2, 4], nums2 = [1, 2, 3, 4]
Output: [3, -1]
Explanation:
- For number 2 in nums1, the next greater number in nums2 is 3.
- For number 4 in nums1, there is no greater number to its right in nums2, so the output is -1.

Constraints:
- 1 <= nums1.length <= nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 10^4
- All integers in nums1 and nums2 are unique.
- All the integers of nums1 also appear in nums2.
"""

from typing import List
import pytest


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pass


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
        ([2, 4], [1, 2, 3, 4], [3, -1]),
        ([1], [1], [-1]),
        ([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7], [7, 7, 7, 7, 7]),
    ],
)
def test_next_greater_element(nums1, nums2, expected):
    s = Solution()
    result = s.nextGreaterElement(nums1, nums2)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
