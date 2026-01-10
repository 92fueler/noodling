"""
2866. Beautiful Towers II

You are given a 0-indexed array maxHeights of n integers.

Your task is to build n towers along a coordinate line, where the i-th tower is located at coordinate
i and has a height of heights[i].

A configuration of towers is considered beautiful if it satisfies the following conditions:

1. 1 <= heights[i] <= maxHeights[i]
2. The array heights forms a mountain array.

An array heights is defined as a mountain array if there exists an index i such that:
- For all 0 < j <= i, heights[j - 1] <= heights[j]
- For all i <= k < n - 1, heights[k + 1] <= heights[k]

The objective is to return the maximum possible sum of heights for a beautiful configuration of towers.

Example:
Input: maxHeights = [5,3,4,1,1]
Output: 13
Explanation: One possible beautiful configuration with the maximum sum is heights = [5,3,3,1,1].
This configuration is beautiful because:
- 1 <= heights[i] <= maxHeights[i]
- heights forms a mountain array with the peak at i = 0.

Constraints:
- 1 <= n == maxHeights.length <= 10^5
- 1 <= maxHeights[i] <= 10^9
"""

from typing import List
import pytest


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        pass


@pytest.mark.parametrize(
    "maxHeights, expected",
    [
        ([5, 3, 4, 1, 1], 13),
        ([6, 5, 3, 9, 2, 7], 22),
        ([3, 2, 5, 5, 2, 3], 18),
    ],
)
def test_maximum_sum_of_heights(maxHeights, expected):
    s = Solution()
    result = s.maximumSumOfHeights(maxHeights)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
