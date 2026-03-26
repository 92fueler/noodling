"""
1 -> 2 -> 3

reverse a linked list
"""

from typing import Optional


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"LinkedList(val={self.val}->next={self.next})"


class Solution:
    def reverse_recursion(self, head: Optional[Node]):
        if not head or not head.next:
            return head

        # curr head: head
        new_head = self.reverse(head.next)

        # reverse
        head.next.next = head
        head.next = None

        return new_head

    def reverse_linear(self, head: Optional[Node]):
        if not head or not head.next:
            return head

        curr = head
        while curr:

        # reverse: prev, curr, next_node
        # curr.next = prev
        # prev = curr
        # curr = next_node




if __name__ == "__main__":

    s = Solution()
    head = Node(1, next=Node(2, next=Node(3, next=None)))
    print("head", head)
    result = s.reverse_recursion(head)

    print(result)
