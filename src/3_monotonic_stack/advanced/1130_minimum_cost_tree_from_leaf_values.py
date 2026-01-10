"""
1130. Minimum Cost Tree From Leaf Values

Given an array arr of positive integers, consider all binary trees such that:

- Each node has either 0 or 2 children.
- The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
- The value of each non-leaf node is equal to the product of the largest leaf value in its left
  and right subtree, respectively.

Among all possible binary trees considered, return the smallest possible sum of the values of each
non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

Note: This problem requires an O(n) solution.

Example 1:
Input: arr = [6,2,4]
Output: 32
Explanation: There are two possible trees. The first has a non-leaf node sum of 36, and the second
has a non-leaf node sum of 32. The second tree has the smaller sum.

Example 2:
Input: arr = [4,11]
Output: 44

Constraints:
- 2 <= arr.length <= 40
- 1 <= arr[i] <= 15
- It is guaranteed that the answer fits into a 32-bit signed integer (i.e., it is less than 2^31).
"""

from typing import List
import pytest


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        pass


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([6, 2, 4], 32),
        ([4, 11], 44),
        ([1, 2, 3], 11),
    ],
)
def test_mct_from_leaf_values(arr, expected):
    s = Solution()
    result = s.mctFromLeafValues(arr)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
