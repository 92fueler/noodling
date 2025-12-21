"""
Tuple Basics

1. create & copy - literals, from iterables, comprehensions, unpacking
2. access - indexing, slicing, safe access, unpacking
3. modify - immutable (cannot modify), workarounds
4. operations - concatenation, repetition, membership, comparison
5. patterns & idioms - tuple unpacking, multiple return values, named tuples
"""

# ============================================================================
# 1. CREATE & COPY
# ============================================================================
# Tuples are immutable sequences

# Create tuple
t = ()  # empty tuple
t = (1,)  # single element (comma required!)
t = (1, 2, 3)  # multiple elements
t = 1, 2, 3  # parentheses optional (comma creates tuple)
t = tuple()  # empty tuple (constructor)
t = tuple([1, 2, 3])  # from list: (1, 2, 3)
t = tuple("hello")  # from string: ('h', 'e', 'l', 'l', 'o')
t = tuple({1, 2, 3})  # from set: (1, 2, 3) - order may vary
t = tuple(range(5))  # from range: (0, 1, 2, 3, 4)

# Comprehensions (generator expression, convert to tuple)
t = tuple(x * 2 for x in range(5))  # (0, 2, 4, 6, 8)
t = tuple(x for x in range(10) if x % 2 == 0)  # (0, 2, 4, 6, 8)

# From unpacking
t = (*[1, 2, 3],)  # (1, 2, 3) - unpacking with comma

# Copy (tuples are immutable, so copy is same reference)
original = (1, 2, 3)
t = original  # same reference (immutable, so safe)
t = tuple(original)  # constructor copy
t = original[:]  # slice copy

# ============================================================================
# 2. ACCESS
# ============================================================================
t = (1, 2, 3, 4, 5)

# Indexing
t[0]  # 1 (first)
t[-1]  # 5 (last)
t[2]  # 3 (by index)

# Slicing
t[1:4]  # (2, 3, 4)
t[:3]  # (1, 2, 3)
t[2:]  # (3, 4, 5)
t[::2]  # (1, 3, 5) - step 2
t[::-1]  # (5, 4, 3, 2, 1) - reverse

# Safe access
idx = 10
value = t[idx] if 0 <= idx < len(t) else None
first = t[0] if t else None
last = t[-1] if t else None

# Unpacking
a, b, c = (1, 2, 3)  # a=1, b=2, c=3
first, *rest = (1, 2, 3, 4, 5)  # first=1, rest=[2, 3, 4, 5]
first, *middle, last = (1, 2, 3, 4, 5)  # first=1, middle=[2, 3, 4], last=5
*a, b, c = (1, 2, 3, 4, 5)  # a=[1, 2, 3], b=4, c=5

# Multiple assignment (tuple unpacking)
x, y = 1, 2  # x=1, y=2
x, y = y, x  # swap: x=2, y=1

# ============================================================================
# 3. MODIFY (IMMUTABLE - WORKAROUNDS)
# ============================================================================
# Tuples are IMMUTABLE - cannot modify in place!

# t[0] = 10                                   # TypeError: 'tuple' object does not support item assignment
# t.append(6)                                 # AttributeError: 'tuple' object has no attribute 'append'

# Workaround: Create new tuple
t = (1, 2, 3)
t = t + (4,)  # (1, 2, 3, 4) - concatenation creates new tuple
t = (*t, 5)  # (1, 2, 3, 4, 5) - unpacking creates new tuple
t = t[:2] + (10,) + t[2:]  # (1, 2, 10, 3, 4, 5) - insert at index 2

# Convert to list, modify, convert back
t = (1, 2, 3)
lst = list(t)  # [1, 2, 3]
lst[0] = 10  # [10, 2, 3]
t = tuple(lst)  # (10, 2, 3)

# ============================================================================
# 4. OPERATIONS
# ============================================================================
t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation (creates new tuple)
t3 = t1 + t2  # (1, 2, 3, 4, 5, 6)
t3 = (*t1, *t2)  # same using unpacking

