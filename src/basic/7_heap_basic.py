"""
Heap Basics (using heapq)

1. basic operations - heapify, push, pop, pushpop, replace, nlargest/nsmallest
2. min heap vs max heap - heapq is min heap, max heap patterns
3. custom sorting - tuples, custom comparators, wrapper classes
4. common leetcode patterns - k largest/smallest, merge k lists, top k frequent, median
5. advanced patterns - sliding window, priority queue, multi-criteria sorting
6. gotchas & tips - heap invariant, heap size management, performance
"""

import heapq

# ============================================================================
# 1. BASIC OPERATIONS
# ============================================================================

# Create heap (heapq maintains min heap property)
heap = []  # empty heap (list)
heap = [3, 1, 4, 1, 5, 9, 2, 6]  # list (not yet a heap)

# Heapify (convert list to heap in-place) - O(n)
heapq.heapify(heap)  # [1, 1, 2, 3, 5, 9, 4, 6] - min heap

# Push (add element) - O(log n)
heapq.heappush(heap, 0)  # adds 0, maintains heap property

# Pop (remove and return smallest) - O(log n)
smallest = heapq.heappop(heap)  # 0, heap maintains min heap property

# Push then pop (more efficient than separate calls) - O(log n)
result = heapq.heappushpop(heap, 7)  # pushes 7, pops smallest, returns popped

# Pop then push (pops first, then pushes) - O(log n)
result = heapq.heapreplace(heap, 8)  # pops smallest, pushes 8, returns popped

# Peek smallest (without removing) - O(1)
smallest = heap[0]  # smallest element (root)

# N largest / N smallest (without modifying heap) - O(n log k)
heap = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(heap)
largest_3 = heapq.nlargest(3, heap)  # [9, 6, 5] - O(n log k)
smallest_3 = heapq.nsmallest(3, heap)  # [1, 1, 2] - O(n log k)

# ============================================================================
# 2. MIN HEAP VS MAX HEAP
# ============================================================================

# heapq is ALWAYS a min heap (smallest at root)
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heap[0]  # 2 (smallest)

# Max heap pattern: negate values
max_heap = []
heapq.heappush(max_heap, -5)  # push -5
heapq.heappush(max_heap, -2)  # push -2
heapq.heappush(max_heap, -8)  # push -8
largest = -heapq.heappop(max_heap)  # 8 (pop and negate)


# Max heap helper functions
def max_heappush(heap, item):
    heapq.heappush(heap, -item)


def max_heappop(heap):
    return -heapq.heappop(heap)


def max_heappushpop(heap, item):
    return -heapq.heappushpop(heap, -item)


# ============================================================================
# 3. CUSTOM SORTING
# ============================================================================

# Tuples: heapq compares tuples element by element
# Useful for: (priority, value) or (value, index) pairs

# Sort by first element (priority)
heap = []
heapq.heappush(heap, (3, "task3"))
heapq.heappush(heap, (1, "task1"))
heapq.heappush(heap, (2, "task2"))
heapq.heappop(heap)  # (1, "task1") - lowest priority first


# Sort by value (for custom objects)
class Task:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name

    def __lt__(self, other):  # required for heapq
        return self.priority < other.priority


heap = []
heapq.heappush(heap, Task(3, "task3"))
heapq.heappush(heap, Task(1, "task1"))
heapq.heappush(heap, Task(2, "task2"))
task = heapq.heappop(heap)  # Task(1, "task1")

# Multi-criteria sorting: (primary, secondary, value)
heap = []
heapq.heappush(heap, (1, 2, "a"))  # sort by first, then second
heapq.heappush(heap, (1, 1, "b"))
heapq.heappush(heap, (2, 1, "c"))
heapq.heappop(heap)  # (1, 1, "b") - tie broken by second

# Reverse order: negate the key
heap = []
heapq.heappush(heap, (-3, "task3"))  # -3 is "larger" than -1
heapq.heappush(heap, (-1, "task1"))
heapq.heappush(heap, (-2, "task2"))
heapq.heappop(heap)  # (-3, "task3") - highest priority first

# ============================================================================
# 4. COMMON LEETCODE PATTERNS
# ============================================================================


# Pattern 1: K Largest Elements
def k_largest(nums, k):
    """Find k largest elements - O(n log k)"""
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)  # maintain size k
        elif num > heap[0]:
            heapq.heapreplace(heap, num)  # replace smallest if larger
    return heap  # returns k largest (unsorted)


# Pattern 2: K Smallest Elements
def k_smallest(nums, k):
    """Find k smallest elements - O(n log k)"""
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, -num)  # max heap (negate)
        elif num < -heap[0]:
            heapq.heapreplace(heap, -num)
    return [-x for x in heap]  # return positive values


# Pattern 3: Top K Frequent Elements
def top_k_frequent(nums, k):
    """Top k frequent elements - O(n log k)"""
    from collections import Counter

    counter = Counter(nums)
    heap = []
    for num, freq in counter.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, num))  # min heap by frequency
        elif freq > heap[0][0]:
            heapq.heapreplace(heap, (freq, num))
    return [num for _, num in heap]  # return elements


# Pattern 4: Merge K Sorted Lists
def merge_k_sorted(lists):
    """Merge k sorted lists - O(n log k)"""
    heap = []
    # Push first element from each list with list index and element index
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        # Push next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            heapq.heappush(
                heap, (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1)
            )
    return result


# Pattern 5: Find Median (two heaps)
class MedianFinder:
    """Find median using two heaps - O(log n) add, O(1) find"""

    def __init__(self):
        self.small = []  # max heap (negate values)
        self.large = []  # min heap

    def add_num(self, num):
        heapq.heappush(self.small, -num)  # add to max heap
        # Balance: move largest from small to large
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # Balance sizes: keep difference <= 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2


