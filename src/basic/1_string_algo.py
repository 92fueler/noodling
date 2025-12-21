"""
String patterns

1. two-pointer technique - palindrome, reverse, merge
2. character frequency counting - Counter, defaultdict, manual
3. sliding window - longest substring without repeats
4. string comparison - lexicographic, min/max
5. anagram grouping - group by sorted chars
6. longest common prefix - find common prefix
7. string matching & regex - pattern matching, normalization
8. string rotation - left/right cyclic shift
9. stack patterns - remove duplicates, valid parentheses
10. string to int - handle signs, whitespace, edge cases
11. character set manipulation - unique chars, sorted sets
12. string partitioning - split by delimiter
13. string ↔ char array - list conversion (LeetCode style)
14. common combinations - anagram check, palindrome clean, word reversal
"""

from collections import Counter, defaultdict

# ============================================================================
# 1. TWO-POINTER TECHNIQUE
# ============================================================================
# Use for: palindrome, reverse, merge, etc.


def is_palindrome_two_pointers(s: str) -> bool:
    """Check if string is palindrome using two pointers."""
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def reverse_string_inplace(s: list[str]) -> None:
    """Reverse string in-place (LeetCode style with list)."""
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# ============================================================================
# 2. CHARACTER FREQUENCY COUNTING
# ============================================================================
# Use for: anagrams, character counting, frequency analysis

s = "hello"

# Using Counter (most convenient)
char_count = Counter(s)  # Counter({'h': 1, 'e': 1, 'l': 2, 'o': 1})
char_count.get("x", 0)  # safe access, returns 0 if not found

# Manual counting
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Using defaultdict
freq = defaultdict(int)
for ch in s:
    freq[ch] += 1

# ============================================================================
# 3. SLIDING WINDOW PATTERN
# ============================================================================
# Use for: longest substring without repeating chars, substring problems


def longest_substring_no_repeat(s: str) -> int:
    """Find length of longest substring without repeating characters."""
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len


# ============================================================================
# 4. STRING COMPARISON
# ============================================================================
# Lexicographic comparison
"apple" < "banana"  # True
min(["dog", "cat", "bird"])  # "bird"
max(["dog", "cat", "bird"])  # "dog"

# ============================================================================
# 5. ANAGRAM GROUPING
# ============================================================================
# Use for: grouping anagrams, anagram detection


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Group strings by anagram."""
    groups = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))  # sorted chars as key
        groups[key].append(word)
    return list(groups.values())


# Example usage
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Result: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


# ============================================================================
# 6. LONGEST COMMON PREFIX
# ============================================================================
def longest_common_prefix(strs: list[str]) -> str:
    """Find longest common prefix among strings."""
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


# ============================================================================
# 7. STRING MATCHING & REGEX
# ============================================================================
import re

# Pattern matching
pattern = r"^a.*b$"  # starts with 'a', ends with 'b'
re.match(pattern, "acb")  # Match object or None

# Common patterns
re.sub(r"\s+", " ", s)  # normalize whitespace
re.findall(r"\w+", s)  # extract words
re.findall(r"\d+", s)  # extract numbers

# ============================================================================
# 8. STRING ROTATION / CYCLIC SHIFT
# ============================================================================
s = "abcdef"
k = 2

rotated_left = s[k:] + s[:k]  # "cdefab" (left rotate by k)
rotated_right = s[-k:] + s[:-k]  # "efabcd" (right rotate by k)

# ============================================================================
# 9. STACK PATTERNS
# ============================================================================
# Use for: remove duplicates, valid parentheses, nested structures


def remove_adjacent_duplicates(s: str) -> str:
    """Remove adjacent duplicate characters using stack."""
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)


def is_valid_parentheses(s: str) -> bool:
    """Check if parentheses are valid using stack."""
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for ch in s:
        if ch in mapping:
            if not stack or stack.pop() != mapping[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


# ============================================================================
# 10. STRING NUMBER CONVERSION (EDGE CASES)
# ============================================================================
def string_to_int(s: str) -> int:
    """Convert string to integer (handle edge cases)."""
    s = s.strip()
    if not s:
        return 0
    sign = -1 if s[0] == "-" else 1
    if s[0] in "+-":
        s = s[1:]
    num = 0
    for ch in s:
        if not ch.isdigit():
            break
        num = num * 10 + int(ch)
    return sign * num


# ============================================================================
# 11. CHARACTER SET MANIPULATION
# ============================================================================
s = "hello"

unique_chars = set(s)  # get unique characters
sorted_unique = "".join(sorted(set(s)))  # sorted unique chars as string

# ============================================================================
# 12. STRING PARTITIONING
# ============================================================================
# Split by delimiter
parts = s.split(" ")  # simple split


# Manual partitioning (more control)
def partition(s: str, delim: str) -> list[str]:
    """Partition string by delimiter manually."""
    result = []
    start = 0
    while True:
        idx = s.find(delim, start)
        if idx == -1:
            result.append(s[start:])
            break
        result.append(s[start:idx])
        start = idx + len(delim)
    return result


# ============================================================================
# 13. STRING TO/FROM CHAR ARRAY (LEETCODE STYLE)
# ============================================================================
s = "hello"
arr = list(s)  # ['h', 'e', 'l', 'l', 'o']
s = "".join(arr)  # "hello"

# ============================================================================
# 14. COMMON COMBINATIONS
# ============================================================================


# Check if two strings are anagrams
def is_anagram(s1: str, s2: str) -> bool:
    return Counter(s1) == Counter(s2)


# Check if string is palindrome (ignoring case, non-alphanumeric)
def is_palindrome_clean(s: str) -> bool:
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


# Word reversal in string
def reverse_words(s: str) -> str:
    return " ".join(s.split()[::-1])


# Simple palindrome check
def is_palindrome(s: str) -> bool:
    return s == s[::-1]


# Remove duplicates while preserving order
def remove_duplicates(s: str) -> str:
    return "".join(dict.fromkeys(s))


# Chunk string into n-sized pieces
def chunk_string(s: str, n: int) -> list[str]:
    return [s[i : i + n] for i in range(0, len(s), n)]
