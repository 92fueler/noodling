"""
Stack, Queue & Deque Basics

1. stack - using list, LIFO operations, common patterns
2. queue - using deque, FIFO operations, BFS patterns
3. deque - double-ended queue, operations from both ends
4. collections module - namedtuple, OrderedDict, ChainMap
5. patterns & idioms - monotonic stack, queue patterns, sliding window
"""

from collections import deque, namedtuple, OrderedDict, ChainMap

# ============================================================================
# 1. STACK (using list - LIFO: Last In First Out)
# ============================================================================
# Stack operations: push (append), pop, peek (top)

# Create stack
stack = []  # empty stack
stack = [1, 2, 3]  # stack with elements

# Push (add to top) - O(1)
stack.append(4)  # [1, 2, 3, 4]
stack.append(5)  # [1, 2, 3, 4, 5]

# Pop (remove from top) - O(1)
top = stack.pop()  # 5, stack = [1, 2, 3, 4]
top = stack.pop() if stack else None  # safe pop

# Peek (view top without removing) - O(1)
top = stack[-1] if stack else None  # 4, stack unchanged
top = stack[len(stack) - 1] if stack else None  # alternative

# Check empty
if not stack:
    pass  # empty check
if stack:
    pass  # non-empty check
len(stack)  # 3

# Stack operations summary
# push: stack.append(item)      # add to end
# pop:  stack.pop()              # remove from end
# peek: stack[-1]                # view last element
# size: len(stack)               # get size
# empty: not stack               # check if empty

# ============================================================================
# 2. QUEUE (using deque - FIFO: First In First Out)
# ============================================================================
# Queue operations: enqueue (append), dequeue (popleft), peek (front)

# Create queue
queue = deque()  # empty queue
queue = deque([1, 2, 3])  # queue with elements

# Enqueue (add to rear/end) - O(1)
queue.append(4)  # deque([1, 2, 3, 4])
queue.append(5)  # deque([1, 2, 3, 4, 5])

# Dequeue (remove from front) - O(1)
front = queue.popleft()  # 1, queue = deque([2, 3, 4, 5])
front = queue.popleft() if queue else None  # safe dequeue

# Peek (view front without removing) - O(1)
front = queue[0] if queue else None  # 2, queue unchanged

# Check empty
if not queue:
    pass  # empty check
if queue:
    pass  # non-empty check
len(queue)  # 4

# Queue operations summary
# enqueue: queue.append(item)        # add to end
# dequeue: queue.popleft()           # remove from front
# peek:    queue[0]                  # view first element
# size:    len(queue)                # get size
# empty:   not queue                 # check if empty

# Note: Using list for queue is inefficient (pop(0) is O(n))
# Always use deque for queue operations!

# ============================================================================
# 3. DEQUE (double-ended queue)
# ============================================================================
# Deque operations: add/remove from both ends

# Create deque
dq = deque()  # empty deque
dq = deque([1, 2, 3])  # deque with elements
dq = deque([1, 2, 3], maxlen=5)  # deque with max size

# Add to right (end) - O(1)
dq.append(4)  # deque([1, 2, 3, 4])
dq.extend([5, 6])  # deque([1, 2, 3, 4, 5, 6])

# Add to left (front) - O(1)
dq.appendleft(0)  # deque([0, 1, 2, 3, 4, 5, 6])
dq.extendleft([-2, -1])  # deque([-1, -2, 0, 1, 2, 3, 4, 5, 6])
# Note: extendleft reverses order!

# Remove from right (end) - O(1)
right = dq.pop()  # 6, deque([-1, -2, 0, 1, 2, 3, 4, 5])
right = dq.pop() if dq else None  # safe pop

# Remove from left (front) - O(1)
left = dq.popleft()  # -1, deque([-2, 0, 1, 2, 3, 4, 5])
left = dq.popleft() if dq else None  # safe popleft

# Access elements
dq[0]  # -2 (front)
dq[-1]  # 5 (rear)
dq[2]  # 0 (index access)

# Rotate (circular shift)
dq.rotate(1)  # rotate right by 1: deque([5, -2, 0, 1, 2, 3, 4])
dq.rotate(-1)  # rotate left by 1: deque([-2, 0, 1, 2, 3, 4, 5])

# Clear
dq.clear()  # deque([])

