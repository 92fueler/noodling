"""
2841. Maximum Sum of Almost Unique Subarray

Problem Statement:
You are given an integer array nums and two integers m and k. You are allowed to
choose a subarray of size k from nums. The score of the chosen subarray is the
sum of its elements, but only if the subarray has at most m distinct elements.
Otherwise, the score is 0.

Return the maximum score you can get.

Example 1:
Input: nums = [2,6,7,3,1,7], m = 3, k = 4
Output: 13
Explanation: The four subarrays of size k = 4 are:
- [2,6,7,3] has 4 distinct elements, score = 0
- [6,7,3,1] has 4 distinct elements, score = 0
- [7,3,1,7] has 3 distinct elements, score = 18
- [3,1,7,7] has 3 distinct elements, score = 18
The maximum score is 18.

Example 2:
Input: nums = [5,9,9,2,4,5,4], m = 1, k = 3
Output: 23
Explanation: The subarray [9,9,2] has 2 distinct elements, score = 0.
The subarray [9,2,4] has 3 distinct elements, score = 0.
The subarray [2,4,5] has 3 distinct elements, score = 0.
The subarray [4,5,4] has 2 distinct elements, score = 0.
The subarray [5,4,5] has 2 distinct elements, score = 0.
The subarray [4,5,4] has 2 distinct elements, score = 0.
The maximum score is 0.

Note: The problem statement may vary. Some versions ask for subarray with at most
k distinct elements, while others ask for at most m distinct elements in a
subarray of length k.
"""

from typing import List
import pytest 


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        # Your code here
        pass

if __name__ == "__main__":
    pytest.main([__file__, "-v"])