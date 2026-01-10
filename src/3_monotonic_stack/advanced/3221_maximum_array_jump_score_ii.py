"""
3221. Maximum Array Jump Score II (Premium)

You are given a 0-indexed array nums of n integers and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward (meaning
you can jump to any index in the range [i + 1, min(i + k, n - 1)]).

The score of a jump from index i to index j is nums[j] - nums[i].

Return the maximum score you can achieve.

Note: This is a premium problem.

Example:
Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7

Explanation:
- Start at index 0, jump to index 2 (score: -2 - 1 = -3)
- Jump from index 2 to index 4 (score: -7 - (-2) = -5)
- Jump from index 4 to index 5 (score: 3 - (-7) = 10)
- Total score: -3 + (-5) + 10 = 2

But we can do better:
- Start at index 0, jump to index 1 (score: -1 - 1 = -2)
- Jump from index 1 to index 3 (score: 4 - (-1) = 5)
- Jump from index 3 to index 5 (score: 3 - 4 = -1)
- Total score: -2 + 5 + (-1) = 2

Actually, the maximum score path needs to be calculated.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 1 <= k <= nums.length
"""

from typing import List
import pytest


class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        pass


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, -1, -2, 4, -7, 3], 2, 7),
        # Add more test cases as needed
    ],
)
def test_max_score(nums, k, expected):
    s = Solution()
    result = s.maxScore(nums, k)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
