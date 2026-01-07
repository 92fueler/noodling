"""
1100. Find K-Length Substrings With No Repeated Characters

Given a string s and an integer k, return the number of substrings in s of length
k with no repeated characters.

Example 1:
Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation:
There are 6 substrings they are: 'havef','avefu','vefun','efuno','funon','onlee'.

Example 2:
Input: s = "home", k = 5
Output: 0
"""

import pytest

# approach 1: using set
# approach 2: using hashmap


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        pass


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("havefunonleetcode", 5, 6),
        ("home", 5, 0),
    ],
)
def test_numKLenSubstrNoRepeats(s, k, expected):
    solution = Solution()
    result = solution.numKLenSubstrNoRepeats(s, k)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
