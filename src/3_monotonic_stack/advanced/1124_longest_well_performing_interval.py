"""
1124. Longest Well-Performing Interval

You are given an array hours representing the number of hours worked per day by an employee.

- A day is considered a tiring day if the number of hours worked is strictly greater than 8.
- A well-performing interval is a contiguous subarray where the count of tiring days is strictly
  greater than the count of non-tiring days.

Determine the length of the longest well-performing interval within the hours array.

Example:
Input: hours = [9, 9, 6, 0, 6, 6, 9]
Output: 3

Explanation: The longest well-performing interval is [9, 9, 6], which has a length of 3.

Constraints:
- 1 <= hours.length <= 10^4
- 0 <= hours[i] <= 16
"""

from typing import List
import pytest


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        pass


@pytest.mark.parametrize(
    "hours, expected",
    [
        ([9, 9, 6, 0, 6, 6, 9], 3),
        ([6, 6, 9], 1),
        ([9, 9, 9], 3),
        ([6, 6, 6], 0),
    ],
)
def test_longest_wpi(hours, expected):
    s = Solution()
    result = s.longestWPI(hours)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
