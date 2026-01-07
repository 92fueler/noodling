"""
904. Fruit Into Baskets

You are visiting a farm that has a single row of fruit trees arranged from left to right.
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the i-th tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

- You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
- Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].

Constraints:
- 1 <= fruits.length <= 10^5
- 0 <= fruits[i] < fruits.length
"""

from typing import List
import pytest
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hash_map = defaultdict(int)

        left, right = 0, 0
        max_length = 0

        while right < len(fruits):
            hash_map[fruits[right]] += 1

            while len(hash_map) > 2:
                hash_map[fruits[left]] -= 1
                if hash_map[fruits[left]] == 0:
                    del hash_map[fruits[left]]
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length


@pytest.mark.parametrize(
    "fruits, expected",
    [
        ([1, 2, 1], 3),
        ([0, 1, 2, 2], 3),
        ([1, 2, 3, 2, 2], 4),
        ([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5),
        ([1, 1, 1, 1, 1], 5),
        ([1, 2, 3, 4, 5], 2),
    ],
)
def test_total_fruit(fruits, expected):
    """Parametrized tests for multiple cases"""
    sol = Solution()
    result = sol.totalFruit(fruits)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
