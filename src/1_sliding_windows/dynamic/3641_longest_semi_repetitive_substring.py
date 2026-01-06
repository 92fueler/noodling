"""
3641. Longest Semi-Repetitive Substring

You are given a string s that consists of digits from 0 to 9.

A string t is called semi-repetitive if there is at most one pair of consecutive same digits. For example, "0010", "002020", "0123", "2002", and "54944" are semi-repetitive while "00101022", and "1101234883" are not.

Return the length of the longest semi-repetitive substring of s.

A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
Input: s = "52233"
Output: 4
Explanation: The longest semi-repetitive substring is "5223", which can be obtained by removing the last character.

Example 2:
Input: s = "5494"
Output: 4
Explanation: s is a semi-repetitive string, so the answer is 4.

Example 3:
Input: s = "11111"
Output: 2
Explanation: The longest semi-repetitive substring is "11", which can be obtained by removing the last three characters.

Constraints:
- 1 <= s.length <= 50
- s consists of digits.
"""

from typing import List
import pytest


class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        # Your code here
        pass


@pytest.mark.parametrize(
    "s, expected",
    [
        ("52233", 4),
        ("5494", 4),
        ("11111", 2),
        ("0010", 4),
        ("00101022", 3),
        ("123456", 6),
    ],
)
def test_longest_semi_repetitive_substring(s, expected):
    """Parametrized tests for multiple cases"""
    sol = Solution()
    result = sol.longestSemiRepetitiveSubstring(s)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

