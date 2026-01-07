"""
1208. Get Equal Substrings Within Budget

You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost.

If there is no substring from s that can be changed to its corresponding substring from t, return 0.

Example 1:
Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd" of t. That costs 3, so the maximum length is 3.

Example 2:
Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to the corresponding character in t, so the maximum length is 1.

Example 3:
Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You cannot make any change, so the maximum length is 1.

Constraints:
- 1 <= s.length <= 10^5
- t.length == s.length
- 0 <= maxCost <= 10^6
- s and t consist of only lowercase English letters.
"""

import pytest


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # Your code here
        pass


@pytest.mark.parametrize(
    "s, t, maxCost, expected",
    [
        ("abcd", "bcdf", 3, 3),
        ("abcd", "cdef", 3, 1),
        ("abcd", "acde", 0, 1),
        ("krrgw", "zjxss", 19, 2),
        ("abcd", "abcd", 0, 4),
        ("abcd", "efgh", 10, 4),
    ],
)
def test_equal_substring(s, t, maxCost, expected):
    """Parametrized tests for multiple cases"""
    sol = Solution()
    result = sol.equalSubstring(s, t, maxCost)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