# Pattern 6: K Closest Points to Origin
def k_closest(points, k):
    """K closest points to origin - O(n log k)"""

    def distance_sq(point):
        return point[0] ** 2 + point[1] ** 2

    heap = []
    for point in points:
        dist_sq = distance_sq(point)
        if len(heap) < k:
            heapq.heappush(heap, (-dist_sq, point))  # max heap (negate)
        elif dist_sq < -heap[0][0]:
            heapq.heapreplace(heap, (-dist_sq, point))
    return [point for _, point in heap]


# Pattern 7: Meeting Rooms / Scheduling
def min_meeting_rooms(intervals):
    """Minimum meeting rooms needed - O(n log n)"""
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])  # sort by start time
    heap = []  # stores end times
    heapq.heappush(heap, intervals[0][1])
    for start, end in intervals[1:]:
        if start >= heap[0]:  # room available
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    return len(heap)


# ============================================================================
# 5. ADVANCED PATTERNS
# ============================================================================


# Pattern 8: Sliding Window Maximum (using heap)
def sliding_window_maximum(nums, k):
    """Maximum in each sliding window - O(n log n)"""
    if not nums:
        return []
    result = []
    heap = []
    # Initialize first window
    for i in range(k):
        heapq.heappush(heap, (-nums[i], i))  # max heap with index
    result.append(-heap[0][0])
    # Slide window
    for i in range(k, len(nums)):
        heapq.heappush(heap, (-nums[i], i))
        # Remove elements outside window
        while heap[0][1] <= i - k:
            heapq.heappop(heap)
        result.append(-heap[0][0])
    return result


# Pattern 9: Priority Queue with Update
class PriorityQueue:
    """Priority queue with ability to update priorities"""

    def __init__(self):
        self.heap = []
        self.entry_finder = {}  # maps item to [priority, item]
        self.REMOVED = "<removed>"  # placeholder for removed items
        self.counter = 0  # unique sequence count

    def add(self, item, priority=0):
        """Add or update item with priority"""
        if item in self.entry_finder:
            self.remove(item)
        entry = [priority, self.counter, item]
        self.entry_finder[item] = entry
        heapq.heappush(self.heap, entry)
        self.counter += 1

    def remove(self, item):
        """Mark item as removed"""
        entry = self.entry_finder.pop(item)
        entry[-1] = self.REMOVED

    def pop(self):
        """Pop smallest priority item"""
        while self.heap:
            priority, count, item = heapq.heappop(self.heap)
            if item is not self.REMOVED:
                del self.entry_finder[item]
                return item
        raise KeyError("pop from empty priority queue")

    def peek(self):
        """Peek smallest priority item"""
        while self.heap and self.heap[0][-1] is self.REMOVED:
            heapq.heappop(self.heap)
        if self.heap:
            return self.heap[0][-1]
        raise KeyError("peek from empty priority queue")


# Pattern 10: Multi-level Priority
def process_tasks_by_priority(tasks):
    """Process tasks with multiple priority levels"""
    heap = []
    for task in tasks:
        # Priority: (urgency, importance, timestamp)
        heapq.heappush(heap, (task["urgency"], task["importance"], task["id"], task))

    processed = []
    while heap:
        _, _, _, task = heapq.heappop(heap)
        processed.append(task)
    return processed


# ============================================================================
# 6. GOTCHAS & TIPS
# ============================================================================

# Gotcha 1: List must be heapified before using as heap
lst = [3, 1, 4, 1, 5]
# heapq.heappop(lst)                        # WRONG - not a heap yet!
heapq.heapify(lst)  # CORRECT - heapify first
heapq.heappop(lst)  # Now it works

# Gotcha 2: Heap maintains min heap property, not sorted order
heap = [3, 1, 4, 1, 5]
heapq.heapify(heap)
# heap is NOT [1, 1, 3, 4, 5] - it's a heap structure
# To get sorted: [heapq.heappop(heap) for _ in range(len(heap))]

# Gotcha 3: Don't modify heap elements directly
heap = []
heapq.heappush(heap, [3, "a"])  # mutable list
heap[0][0] = 1  # BREAKS heap invariant!
# Use tuples instead (immutable)
heapq.heappush(heap, (3, "a"))  # safer

# Gotcha 4: Max heap requires negating values
# For max heap, always negate on push and pop
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -2)
largest = -heapq.heappop(max_heap)  # 5

# Tip 1: Use heappushpop/heapreplace for efficiency
# Instead of:
# heapq.heappush(heap, x)
# heapq.heappop(heap)
# Use:
# heapq.heappushpop(heap, x)               # more efficient

# Tip 2: Maintain fixed-size heap for K problems
heap = []
for num in nums:
    if len(heap) < k:
        heapq.heappush(heap, num)
    elif num > heap[0]:
        heapq.heapreplace(heap, num)  # maintains size k

# Tip 3: Use nlargest/nsmallest for one-time queries
# If you only need result once and don't need to maintain heap:
largest_3 = heapq.nlargest(3, nums)  # O(n log k), no heap needed


# Tip 4: For custom objects, implement __lt__ method
class Node:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val < other.val


# Tip 5: Use counter in tuple for stable sorting
# When priorities are equal, use counter to maintain insertion order
counter = 0
heap = []
heapq.heappush(heap, (priority, counter, item))
counter += 1

# Tip 6: Check heap size before popping
if heap:
    item = heapq.heappop(heap)
else:
    # handle empty heap
    pass

# Performance notes:
# - heapify: O(n) - faster than n pushes
# - push/pop: O(log n)
# - peek: O(1)
# - nlargest/nsmallest: O(n log k) where k is number requested
# - For K problems, maintain heap size k for O(n log k) instead of O(n log n)
