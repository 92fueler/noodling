"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together
the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional
import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next

    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"


def list_to_linked_list(arr):
    """Helper function to convert list to linked list"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Helper function to convert linked list to list"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Base cases: if one list is empty, return the other
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # Recursive case: compare values and merge
        if list1.val <= list2.val:
            # list1's value is smaller or equal, so it should come first
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # list2's value is smaller, so it should come first
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5, 6]),
        ([1], [2, 3, 4], [1, 2, 3, 4]),
        ([2, 3, 4], [1], [1, 2, 3, 4]),
    ],
)
def test_merge_two_lists(list1, list2, expected):
    """Test cases for merging two sorted lists"""
    sol = Solution()
    l1 = list_to_linked_list(list1)
    l2 = list_to_linked_list(list2)
    result = sol.mergeTwoLists(l1, l2)
    result_list = linked_list_to_list(result)
    assert result_list == expected, f"Expected {expected}, got {result_list}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