# Maxlen (bounded deque)
bounded = deque(maxlen=3)
bounded.append(1)  # deque([1], maxlen=3)
bounded.append(2)  # deque([1, 2], maxlen=3)
bounded.append(3)  # deque([1, 2, 3], maxlen=3)
bounded.append(4)  # deque([2, 3, 4], maxlen=3) - 1 removed

# ============================================================================
# 4. COLLECTIONS MODULE
# ============================================================================

# NamedTuple (immutable, named fields)
Point = namedtuple("Point", ["x", "y"])
p1 = Point(1, 2)  # Point(x=1, y=2)
p1.x  # 1
p1.y  # 2
p1[0]  # 1 (index access)
p1[1]  # 2

# NamedTuple with defaults (Python 3.7+)
Person = namedtuple("Person", ["name", "age", "city"], defaults=["Unknown"])
p = Person("Alice", 30)  # Person(name='Alice', age=30, city='Unknown')

# OrderedDict (maintains insertion order - Python 3.7+ dicts are ordered by default)
# Still useful for: move_to_end, popitem with last=False
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

od.move_to_end("a")  # move 'a' to end
od.move_to_end("c", last=False)  # move 'c' to beginning
od.popitem(last=True)  # remove and return ('a', 1) - from end
od.popitem(last=False)  # remove and return ('c', 3) - from beginning

# ChainMap (search multiple dicts)
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
chain = ChainMap(d1, d2)  # searches d1 first, then d2
chain["a"]  # 1 (from d1)
chain["b"]  # 2 (from d1, first match)
chain["c"]  # 4 (from d2)
chain.maps  # [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]
chain.new_child({"d": 5})  # add new dict to front

# ============================================================================
# 5. PATTERNS & IDIOMS
# ============================================================================


# Stack pattern: Valid parentheses
def is_valid_parentheses(s: str) -> bool:
    """Check if parentheses are valid using stack."""
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack


# Stack pattern: Remove adjacent duplicates
def remove_adjacent_duplicates(s: str) -> str:
    """Remove adjacent duplicate characters using stack."""
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)


# Stack pattern: Monotonic stack (increasing)
def monotonic_increasing_stack(nums: list[int]) -> list[int]:
    """Maintain increasing order in stack."""
    stack = []
    for num in nums:
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)
    return stack


# Stack pattern: Next greater element
def next_greater_element(nums: list[int]) -> list[int]:
    """Find next greater element for each element."""
    stack = []
    result = [-1] * len(nums)
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result


# Queue pattern: BFS traversal
def bfs_with_queue(graph: dict, start: int) -> list[int]:
    """BFS traversal using queue."""
    visited = set()
    result = []
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


# Queue pattern: Level-order traversal
def level_order_traversal(root) -> list[list[int]]:
    """Level-order traversal using queue."""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result


# Deque pattern: Sliding window maximum
def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    """Find maximum in each sliding window of size k."""
    if not nums:
        return []

    dq = deque()  # store indices
    result = []

    for i in range(len(nums)):
        # Remove indices outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove indices with smaller values (maintain decreasing order)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Add to result when window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# Deque pattern: Palindrome checker
def is_palindrome_deque(s: str) -> bool:
    """Check if string is palindrome using deque."""
    dq = deque(s.lower())
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


# Stack + Queue: Implement stack using queues
class StackUsingQueues:
    """Implement stack using two queues."""

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """Push element onto stack."""
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        """Remove element from top of stack."""
        return self.q1.popleft()

    def top(self) -> int:
        """Get top element."""
        return self.q1[0]

    def empty(self) -> bool:
        """Check if stack is empty."""
        return not self.q1


# Queue + Stack: Implement queue using stacks
class QueueUsingStacks:
    """Implement queue using two stacks."""

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """Push element to rear of queue."""
        self.stack1.append(x)

    def pop(self) -> int:
        """Remove element from front of queue."""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        """Get front element."""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        """Check if queue is empty."""
        return not self.stack1 and not self.stack2


# Bounded queue pattern (using deque with maxlen)
def process_with_bounded_queue(items: list, max_size: int):
    """Process items with bounded queue."""
    queue = deque(maxlen=max_size)
    for item in items:
        queue.append(item)
        # Process queue when full
        if len(queue) == max_size:
            process_batch(list(queue))


def process_batch(batch: list):
    """Process a batch of items."""
    pass


# Priority queue pattern (using heap - see heap_basic.py)
# For priority queue, use heapq module (covered in heap_basic.py)
