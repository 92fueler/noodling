"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols, and spaces.
"""

from typing import List
import pytest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Your code here
        pass


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
    ],
)
def test_length_of_longest_substring(s, expected):
    """Parametrized tests for multiple cases"""
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

