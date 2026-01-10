"""
739. Daily Temperatures

Given an array of integers temperatures representing the daily temperatures, return an array answer
such that answer[i] is the number of days you have to wait after the i-th day to get a warmer
temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
Explanation:
- Day 0: Wait 1 day for warmer temperature (74 > 73)
- Day 1: Wait 1 day for warmer temperature (75 > 74)
- Day 2: Wait 4 days for warmer temperature (76 > 75)
- Day 3: Wait 2 days for warmer temperature (72 > 71)
- Day 4: Wait 1 day for warmer temperature (72 > 69)
- Day 5: Wait 1 day for warmer temperature (76 > 72)
- Day 6: No warmer temperature, answer is 0
- Day 7: No warmer temperature, answer is 0

Example 2:
Input: temperatures = [30, 40, 50, 60]
Output: [1, 1, 1, 0]

Example 3:
Input: temperatures = [30, 60, 90]
Output: [1, 1, 0]

Constraints:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100
"""

from typing import List
import pytest


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pass


@pytest.mark.parametrize(
    "temperatures, expected",
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([55], [0]),
        ([70, 69, 68, 67], [0, 0, 0, 0]),
    ],
)
def test_daily_temperatures(temperatures, expected):
    s = Solution()
    result = s.dailyTemperatures(temperatures)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
