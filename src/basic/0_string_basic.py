"""
String Basics

1. create & modify - literals, f-strings, join, concatenate, reverse, case
2. access & slicing - indexing, slice patterns, safe access
3. search & check - find/index, membership, prefix/suffix, type checks, count, validation
4. iterate - for loops, enumerate, comprehensions
5. transform - split/strip/join, replace, removeprefix/suffix, translate, regex
6. conversion - string ↔ list/bytes/numbers/sequences
7. patterns & idioms - join vs +=, unpacking, raw strings, common patterns
"""

# ============================================================================
# 1. CREATE & MODIFY
# ============================================================================
s = "hello"  # literal
s = str(42)  # from number
s = "".join(["h", "e", "l", "l", "o"])  # from iterable
s = "world" * 3  # repetition

# F-string formatting (preferred)
name, age = "Alice", 30
s = f"{name} is {age}"  # basic
num = 42
f"{num:05d}"  # "00042" (zero-pad)
f"{num:x}"  # hex
f"{num:b}"  # binary
f"{3.14159:.2f}"  # precision
f"{1000000:,}"  # thousands sep

# Concatenate (strings are immutable - create new strings!)
s = "hello" + "world"  # okay for few
s = " ".join(["hello", "world"])  # best for many (O(n) vs O(n²))

# Modify
s = f"{s[:5]}x{s[5:]}"  # insert at index 5
s = s[:-1]  # pop last char
idx = 2
s = f"{s[:idx]}{s[idx + 1 :]}"  # remove at idx
s = s[::-1]  # reverse

# Case transformations
s = "Hello World"
s.upper()  # "HELLO WORLD" - all uppercase
s.lower()  # "hello world" - all lowercase
s.capitalize()  # "Hello world" - first char uppercase, rest lowercase
s.title()  # "Hello World" - first char of each word uppercase
s.swapcase()  # "hELLO wORLD" - swap case of all characters

# ============================================================================
# 2. ACCESS & SLICING
# ============================================================================
s = "hello"
s[0], s[-1]  # first, last
s[1:4], s[:3], s[2:], s[::2], s[::-1]  # slice patterns
idx = 10
ch = s[idx] if idx < len(s) else None  # safe access

# ============================================================================
# 3. SEARCH & CHECK
# ============================================================================
s = "hello world"

# Search
s.find("world")  # returns -1 if not found
s.rfind("o")  # from right
s.index("world")  # raises ValueError if not found
"world" in s  # membership check (preferred)

# Checks
if s:
    pass  # truthiness (non-empty)
s.startswith("hel"), s.endswith("lo")  # prefix/suffix
s.isalpha(), s.isalnum(), s.isdigit()  # type checks
s.islower(), s.isupper(), s.isspace()  # case/whitespace
s.count("l")  # count occurrences
all(c.isdigit() for c in s)  # all digits validation

# ============================================================================
# 4. ITERATE
# ============================================================================
s = "hello"
for ch in s:
    pass  # over characters
for i, ch in enumerate(s):
    pass  # with index
[ch.upper() for ch in s]  # list comprehension
"".join(ch.upper() for ch in s)  # generator expression

# ============================================================================
# 5. TRANSFORM
# ============================================================================
# Split, strip, join (common pattern)
", ".join(word.strip() for word in s.split(","))

# Whitespace
s.strip(), s.lstrip(), s.rstrip()  # remove whitespace
s.strip(".,!?")  # remove specific chars

# Replace
s.replace("world", "python")  # all occurrences
s.replace("l", "L", 2)  # limit to 2

# Prefix/suffix removal (Python 3.9+)
s.removeprefix("hello ")
s.removesuffix(" world")

# Translation
trans = str.maketrans("aeiou", "12345")
"hello".translate(trans)  # "h2ll4"

# Regex
import re

# Basic regex syntax:
# \s = whitespace, \w = word char (letters/digits/_), \d = digit
# + = one or more, * = zero or more, ? = zero or one
# ^ = start, $ = end, . = any char (except newline)
re.sub(r"\s+", " ", s)  # normalize whitespace (\s+ = one or more spaces)
re.findall(r"\w+", s)  # extract words (\w+ = one or more word chars)
re.findall(r"\d+", s)  # extract numbers (\d+ = one or more digits)

# ============================================================================
# 6. CONVERSION
# ============================================================================
s = "hello"

# String ↔ List
list(s)  # ['h', 'e', 'l', 'l', 'o']
s.split(), "a,b,c".split(",")  # split to list
"".join(["h", "e", "l", "l", "o"])  # list to string
" ".join(["hello", "world"])  # join with separator

# String ↔ Numbers
int("12345"), float("3.14")  # parse numbers
[int(ch) for ch in "12345"]  # string digits to int list
[int(x) for x in "1,2,3".split(",")]  # delimited to int list
num = int(s) if s.isdigit() else None  # safe conversion

# String ↔ Bytes
s.encode(), s.encode("ascii")  # to bytes
b"hello".decode()  # from bytes

# String as sequence
set(s), tuple(s), sorted(s)  # to set/tuple/sorted list
"".join(sorted(s))  # sorted string

# ============================================================================
# 7. PATTERNS & IDIOMS
# ============================================================================
# String building (use join, not +=)
words = ["hello", "world"]
" ".join(words)  # ✅ O(n) - best for many strings
# result += word                          # ❌ O(n²) - avoid for many strings

# String unpacking
first, *middle, last = "hello"

# Raw strings (for regex, paths)
r"\n", r"C:\Users\name"

# Common pattern: remove all whitespace
"".join(s.split())  # split then join
