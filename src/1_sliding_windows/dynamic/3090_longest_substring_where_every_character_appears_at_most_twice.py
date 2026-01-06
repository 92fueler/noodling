"""
3090. Longest Substring Where Every Character Appears At Most Twice

Given a string s, find the length of the longest substring where each character appears at most twice.

Example 1:
Input: s = "abcabcbb"
Output: 5
Explanation: The answer is "abcab", with the length of 5.

Example 2:
Input: s = "aabbcc"
Output: 6
Explanation: The entire string "aabbcc" is valid.

Example 3:
Input: s = "aaabb"
Output: 4
Explanation: The answer is "aabb", with the length of 4.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
"""

from typing import List
import pytest


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # Your code here
        pass


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 5),
        ("aabbcc", 6),
        ("aaabb", 4),
        ("aaaa", 2),
        ("abcde", 5),
        ("ababab", 6),
    ],
)
def test_maximum_length_substring(s, expected):
    """Parametrized tests for multiple cases"""
    sol = Solution()
    result = sol.maximumLengthSubstring(s)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

