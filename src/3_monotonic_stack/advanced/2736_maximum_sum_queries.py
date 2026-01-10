"""
2736. Maximum Sum Queries

You are given two 0-indexed integer arrays nums1 and nums2, each of length n, and a 2D array queries
where queries[i] = [xi, yi].

For each query [xi, yi], determine the maximum value of nums1[j] + nums2[j] for all indices j
(where 0 <= j < n) that satisfy:
- nums1[j] >= xi
- nums2[j] >= yi

If no such index j exists, return -1 for that query.

Return an array answer where answer[i] is the result for the i-th query.

Example:
Input:
nums1 = [4, 3, 1, 2]
nums2 = [2, 4, 9, 5]
queries = [[4, 1], [1, 3], [2, 5]]

Output: [6, 10, 7]

Explanation:
- For the first query [4, 1], the valid index is j = 0 (since nums1[0] = 4 >= 4 and nums2[0] = 2 >= 1),
  yielding a sum of 4 + 2 = 6.
- For the second query [1, 3], the valid index is j = 2 (since nums1[2] = 1 >= 1 and nums2[2] = 9 >= 3),
  yielding a sum of 1 + 9 = 10.
- For the third query [2, 5], the valid index is j = 3 (since nums1[3] = 2 >= 2 and nums2[3] = 5 >= 5),
  yielding a sum of 2 + 5 = 7.

Constraints:
- nums1.length == nums2.length == n
- 1 <= n <= 10^5
- 1 <= nums1[i], nums2[i] <= 10^9
- 1 <= queries.length <= 10^5
- queries[i].length == 2
- 1 <= xi, yi <= 10^9
"""

from typing import List
import pytest


class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        pass


@pytest.mark.parametrize(
    "nums1, nums2, queries, expected",
    [
        ([4, 3, 1, 2], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]], [6, 10, 7]),
    ],
)
def test_maximum_sum_queries(nums1, nums2, queries, expected):
    s = Solution()
    result = s.maximumSumQueries(nums1, nums2, queries)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
