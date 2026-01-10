"""
1776. Car Fleet II

There are n cars traveling at different speeds along a one-lane road. Each car is represented by
its position and speed, given in an array cars where cars[i] = [position_i, speed_i]:

- position_i is the distance (in meters) of the i-th car from the start of the road.
- speed_i is the speed (in meters per second) of the i-th car.

The cars are ordered by position, ensuring that position_i < position_{i+1}.

When a faster car catches up to a slower car ahead, they collide and form a fleet. After the
collision:
- The cars move together as a single unit.
- The fleet moves at the speed of the slower car.

The task is to determine when each car will collide with the car directly in front of it. The
output should be an array answer where answer[i] represents:
- The time (in seconds) when car i collides with car i+1.
- -1.0 if car i never collides with the next car.

Example 1:
Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]

Explanation:
- After exactly one second, the first car will collide with the second car, forming a fleet with
  speed 1 m/s.
- After exactly 3 seconds, the third car will collide with the fourth car, forming a fleet with
  speed 2 m/s.

Example 2:
Input: cars = [[3,4],[5,4],[6,3],[9,1]]
Output: [2.00000,1.00000,1.50000,-1.00000]

Constraints:
- 1 <= cars.length <= 10^5
- 1 <= position_i, speed_i <= 10^6
- position_i < position_{i+1}
"""

from typing import List
import pytest


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        pass


@pytest.mark.parametrize(
    "cars, expected",
    [
        ([[1, 2], [2, 1], [4, 3], [7, 2]], [1.0, -1.0, 3.0, -1.0]),
        ([[3, 4], [5, 4], [6, 3], [9, 1]], [2.0, 1.0, 1.5, -1.0]),
    ],
)
def test_get_collision_times(cars, expected):
    s = Solution()
    result = s.getCollisionTimes(cars)
    assert len(result) == len(expected), "Result length mismatch"
    for i, (r, e) in enumerate(zip(result, expected)):
        if e == -1.0:
            assert r == -1.0, f"Expected -1.0 at index {i}, got {r}"
        else:
            assert abs(r - e) < 1e-5, f"Expected {e} at index {i}, got {r}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
