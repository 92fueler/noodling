"""
Dict Basics

1. create & copy - literals, from pairs/keys/values, comprehensions, copy
2. modify - add/update, delete, clear, setdefault, update
3. access - get, keys/values/items, safe access, default values
4. search & check - in operator, key existence, empty check
5. iterate - for loops, keys/values/items, enumerate, comprehensions
6. patterns & idioms - defaultdict, Counter, dict unpacking, merge
"""

# ============================================================================
# 1. CREATE & COPY
# ============================================================================
d = {}  # empty dict
d = {"a": 1, "b": 2, "c": 3}  # literal
d = dict()  # constructor
d = dict(a=1, b=2, c=3)  # keyword args
d = dict([("a", 1), ("b", 2)])  # from list of pairs
d = dict(zip(["a", "b"], [1, 2]))  # from keys and values

# Comprehensions
d = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
d = {k: v for k, v in [("a", 1), ("b", 2)] if v > 0}  # with condition

# From keys with default value
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)  # {"a": 0, "b": 0, "c": 0}
d = dict.fromkeys(keys)  # {"a": None, "b": None, "c": None}

# Copy
original = {"a": 1, "b": 2}
d = original.copy()  # shallow copy
d = dict(original)  # constructor copy
import copy

d = copy.deepcopy(original)  # deep copy (for nested)

# ============================================================================
# 2. MODIFY
# ============================================================================
d = {"a": 1, "b": 2}

# Add / Update
d["c"] = 3  # add new key
d["a"] = 10  # update existing
d.update({"d": 4, "e": 5})  # update multiple
d.update(a=10, b=20)  # update with kwargs

# Setdefault (add if key doesn't exist)
d.setdefault("f", 6)  # returns 6, adds if not exists
d.setdefault("a", 100)  # returns 10 (key exists, no change)

# Delete
del d["a"]  # delete key
value = d.pop("b")  # delete and return value
value = d.pop("x", None)  # delete with default if not found
d.popitem()  # remove and return (key, value) - LIFO (3.7+)

# Clear
d.clear()  # remove all items
d = {}  # reassign to empty

# ============================================================================
# 3. ACCESS
# ============================================================================
d = {"a": 1, "b": 2, "c": 3}

# Direct access
value = d["a"]  # 1
value = d["x"]  # KeyError if not found

# Safe access with get
value = d.get("a")  # 1
value = d.get("x")  # None if not found
value = d.get("x", 0)  # 0 (default) if not found

# Keys / Values / Items
keys = d.keys()  # dict_keys(['a', 'b', 'c'])
values = d.values()  # dict_values([1, 2, 3])
items = d.items()  # dict_items([('a', 1), ('b', 2), ('c', 3)])

# Convert to list (if needed)
list(d.keys())  # ['a', 'b', 'c']
list(d.values())  # [1, 2, 3]
list(d.items())  # [('a', 1), ('b', 2), ('c', 3)]

# ============================================================================
# 4. SEARCH & CHECK
# ============================================================================
d = {"a": 1, "b": 2, "c": 3}

# Key existence
"a" in d  # True
"x" not in d  # True

# Empty check
if not d:
    pass  # empty check
if d:
    pass  # non-empty check
len(d)  # 3

# Check if key exists (before access)
if "a" in d:
    value = d["a"]

# ============================================================================
# 5. ITERATE
# ============================================================================
d = {"a": 1, "b": 2, "c": 3}

# Over keys (default)
for key in d:  # iterate over keys
    print(key, d[key])

# Explicit keys / values / items
for key in d.keys():
    pass
for value in d.values():
    pass
for key, value in d.items():
    pass  # preferred for key-value pairs

# With enumerate
for i, key in enumerate(d):
    pass
for i, (key, value) in enumerate(d.items()):
    pass

# Comprehensions
{key: value * 2 for key, value in d.items()}  # transform values
{k: v for k, v in d.items() if v > 1}  # filter by value
{key: d[key] for key in d if key != "a"}  # filter by key

# ============================================================================
# 6. PATTERNS & IDIOMS
# ============================================================================
# Defaultdict (avoid KeyError, auto-create keys)
from collections import defaultdict

dd = defaultdict(int)  # default value is 0
dd["a"] += 1  # auto-creates "a": 0, then increments
dd = defaultdict(list)  # default value is []
dd["key"].append(1)  # auto-creates "key": []

# Counter (frequency counting)
from collections import Counter

counter = Counter(["a", "b", "a", "c"])  # Counter({'a': 2, 'b': 1, 'c': 1})
counter["a"]  # 2
counter["x"]  # 0 (doesn't raise KeyError)
counter.most_common(2)  # [('a', 2), ('b', 1)]

# Dict unpacking
d1, d2 = {"a": 1}, {"b": 2}
merged = {**d1, **d2}  # {"a": 1, "b": 2} - merge (Python 3.5+)
d1.update(d2)  # in-place merge

# ChainMap (search multiple dicts)
from collections import ChainMap

d1, d2 = {"a": 1}, {"b": 2}
chain = ChainMap(d1, d2)  # searches d1 first, then d2
chain["a"]  # 1 (from d1)
chain["b"]  # 2 (from d2)

# Invert dict (swap keys and values)
d = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in d.items()}  # {1: 'a', 2: 'b', 3: 'c'}
# Note: values must be unique for proper inversion

# Group by value
from collections import defaultdict

items = [("a", 1), ("b", 1), ("c", 2)]
grouped = defaultdict(list)
for key, value in items:
    grouped[value].append(key)  # {1: ['a', 'b'], 2: ['c']}

# Get key by value (first occurrence)
d = {"a": 1, "b": 2, "c": 1}
key = next((k for k, v in d.items() if v == 1), None)  # "a"
