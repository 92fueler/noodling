"""
2024. Maximize the Confusion of an Exam

A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the i-th question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

- Change the answer to any question (i.e., set answerKey[i] to 'T' or 'F').

Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

Example 1:
Input: answerKey = "TTFF", k = 2
Output: 4
Explanation: We can replace both the 'F' with 'T' to make answerKey = "TTTT".
There are four consecutive 'T's.

Example 2:
Input: answerKey = "TFFT", k = 1
Output: 3
Explanation: We can replace the first 'F' with 'T' to make answerKey = "TTFT".
Alternatively, we can replace the second 'F' with 'T' to make answerKey = "TFTT".
In both cases, there are three consecutive 'T's.

Example 3:
Input: answerKey = "TTFTTFTT", k = 1
Output: 5
Explanation: We can replace the first 'F' with 'T' to make answerKey = "TTTTTFTT".
Alternatively, we can replace the second 'F' with 'T' to make answerKey = "TTFTTTTT".
In both cases, there are five consecutive 'T's.

Constraints:
- n == answerKey.length
- 1 <= n <= 5 * 10^4
- answerKey[i] is either 'T' or 'F'
- 1 <= k <= n
"""

import pytest


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # Your code here
        pass


@pytest.mark.parametrize(
    "answerKey, k, expected",
    [
        ("TTFF", 2, 4),
        ("TFFT", 1, 3),
        ("TTFTTFTT", 1, 5),
        ("T", 1, 1),
        ("FFFTTFTTFT", 3, 8),
    ],
)
def test_max_consecutive_answers(answerKey, k, expected):
    """Parametrized tests for multiple cases"""
    sol = Solution()
    result = sol.maxConsecutiveAnswers(answerKey, k)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