# Repetition
t = (1, 2) * 3  # (1, 2, 1, 2, 1, 2)

# Membership
3 in t1  # True
10 not in t1  # True

# Comparison (lexicographic)
(1, 2, 3) < (1, 2, 4)  # True
(1, 2) < (1, 2, 3)  # True (shorter is "less")
(2, 1) > (1, 2)  # True (2 > 1)

# Count occurrences
t = (1, 2, 2, 3, 2, 4)
t.count(2)  # 3

# Find index
t.index(2)  # 1 (first occurrence)
t.index(2, 2)  # 4 (starting from index 2)
# t.index(10)                                 # ValueError if not found

# Length
len(t)  # 6

# Min / Max
min(t)  # 1
max(t)  # 4

# Sum (if all numeric)
sum(t)  # 14

# ============================================================================
# 5. PATTERNS & IDIOMS
# ============================================================================


# Multiple return values (common pattern)
def get_name_age():
    return "Alice", 30  # returns tuple


name, age = get_name_age()  # unpack tuple
result = get_name_age()  # result = ("Alice", 30)


# Function with multiple return values
def divide_with_remainder(a: int, b: int) -> tuple[int, int]:
    """Return (quotient, remainder)."""
    return a // b, a % b


quotient, remainder = divide_with_remainder(10, 3)  # 3, 1

# Tuple as dictionary key (tuples are hashable if elements are hashable)
d = {}
d[(1, 2)] = "value"  # tuple as key
d[(3, 4)] = "another"
# d[([1, 2], 3)] = "error"                   # TypeError: unhashable type (list not hashable)

# Tuple of tuples (2D structure)
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
matrix[0][1]  # 2

# Named tuple (from collections - see stack_queue_basic.py)
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)  # Point(x=1, y=2)
p.x, p.y  # 1, 2

# Tuple unpacking in loops
pairs = [(1, "a"), (2, "b"), (3, "c")]
for num, char in pairs:  # unpack in loop
    pass

# Enumerate returns tuples
for i, value in enumerate([10, 20, 30]):  # i, value are unpacked from tuple
    pass

# Zip returns tuples
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
for num, char in zip(list1, list2):  # unpack tuples from zip
    pass

# Tuple comparison for sorting
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted(people)  # sorted by first element, then second
sorted(people, key=lambda x: x[1])  # sorted by age (second element)
sorted(people, key=lambda x: (x[1], x[0]))  # sorted by age, then name

# Tuple for fixed-size records
student = ("Alice", 25, "CS")  # name, age, major
name, age, major = student

# Immutable configuration
CONFIG = ("localhost", 8080, True)  # host, port, debug
HOST, PORT, DEBUG = CONFIG


# Tuple unpacking with * (Python 3.5+)
def func(a, b, c):
    return a + b + c


args = (1, 2, 3)
result = func(*args)  # unpack tuple as arguments


# Tuple unpacking in function definitions
def process_coordinates(x, y, z):
    return x + y + z


coords = (1, 2, 3)
result = process_coordinates(*coords)  # unpack as arguments

# Tuple for multiple assignments
a, b, c = 1, 2, 3  # multiple assignment
a, b = b, a  # swap (common idiom)

# Tuple comprehension alternative (generator + tuple)
squares = tuple(x**2 for x in range(5))  # (0, 1, 4, 9, 16)

# Tuple as immutable alternative to list
# Use tuple when: order matters, need hashable, want immutability
coordinates = (10, 20)  # immutable point
# Use list when: need to modify, need mutable sequence

# Tuple unpacking with ignore
data = (1, 2, 3, 4, 5)
first, _, third, *_ = data  # ignore second and rest
first, *_, last = data  # get first and last, ignore middle


# Tuple for function arguments (packing)
def sum_all(*args):
    return sum(args)


result = sum_all(1, 2, 3, 4)  # args = (1, 2, 3, 4)


# Tuple for keyword arguments (packing)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Alice", age=30)  # kwargs = {'name': 'Alice', 'age': 30}
