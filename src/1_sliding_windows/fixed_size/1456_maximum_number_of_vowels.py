"""
1456. Maximum Number of Vowels in a Substring of Given Length

Problem Statement:
Given a string s and an integer k, return the maximum number of vowel letters
in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet", "etc", "tco", "cod", "ode" all contain 2 vowels.
"""
import pytest


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        pass


# s = "leetcode"
# k = 3

s = "abciiidef"
k = 3

sol = Solution()
result = sol.maxVowels(s, k)
print(result)
if __name__ == "__main__":
    pytest.main([__file__, "-v"])

