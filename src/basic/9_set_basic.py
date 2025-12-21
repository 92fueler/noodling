"""
Set Basics

1. create & copy - literals, from iterables, comprehensions, copy
2. modify - add, remove, discard, pop, clear, update
3. access & iterate - membership, iteration, comprehensions
4. set operations - union, intersection, difference, symmetric difference
5. checks - empty, subset/superset, disjoint, equality
6. patterns & idioms - deduplication, set comprehensions, common leetcode patterns
"""

# ============================================================================
# 1. CREATE & COPY
# ============================================================================
s = set()  # empty set
s = {1, 2, 3}  # literal
s = set([1, 2, 3])  # from list
s = set((1, 2, 3))  # from tuple
s = set("hello")  # from string: {'h', 'e', 'l', 'o'}
s = set(range(5))  # from range: {0, 1, 2, 3, 4}

# Comprehensions
s = {x for x in range(5)}  # {0, 1, 2, 3, 4}
s = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}
s = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}

# From dict (keys)
d = {"a": 1, "b": 2, "c": 3}
s = set(d)  # {'a', 'b', 'c'} - keys only
s = set(d.keys())  # same as above
s = set(d.values())  # {1, 2, 3} - values

# Copy
original = {1, 2, 3}
s = original.copy()  # shallow copy
s = set(original)  # constructor copy
import copy

s = copy.deepcopy(original)  # deep copy (for nested sets)

# ============================================================================
# 2. MODIFY
# ============================================================================
s = {1, 2, 3}

# Add
s.add(4)  # {1, 2, 3, 4}
s.add(2)  # {1, 2, 3, 4} - no duplicate

# Remove / Discard
s.remove(2)  # {1, 3, 4} - raises KeyError if not found
s.discard(5)  # {1, 3, 4} - no error if not found
s.discard(3)  # {1, 4}

# Pop (remove and return arbitrary element)
value = s.pop()  # removes and returns one element
value = s.pop() if s else None  # safe pop

# Update (add multiple elements)
s = {1, 2}
s.update([3, 4, 5])  # {1, 2, 3, 4, 5} - from list
s.update((6, 7))  # {1, 2, 3, 4, 5, 6, 7} - from tuple
s.update({8, 9})  # {1, 2, 3, 4, 5, 6, 7, 8, 9} - from set
s |= {10, 11}  # same as update

# Clear
s.clear()  # set()
s = set()  # reassign to empty

# ============================================================================
# 3. ACCESS & ITERATE
# ============================================================================
s = {1, 2, 3, 4, 5}

# Membership check (O(1) average)
3 in s  # True
10 not in s  # True

# Iterate (order is arbitrary in Python < 3.7, insertion order in 3.7+)
for item in s:
    pass
for item in sorted(s):
    pass  # iterate in sorted order

# Comprehensions
doubled = {x * 2 for x in s}  # {2, 4, 6, 8, 10}
filtered = {x for x in s if x % 2 == 0}  # {2, 4}

# Convert to list/tuple (preserves order in Python 3.7+)
lst = list(s)  # [1, 2, 3, 4, 5] (order may vary < 3.7)
tup = tuple(s)  # (1, 2, 3, 4, 5)

# ============================================================================
# 4. SET OPERATIONS
# ============================================================================
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (elements in either set)
a | b  # {1, 2, 3, 4, 5, 6}
a.union(b)  # same as above
a |= b  # in-place union (modifies a)

# Intersection (elements in both sets)
a & b  # {3, 4}
a.intersection(b)  # same as above
a &= b  # in-place intersection

# Difference (elements in a but not in b)
a - b  # {1, 2}
a.difference(b)  # same as above
a -= b  # in-place difference

# Symmetric Difference (elements in either set, but not both)
a ^ b  # {1, 2, 5, 6}
a.symmetric_difference(b)  # same as above
a ^= b  # in-place symmetric difference

# Multiple sets
a = {1, 2, 3}
b = {2, 3, 4}
c = {3, 4, 5}
a.union(b, c)  # {1, 2, 3, 4, 5}
a.intersection(b, c)  # {3}
a.difference(b, c)  # {1} - elements in a but not in b or c

# ============================================================================
# 5. CHECKS
# ============================================================================
a = {1, 2, 3}
b = {2, 3}
c = {4, 5}

# Empty check
if not a:
    pass  # empty check
if a:
    pass  # non-empty check
len(a)  # 3

# Subset / Superset
b.issubset(a)  # True - b is subset of a
a.issuperset(b)  # True - a is superset of b
b <= a  # True - subset (operator)
a >= b  # True - superset (operator)
b < a  # True - proper subset
a > b  # True - proper superset

# Disjoint (no common elements)
a.isdisjoint(c)  # True - no common elements
a.isdisjoint(b)  # False - has common elements

# Equality
a == {1, 2, 3}  # True - order doesn't matter
a == {3, 2, 1}  # True - same elements

# ============================================================================
# 6. PATTERNS & IDIOMS
# ============================================================================
# Deduplication (preserve order in Python 3.7+)
lst = [1, 2, 2, 3, 3, 3, 4]
unique = list(dict.fromkeys(lst))  # [1, 2, 3, 4] - preserves order
unique = list(set(lst))  # [1, 2, 3, 4] - may not preserve order

# Find unique elements
lst = [1, 2, 2, 3, 3, 3]
unique = set(lst)  # {1, 2, 3}

# Find duplicates
lst = [1, 2, 2, 3, 3, 3, 4]
seen = set()
duplicates = {x for x in lst if x in seen or seen.add(x)}  # {2, 3}

# Find common elements between lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)  # {3, 4}

# Find elements in one list but not the other
only_in_list1 = set(list1) - set(list2)  # {1, 2}
only_in_list2 = set(list2) - set(list1)  # {5, 6}

# Check if all elements are unique
lst = [1, 2, 3, 4]
all_unique = len(lst) == len(set(lst))  # True

# Count distinct elements
distinct_count = len(set(lst))  # 4

# Set comprehension with condition
evens = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}

# Frozen set (immutable set)
fs = frozenset([1, 2, 3])  # immutable, hashable
# fs.add(4)                                  # AttributeError - cannot modify
# Can be used as dict key or set element
d = {fs: "value"}  # valid
s = {fs}  # valid

# Leetcode pattern: Two sets for tracking
visited = set()  # track visited nodes/elements
seen = set()  # track seen elements

# Leetcode pattern: Set for O(1) lookup
# Instead of: if x in list:  # O(n)
# Use: if x in set:  # O(1)
lookup_set = set([1, 2, 3, 4, 5])
if 3 in lookup_set:
    pass  # O(1) lookup

# Leetcode pattern: Set intersection for common elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)  # {3, 4}

# Leetcode pattern: Set difference for missing elements
full_set = {1, 2, 3, 4, 5}
partial_set = {2, 4}
missing = full_set - partial_set  # {1, 3, 5}

# Leetcode pattern: Character set operations
s1 = set("hello")  # {'h', 'e', 'l', 'o'}
s2 = set("world")  # {'w', 'o', 'r', 'l', 'd'}
common_chars = s1 & s2  # {'l', 'o'}
unique_to_s1 = s1 - s2  # {'h', 'e'}
unique_to_s2 = s2 - s1  # {'w', 'r', 'd'}
