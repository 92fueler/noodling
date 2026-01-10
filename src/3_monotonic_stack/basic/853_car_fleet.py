"""
853. Car Fleet

There are n cars going to the same destination along a one-lane road. The destination is target
miles away.

You are given two integer arrays position and speed, both of length n, where position[i] is the
position of the i-th car and speed[i] is the speed of the i-th car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper
at the same speed. The faster car will slow down to match the slower car's speed. The distance
between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and the same speed. Note
that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as
one car fleet.

Return the number of car fleets that will arrive at the destination.

Example 1:
Input: target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]
Output: 3
Explanation:
- The cars starting at positions 10 and 8 form a fleet, meeting each other at the destination.
- The car starting at position 0 does not catch up to any other car and forms its own fleet.
- The cars starting at positions 5 and 3 form a fleet, meeting each other before the destination.

Example 2:
Input: target = 10, position = [3], speed = [3]
Output: 1

Example 3:
Input: target = 100, position = [0, 2, 4], speed = [4, 2, 1]
Output: 1
Explanation:
- The cars starting at positions 0, 2, and 4 form a fleet, meeting each other at the destination.

Constraints:
- n == position.length == speed.length
- 1 <= n <= 10^5
- 0 < target <= 10^6
- 0 <= position[i] < target
- All the values of position are unique.
- 0 < speed[i] <= 10^6
"""

from typing import List
import pytest


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pass


@pytest.mark.parametrize(
    "target, position, speed, expected",
    [
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),
        (10, [3], [3], 1),
        (100, [0, 2, 4], [4, 2, 1], 1),
        (10, [6, 8], [3, 2], 2),
        (10, [0, 4, 2], [2, 1, 3], 1),
    ],
)
def test_car_fleet(target, position, speed, expected):
    s = Solution()
    result = s.carFleet(target, position, speed)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
