"""
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
- 1 <= s.length <= 10^5
- s[i] is a printable ascii character.
"""

from typing import List
import pytest


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Your code here
        pass


@pytest.mark.parametrize(
    "s, expected",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
        (["a"], ["a"]),
        (["a", "b"], ["b", "a"]),
        (["A", "B", "C"], ["C", "B", "A"]),
    ],
)
def test_reverse_string(s, expected):
    """Test cases for reverse string"""
    sol = Solution()
    # Create a copy since we're modifying in-place
    s_copy = s.copy()
    sol.reverseString(s_copy)
    assert s_copy == expected, f"Expected {expected}, got {s_copy}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

