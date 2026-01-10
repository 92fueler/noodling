"""
901. Online Stock Span

Design an algorithm that collects daily price quotes for some stock and returns the span of that
stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting
from today and going backward) for which the stock price was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85],
then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

Implement the StockSpanner class:

- StockSpanner(): Initializes the object of the class.
- int next(int price): Returns the span of the stock's price given that today's price is price.

Example 1:
Input:
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output:
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation:
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2, because the last 2 prices (including today's price of 70)
                        // were less than or equal to today's price.
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75)
                        // were less than or equal to today's price.
stockSpanner.next(85);  // return 6

Constraints:
- 1 <= price <= 10^5
- At most 10^4 calls will be made to next per test case.
- There will be at most 150,000 calls to next across all test cases.
"""

import pytest


class StockSpanner:
    def __init__(self):
        pass

    def next(self, price: int) -> int:
        pass


@pytest.mark.parametrize(
    "operations, prices, expected",
    [
        (
            ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"],
            [None, 100, 80, 60, 70, 60, 75, 85],
            [None, 1, 1, 1, 2, 1, 4, 6],
        ),
        (
            ["StockSpanner", "next", "next", "next"],
            [None, 10, 20, 30],
            [None, 1, 2, 3],
        ),
        (
            ["StockSpanner", "next", "next", "next"],
            [None, 30, 20, 10],
            [None, 1, 1, 1],
        ),
    ],
)
def test_stock_spanner(operations, prices, expected):
    spanner = None
    results = []
    for op, price, exp in zip(operations, prices, expected):
        if op == "StockSpanner":
            spanner = StockSpanner()
            results.append(None)
        elif op == "next":
            result = spanner.next(price)
            results.append(result)
            assert result == exp, f"Expected {exp}, got {result} for price {price}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
