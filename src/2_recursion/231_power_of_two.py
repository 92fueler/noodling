"""
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2^x.

Example 1:
Input: n = 1
Output: true
Explanation: 2^0 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 2^4 = 16

Example 3:
Input: n = 3
Output: false

Constraints:
- -2^31 <= n <= 2^31 - 1
"""

import pytest


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Your code here
        pass


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, True),
        (2, True),
        (4, True),
        (8, True),
        (16, True),
        (32, True),
        (1024, True),
        (3, False),
        (5, False),
        (6, False),
        (7, False),
        (9, False),
        (10, False),
        (0, False),
        (-1, False),
        (-16, False),
    ],
)
def test_is_power_of_two(n, expected):
    """Test cases for power of two"""
    sol = Solution()
    result = sol.isPowerOfTwo(n)
    assert result == expected, f"Expected {n} is power of two: {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

