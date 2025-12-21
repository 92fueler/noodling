"""
List Basics

1. create & copy - literals, comprehensions, from iterables, shallow/deep copy
2. modify - append/pop, insert/remove, extend, reverse, sort, dedup
3. access - indexing, slicing, safe access, first/last
4. search - index, find with predicate, binary search
5. checks - empty, contains, all/any, min/max, sum/product, sorted
6. iterate - for loops, enumerate, zip, pairwise, chunks, window
7. patterns - comprehensions, unpacking, swap, rotate, partition
"""

# ============================================================================
# 1. CREATE & COPY
# ============================================================================
lst = []  # empty
lst = [1, 2, 3]  # literal
lst = list(range(10))  # from iterable
lst = [0] * 5  # repeat: [0, 0, 0, 0, 0]
lst = [i * 2 for i in range(5)]  # comprehension: [0, 2, 4, 6, 8]

# 2D matrix
matrix = [[0] * 3 for _ in range(3)]  # 3x3 matrix (use for _ not [0]*3)

# From other collections
lst = list("hello")  # from string
lst = list({1, 2, 3})  # from set
lst = list((1, 2, 3))  # from tuple

# Copy
original = [1, 2, 3]
lst = original.copy()  # shallow copy
lst = original[:]  # slice copy
lst = list(original)  # constructor copy
import copy

lst = copy.deepcopy(original)  # deep copy (for nested)

# ============================================================================
# 2. MODIFY
# ============================================================================
# Append / Pop
lst = [1, 2, 3]
lst.append(4)  # [1, 2, 3, 4] - O(1)
lst.pop()  # 4, lst = [1, 2, 3] - O(1)
lst.pop(0)  # 1, lst = [2, 3] - O(n)
value = lst.pop() if lst else None  # safe pop

# Insert / Remove
lst = [1, 2, 4, 5]
lst.insert(2, 3)  # [1, 2, 3, 4, 5] - O(n)
lst.remove(3)  # [1, 2, 4, 5] - O(n), removes first
del lst[2]  # remove by index

# Extend / Concat
lst = [1, 2, 3]
lst.extend([4, 5, 6])  # [1, 2, 3, 4, 5, 6] - in-place
lst += [7, 8]  # in-place extend
lst = lst + [9, 10]  # creates new list

# Reverse
lst.reverse()  # in-place
lst = lst[::-1]  # creates new list
lst = list(reversed(lst))  # using reversed()

# Sort
lst = [3, 1, 4, 1, 5, 9]
lst.sort()  # [1, 1, 3, 4, 5, 9] - in-place
lst = sorted(lst)  # creates new sorted list
lst.sort(reverse=True)  # descending
lst.sort(key=lambda x: -x)  # custom key
people = [("Alice", 30), ("Bob", 25)]
people.sort(key=lambda x: (x[1], x[0]))  # by age, then name

# Dedup (remove duplicates)
lst = [1, 2, 2, 3, 3, 3, 4]
lst = list(dict.fromkeys(lst))  # [1, 2, 3, 4] - preserves order
lst = list(set(lst))  # may not preserve order

# Clear / Truncate
lst.clear()  # []
lst = []  # reassign
lst = lst[:3]  # truncate (creates new)
del lst[3:]  # truncate in-place

# ============================================================================
# 3. ACCESS
# ============================================================================
lst = [1, 2, 3, 4, 5]

# Indexing
lst[0], lst[-1]  # first, last
lst[1:4], lst[:3], lst[2:], lst[::2], lst[::-1]  # slicing

# Safe access
idx = 2
value = lst[idx] if 0 <= idx < len(lst) else None
first = lst[0] if lst else None
last = lst[-1] if lst else None

# Split
left, right = lst[:2], lst[2:]  # [1, 2], [3, 4, 5]

# ============================================================================
# 4. SEARCH
# ============================================================================
lst = [1, 2, 3, 4, 5, 3, 2, 1]

# Find index
try:
    idx = lst.index(3)  # 2 - first occurrence
except ValueError:
    idx = None

# Find with predicate
idx = next((i for i, x in enumerate(lst) if x > 3), None)  # 4

# Binary search (sorted list)
import bisect

sorted_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
idx = bisect.bisect_left(sorted_lst, 5)  # 4 - insert position
if idx < len(sorted_lst) and sorted_lst[idx] == 5:
    print(f"Found at {idx}")

# Find all indices
indices = [i for i, x in enumerate(lst) if x == 3]  # [2, 5]

# ============================================================================
# 5. CHECKS
# ============================================================================
lst = [1, 2, 3, 4, 5]

# Empty / Length
if not lst:
    pass  # empty check
if lst:
    pass  # non-empty check
len(lst)  # 5

# Contains
3 in lst  # True
10 not in lst  # True

# All / Any
all(x % 2 == 0 for x in [2, 4, 6])  # True
any(x % 2 == 1 for x in [2, 4, 6])  # False
all(x == lst[0] for x in lst) if lst else True  # all same

# Sorted check
is_sorted = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
is_sorted = lst == sorted(lst)

# Count / Min / Max / Sum
lst.count(3)  # count occurrences
min(lst), max(lst)  # 1, 5
min(lst, default=None)  # safe min
sum(lst)  # 15
from math import prod

prod(lst)  # 120 (Python 3.8+)

# ============================================================================
# 6. ITERATE
# ============================================================================
lst = [1, 2, 3, 4, 5]

# Basic
for item in lst:
    pass
for i, item in enumerate(lst):
    pass  # with index
for i, item in enumerate(lst, start=1):
    pass  # start from 1

# Reverse
for item in reversed(lst):
    pass

# Multiple lists
lst1, lst2 = [1, 2, 3], ["a", "b", "c"]
for num, char in zip(lst1, lst2):
    pass  # pairs

# Pairwise (sliding window of 2)
from itertools import pairwise

for curr, next_val in pairwise(lst):
    pass  # (1,2), (2,3), (3,4), (4,5)


# Chunks
def chunks(lst, n):
    return [lst[i : i + n] for i in range(0, len(lst), n)]


chunks([1, 2, 3, 4, 5], 2)  # [[1, 2], [3, 4], [5]]


# Window (sliding window of size n)
def window(lst, n):
    for i in range(len(lst) - n + 1):
        yield lst[i : i + n]


# ============================================================================
# 7. PATTERNS & IDIOMS
# ============================================================================
# Comprehensions (preferred)
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
pairs = [(x, y) for x in range(3) for y in range(3)]

# Flatten
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [item for row in matrix for item in row]

# Conditional in comprehension
result = [x if x > 0 else 0 for x in [-1, 2, -3, 4]]

# Map / Filter (functional style)
squares = list(map(lambda x: x**2, range(10)))
evens = list(filter(lambda x: x % 2 == 0, range(10)))

# Unpacking
first, *rest = [1, 2, 3, 4, 5]  # first=1, rest=[2,3,4,5]
first, *middle, last = [1, 2, 3, 4, 5]  # first=1, middle=[2,3,4], last=5

# Swap
i, j = 0, 1
lst[i], lst[j] = lst[j], lst[i]


# Rotate
def rotate(lst, n):
    if not lst:
        return lst
    n = n % len(lst)
    return lst[-n:] + lst[:-n]


rotate([1, 2, 3, 4, 5], 2)  # [4, 5, 1, 2, 3]


# Partition
def partition(lst, predicate):
    trues = [x for x in lst if predicate(x)]
    falses = [x for x in lst if not predicate(x)]
    return trues, falses


evens, odds = partition([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
