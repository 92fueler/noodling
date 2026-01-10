"""
1944. Number of Visible People in a Queue

You are given an array heights of distinct integers, where heights[i] represents the height of the
i-th person standing in a queue from left to right. A person can see another person to their right
if all individuals between them are shorter than both. Formally, the i-th person can see the j-th
person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

The task is to return an array answer of the same length as heights, where answer[i] is the number
of people the i-th person can see to their right in the queue.

Example:
Input: heights = [10,6,8,5,11,9]
Output: [3,1,2,1,1,0]

Explanation:
- Person 0 (height 10) can see persons 1 (height 6), 2 (height 8), and 4 (height 11).
- Person 1 (height 6) can see person 2 (height 8).
- Person 2 (height 8) can see persons 3 (height 5) and 4 (height 11).
- Person 3 (height 5) can see person 4 (height 11).
- Person 4 (height 11) can see person 5 (height 9).
- Person 5 (height 9) cannot see anyone to their right.

Constraints:
- n == heights.length
- 1 <= n <= 10^5
- 1 <= heights[i] <= 10^5
- All the values of heights are unique.
"""

from typing import List
import pytest


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        pass


@pytest.mark.parametrize(
    "heights, expected",
    [
        ([10, 6, 8, 5, 11, 9], [3, 1, 2, 1, 1, 0]),
        ([5, 1, 2, 3, 10], [4, 1, 1, 1, 0]),
        ([1], [0]),
    ],
)
def test_can_see_persons_count(heights, expected):
    s = Solution()
    result = s.canSeePersonsCount(heights)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
