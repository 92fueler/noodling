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

import pytest
from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hash_map = defaultdict(int)

        left, right = 0, 0
        max_length = 0

        while right < len(s):
            hash_map[s[right]] += 1

            while hash_map[s[right]] > 2:
                hash_map[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 6),  # "abcabc" - a:2, b:2, c:2
        ("aabbcc", 6),  # "aabbcc" (entire string)
        ("aaabb", 4),  # "aabb"
        ("aaaa", 2),  # "aa"
        ("abcde", 5),  # "abcde" (entire string)
        ("ababab", 4),  # "abab"
        ("aabbccdd", 8),  # "aabbccdd" (entire string)
        ("aaabbbccc", 4),  # "aabb" or "bbcc" - max is 4, not 6!
        ("a", 1),  # single character
        ("aabbc", 5),  # "aabbc" (entire string)
    ],
)
def test_maximum_length_substring(s, expected):
    """Parametrized tests for multiple cases"""
    sol = Solution()
    result = sol.maximumLengthSubstring(s)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
