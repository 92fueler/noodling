"""
Linked List Basics - CRUD Operations

1. create - node class, create list from array, create empty
2. read - traverse, access by index, find node, get length
3. update - modify value, insert at position, append/prepend
4. delete - remove by value, remove at index, clear list
"""


# ============================================================================
# NODE DEFINITION
# ============================================================================
class ListNode:
    """Singly linked list node."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class DoublyListNode:
    """Doubly linked list node."""

    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


# ============================================================================
# 1. CREATE
# ============================================================================
# Create single node
node = ListNode(1)


# Create list from array
def create_list(arr: list) -> ListNode | None:
    """Create linked list from array."""
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


# Create list from array (recursive)
def create_list_recursive(arr: list, idx: int = 0) -> ListNode | None:
    """Create linked list recursively."""
    if idx >= len(arr):
        return None
    node = ListNode(arr[idx])
    node.next = create_list_recursive(arr, idx + 1)
    return node


# Create empty list
head = None


# ============================================================================
# 2. READ
# ============================================================================
# Traverse and print
def traverse(head: ListNode | None):
    """Traverse and print all nodes."""
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next


# Convert to array
def to_array(head: ListNode | None) -> list:
    """Convert linked list to array."""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


# Get length
def get_length(head: ListNode | None) -> int:
    """Get length of linked list."""
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    return length


# Access by index (0-based)
def get_node_at_index(head: ListNode | None, index: int) -> ListNode | None:
    """Get node at specific index."""
    curr = head
    for _ in range(index):
        if not curr:
            return None
        curr = curr.next
    return curr


# Find node by value
def find_node(head: ListNode | None, target: int) -> ListNode | None:
    """Find first node with given value."""
    curr = head
    while curr:
        if curr.val == target:
            return curr
        curr = curr.next
    return None


# Get middle node (two pointers)
def get_middle(head: ListNode | None) -> ListNode | None:
    """Get middle node using two pointers."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# Get last node
def get_last(head: ListNode | None) -> ListNode | None:
    """Get last node."""
    if not head:
        return None
    curr = head
    while curr.next:
        curr = curr.next
    return curr


# ============================================================================
# 3. UPDATE
# ============================================================================
# Modify value at index
def update_at_index(head: ListNode | None, index: int, value: int) -> bool:
    """Update value at specific index."""
    node = get_node_at_index(head, index)
    if node:
        node.val = value
        return True
    return False


# Insert at beginning (prepend)
def prepend(head: ListNode | None, value: int) -> ListNode:
    """Insert node at beginning."""
    new_node = ListNode(value)
    new_node.next = head
    return new_node  # new head


# Insert at end (append)
def append(head: ListNode | None, value: int) -> ListNode:
    """Insert node at end."""
    new_node = ListNode(value)
    if not head:
        return new_node
    last = get_last(head)
    last.next = new_node
    return head


# Insert at index
def insert_at_index(head: ListNode | None, index: int, value: int) -> ListNode:
    """Insert node at specific index."""
    if index == 0:
        return prepend(head, value)

    prev = get_node_at_index(head, index - 1)
    if not prev:
        return head  # index out of bounds

    new_node = ListNode(value)
    new_node.next = prev.next
    prev.next = new_node
    return head


# Insert after node
def insert_after(prev_node: ListNode, value: int):
    """Insert node after given node."""
    if not prev_node:
        return
    new_node = ListNode(value)
    new_node.next = prev_node.next
    prev_node.next = new_node


# Insert in sorted order
def insert_sorted(head: ListNode | None, value: int) -> ListNode:
    """Insert node in sorted linked list."""
    new_node = ListNode(value)

    # Insert at beginning
    if not head or head.val >= value:
        new_node.next = head
        return new_node

    # Find insertion point
    curr = head
    while curr.next and curr.next.val < value:
        curr = curr.next

    new_node.next = curr.next
    curr.next = new_node
    return head


# ============================================================================
# 4. DELETE
# ============================================================================
# Delete by value (first occurrence)
def delete_by_value(head: ListNode | None, value: int) -> ListNode | None:
    """Delete first node with given value."""
    if not head:
        return None

    # If head is the target
    if head.val == value:
        return head.next

    # Find and delete
    curr = head
    while curr.next:
        if curr.next.val == value:
            curr.next = curr.next.next
            return head
        curr = curr.next

    return head


# Delete at index
def delete_at_index(head: ListNode | None, index: int) -> ListNode | None:
    """Delete node at specific index."""
    if not head:
        return None

    if index == 0:
        return head.next

    prev = get_node_at_index(head, index - 1)
    if not prev or not prev.next:
        return head  # index out of bounds

    prev.next = prev.next.next
    return head


# Delete all occurrences of value
def delete_all_occurrences(head: ListNode | None, value: int) -> ListNode | None:
    """Delete all nodes with given value."""
    # Remove all from beginning
    while head and head.val == value:
        head = head.next

    if not head:
        return None

    # Remove from middle/end
    curr = head
    while curr.next:
        if curr.next.val == value:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head


# Clear list
def clear_list(head: ListNode | None) -> None:
    """Clear entire list."""
    curr = head
    while curr:
        next_node = curr.next
        curr.next = None
        curr = next_node


# Delete node (given only that node - no head)
def delete_node(node: ListNode):
    """Delete node when only given that node (copy next value)."""
    if node and node.next:
        node.val = node.next.val
        node.next = node.next.next


# ============================================================================
# COMMON PATTERNS
# ============================================================================
# Reverse list
def reverse(head: ListNode | None) -> ListNode | None:
    """Reverse linked list iteratively."""
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


# Reverse list recursively
def reverse_recursive(head: ListNode | None) -> ListNode | None:
    """Reverse linked list recursively."""
    if not head or not head.next:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


# Check if cycle exists
def has_cycle(head: ListNode | None) -> bool:
    """Check if linked list has cycle (Floyd's algorithm)."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Find cycle start
def find_cycle_start(head: ListNode | None) -> ListNode | None:
    """Find start of cycle if exists."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Move slow to head and move both one step
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None


# Merge two sorted lists
def merge_sorted(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """Merge two sorted linked lists."""
    dummy = ListNode(0)
    curr = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    curr.next = list1 or list2
    return dummy.next


# Split list into two halves
def split_list(head: ListNode | None) -> tuple[ListNode | None, ListNode | None]:
    """Split list into two halves."""
    if not head:
        return None, None

    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None
    return head, second
