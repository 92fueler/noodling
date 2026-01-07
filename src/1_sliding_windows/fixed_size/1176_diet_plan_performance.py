"""
1176. Diet Plan Performance

Problem Statement:
A dieter consumes calories[i] calories on the i-th day.

Given an integer k, for every consecutive sequence of k days (calories[i],
calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k), they look at T, the
total calories consumed during that sequence of k days:

- If T < lower, they performed poorly on their diet and lose 1 point.
- If T > upper, they performed well on their diet and gain 1 point.
- Otherwise, they performed normally and there is no change in points.

Initially, the dieter has zero points. Return the total number of points the
dieter has after dieting for n days.

Note that the total points can be negative.

Example 1:
Input: calories = [1, 2, 3, 4, 5], k = 1, lower = 3, upper = 3
Output: 0
Explanation: Since k = 1, we consider each element of the array separately and
compare it to lower and upper.
calories[0] and calories[1] are less than lower so 2 points are lost.
calories[3] and calories[4] are greater than upper so 2 points are gained.

Example 2:
Input: calories = [3, 2], k = 2, lower = 0, upper = 1
Output: 1

Example 3:
Input: calories = [6,5,0,0], k = 2, lower = 1, upper = 5
Output: 0
"""

from typing import List
import pytest


class Solution:
    def dietPlanPerformance(
        self, calories: List[int], k: int, lower: int, upper: int
    ) -> int:
        pass


@pytest.mark.parametrize(
    "calories, k, lower, upper, expected",
    [([3, 2], 2, 0, 1, 1), ([6, 5, 0, 0], 2, 1, 5, 0)],
)
def test_diet_plan_performance(calories, k, lower, upper, expected):
    s = Solution()
    result = s.dietPlanPerformance(calories, k, lower, upper)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
