"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
- 1 <= n <= 45
"""

import pytest


class Solution:
    def climbStairs(self, n: int) -> int:
        # Your code here
        pass


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (7, 21),
        (10, 89),
        (20, 10946),
    ],
)
def test_climb_stairs(n, expected):
    """Test cases for climbing stairs"""
    sol = Solution()
    result = sol.climbStairs(n)
    assert result == expected, (
        f"Expected {expected} ways to climb {n} stairs, got {result}"
    )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
