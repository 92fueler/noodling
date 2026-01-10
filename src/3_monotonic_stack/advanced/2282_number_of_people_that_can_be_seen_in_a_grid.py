"""
2282. Number of People That Can Be Seen in a Grid (Premium)

You are given an m x n grid where grid[i][j] represents the height of a person standing at
position (i, j).

A person at position (i, j) can see another person at position (x, y) if:
- The line connecting (i, j) and (x, y) does not pass through any person taller than both.
- The person at (x, y) is in one of the 8 directions (horizontal, vertical, or diagonal).

Return a 2D array answer where answer[i][j] is the number of people that the person at (i, j)
can see.

Note: This is a premium problem.

Example:
Input: grid = [[3,1,4,2,5]]
Output: [[2,2,2,3,1]]

Explanation:
- Person at (0,0) can see persons at (0,2) and (0,4)
- Person at (0,1) can see persons at (0,2) and (0,4)
- Person at (0,2) can see persons at (0,3) and (0,4)
- Person at (0,3) can see persons at (0,4)
- Person at (0,4) can see no one

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 500
- 1 <= grid[i][j] <= 10^5
"""

from typing import List
import pytest


class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        pass


@pytest.mark.parametrize(
    "heights, expected",
    [
        ([[3, 1, 4, 2, 5]], [[2, 2, 2, 3, 1]]),
        # Add more test cases as needed
    ],
)
def test_see_people(heights, expected):
    s = Solution()
    result = s.seePeople(heights)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
