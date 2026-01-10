"""
1019. Next Greater Node In Linked List

You are given the head of a linked list with n nodes.

For each node in the list, determine the value of the next greater node. Specifically, for each node,
find the value of the first node that appears after it and has a strictly larger value.

Return an integer array answer where answer[i] is the value of the next greater node of the i-th node
(1-indexed). If the i-th node does not have a next greater node, set answer[i] = 0.

Example 1:
Input: head = [2,1,5]
Output: [5,5,0]

Example 2:
Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]

Constraints:
- The number of nodes in the list is n.
- 1 <= n <= 10^4
- 1 <= Node.val <= 10^9
"""

from typing import List, Optional
import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    """Helper function to convert list to linked list"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Helper function to convert linked list to list"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        pass


@pytest.mark.parametrize(
    "head_list, expected",
    [
        ([2, 1, 5], [5, 5, 0]),
        ([2, 7, 4, 3, 5], [7, 0, 5, 5, 0]),
        ([1], [0]),
        ([1, 2, 3], [2, 3, 0]),
    ],
)
def test_next_larger_nodes(head_list, expected):
    s = Solution()
    head = list_to_linked_list(head_list)
    result = s.nextLargerNodes(head)
    assert result == expected, f"Expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
