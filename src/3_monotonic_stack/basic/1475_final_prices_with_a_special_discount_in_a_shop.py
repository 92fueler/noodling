"""
1475. Final Prices With a Special Discount in a Shop

You are given an integer array prices where prices[i] is the price of the i-th item in a shop.

The shop offers a special discount: when you buy the i-th item, you receive a discount equal to
prices[j], where j is the smallest index such that j > i and prices[j] <= prices[i]. If no such
j exists, no discount is applied.

Return an integer array answer where answer[i] is the final price you will pay for the i-th item,
considering the special discount.

Example 1:
Input: prices = [8, 4, 6, 2, 3]
Output: [4, 2, 4, 2, 3]
Explanation:
- For item 0 with prices[0] = 8, the next item with a price less than or equal to 8 is at index 1
  (prices[1] = 4), so the final price is 8 - 4 = 4.
- For item 1 with prices[1] = 4, the next item with a price less than or equal to 4 is at index 3
  (prices[3] = 2), so the final price is 4 - 2 = 2.
- For item 2 with prices[2] = 6, the next item with a price less than or equal to 6 is at index 3
  (prices[3] = 2), so the final price is 6 - 2 = 4.
- For items 3 and 4, there are no subsequent items with a price less than or equal to their prices,
  so the final prices remain 2 and 3, respectively.

Example 2:
Input: prices = [1, 2, 3, 4, 5]
Output: [1, 2, 3, 4, 5]
Explanation: In this case, no item has a subsequent item with a price less than or equal to its own,
so no discounts are applied.

Example 3:
Input: prices = [10, 1, 1, 6]
Output: [9, 0, 1, 6]

Constraints:
- 1 <= prices.length <= 500
- 1 <= prices[i] <= 1000
"""

from typing import List
import pytest


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        pass


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([8, 4, 6, 2, 3], [4, 2, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([10, 1, 1, 6], [9, 0, 1, 6]),
        ([5], [5]),
        ([10, 5, 5, 5], [5, 0, 0, 5]),
    ],
)
def test_final_prices(prices, expected):
    s = Solution()
    result = s.finalPrices(prices)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
