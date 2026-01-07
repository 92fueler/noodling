"""
2107. Number of Unique Flavors After Sharing K Candies

You are given an integer array candies, where candies[i] represents the flavor
of the i-th candy. You are also given an integer k.

You will share k consecutive candies with your friend. You want to choose k
consecutive candies such that after sharing them, you have the maximum number of
unique flavors remaining.

Return the maximum number of unique flavors you can have after sharing k
consecutive candies.

Example 1:
Input: candies = [1,2,2,3,4,3], k = 3
Output: 3
Explanation:
You can share candies [2,2,3] with your friend, and you will have candies
[1,3,4,3]. The unique flavors are [1,3,4], so the answer is 3.

Example 2:
Input: candies = [2,2,2,2,3,3], k = 2
Output: 2
Explanation:
You can share candies [2,2] with your friend, and you will have candies
[2,2,3,3]. The unique flavors are [2,3], so the answer is 2.

Example 3:
Input: candies = [2,4,5], k = 0
Output: 3
Explanation:
You do not have to share any candies, so the unique flavors are [2,4,5], so the
answer is 3.
"""

from typing import List
import pytest


class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        pass


@pytest.mark.parametrize(
    "candies, k, expected",
    [([1, 2, 2, 3, 4, 3], 3, 3), ([2, 2, 2, 2, 3, 3], 2, 2), ([2, 4, 5], 0, 3)],
)
def test_share_candies(candies, k, expected):
    s = Solution()
    result = s.shareCandies(candies, k)
    assert result == expected, f"Expected: {expected}, got result: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
