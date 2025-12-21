"""
Set patterns

1. O(1) lookup optimization - replace list membership with set
2. duplicate detection - find duplicates, first duplicate, all duplicates
3. two sets pattern - find intersection, union, difference, symmetric difference
4. sliding window with set - track unique elements in window
5. visited tracking - DFS/BFS visited nodes, cycle detection
6. complement search - find missing elements, complement pairs
7. set operations for arrays - common elements, unique elements
8. character set operations - unique chars, anagram detection
9. set-based grouping - group by unique characteristics
10. set for validation - check constraints, validate conditions
"""

# ============================================================================
# 1. O(1) LOOKUP OPTIMIZATION
# ============================================================================
# Replace O(n) list membership with O(1) set membership


# Bad: O(n) lookup
def contains_slow(nums: list[int], target: int) -> bool:
    return target in nums  # O(n)


# Good: O(1) lookup
def contains_fast(nums: list[int], target: int) -> bool:
    lookup = set(nums)
    return target in lookup  # O(1)


# Find intersection efficiently
def find_intersection(list1: list[int], list2: list[int]) -> list[int]:
    """Find common elements between two lists."""
    set2 = set(list2)
    return [x for x in list1 if x in set2]  # O(n) instead of O(n*m)


# ============================================================================
# 2. DUPLICATE DETECTION
# ============================================================================
# Find if array contains duplicates
def has_duplicate(nums: list[int]) -> bool:
    """Check if array contains duplicates."""
    return len(nums) != len(set(nums))


# Find first duplicate
def find_first_duplicate(nums: list[int]) -> int | None:
    """Find first duplicate element."""
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None


# Find all duplicates
def find_all_duplicates(nums: list[int]) -> list[int]:
    """Find all duplicate elements."""
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)


# Find missing number (1 to n)
def find_missing_number(nums: list[int], n: int) -> int:
    """Find missing number in range [1, n]."""
    num_set = set(nums)
    for i in range(1, n + 1):
        if i not in num_set:
            return i
    return -1


# ============================================================================
# 3. TWO SETS PATTERN
# ============================================================================
# Find intersection of two arrays
def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    """Find intersection of two arrays."""
    return list(set(nums1) & set(nums2))


# Find union of two arrays
def union(nums1: list[int], nums2: list[int]) -> list[int]:
    """Find union of two arrays."""
    return list(set(nums1) | set(nums2))


# Find elements in nums1 but not in nums2
def difference(nums1: list[int], nums2: list[int]) -> list[int]:
    """Find elements in nums1 but not in nums2."""
    return list(set(nums1) - set(nums2))


# Find symmetric difference (elements in either but not both)
def symmetric_difference(nums1: list[int], nums2: list[int]) -> list[int]:
    """Find symmetric difference of two arrays."""
    return list(set(nums1) ^ set(nums2))


# ============================================================================
# 4. SLIDING WINDOW WITH SET
# ============================================================================
# Longest substring without repeating characters
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


# Check if array has duplicate in window of size k
def has_duplicate_in_window(nums: list[int], k: int) -> bool:
    """Check if there's duplicate in any window of size k."""
    window = set()
    for i, num in enumerate(nums):
        # Remove element leaving the window (if window is full)
        if i >= k:
            window.discard(nums[i - k])
        # Check for duplicate before adding
        if num in window:
            return True
        # Add current element to window
        window.add(num)
    return False


# Longest substring with at most k distinct characters
def longest_substring_k_distinct(s: str, k: int) -> int:
    """Find length of longest substring with at most k distinct chars."""
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        char_set.add(s[right])
        while len(char_set) > k:
            if s[left] not in s[left + 1 : right + 1]:
                char_set.remove(s[left])
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


# ============================================================================
# 5. VISITED TRACKING
# ============================================================================
# DFS with visited set
def dfs_with_visited(graph: dict, start: int) -> list[int]:
    """DFS traversal with visited set."""
    visited = set()
    result = []

    def dfs(node: int):
        if node in visited:
            return
        visited.add(node)
        result.append(node)
        for neighbor in graph.get(node, []):
            dfs(neighbor)

    dfs(start)
    return result


# BFS with visited set
def bfs_with_visited(graph: dict, start: int) -> list[int]:
    """BFS traversal with visited set."""
    from collections import deque

    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        result.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)

    return result


# Cycle detection in linked list (Floyd's algorithm uses two pointers, but set works too)
def has_cycle_set(head) -> bool:
    """Detect cycle in linked list using set."""
    visited = set()
    current = head
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    return False


# ============================================================================
# 6. COMPLEMENT SEARCH
# ============================================================================
# Two sum using set (complement search)
def two_sum_set(nums: list[int], target: int) -> list[int]:
    """Find two indices whose values sum to target using set."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# Find missing numbers in range
def find_missing_numbers(nums: list[int], n: int) -> list[int]:
    """Find all missing numbers in range [1, n]."""
    num_set = set(nums)
    return [i for i in range(1, n + 1) if i not in num_set]


# Find complement set
def find_complement_set(full_set: set[int], partial_set: set[int]) -> set[int]:
    """Find elements in full_set but not in partial_set."""
    return full_set - partial_set


# ============================================================================
# 7. SET OPERATIONS FOR ARRAYS
# ============================================================================
# Find common elements in multiple arrays
def find_common_elements(arrays: list[list[int]]) -> list[int]:
    """Find elements common to all arrays."""
    if not arrays:
        return []
    common = set(arrays[0])
    for arr in arrays[1:]:
        common &= set(arr)
    return list(common)


# Find unique elements (elements that appear only once)
def find_unique_elements(nums: list[int]) -> list[int]:
    """Find elements that appear exactly once."""
    from collections import Counter

    count = Counter(nums)
    return [x for x, cnt in count.items() if cnt == 1]


# Find elements that appear in at least k arrays
def find_elements_in_k_arrays(arrays: list[list[int]], k: int) -> list[int]:
    """Find elements that appear in at least k arrays."""
    from collections import Counter

    element_count = Counter()
    for arr in arrays:
        element_count.update(set(arr))
    return [x for x, cnt in element_count.items() if cnt >= k]


# ============================================================================
# 8. CHARACTER SET OPERATIONS
# ============================================================================
# Check if string has all unique characters
def has_unique_chars(s: str) -> bool:
    """Check if string has all unique characters."""
    return len(s) == len(set(s))


# Find common characters between strings
def common_chars(s1: str, s2: str) -> list[str]:
    """Find common characters between two strings."""
    return list(set(s1) & set(s2))


# Check if two strings are anagrams (using set for quick check)
def is_anagram_set(s1: str, s2: str) -> bool:
    """Check if two strings are anagrams (quick check with set)."""
    if len(s1) != len(s2):
        return False
    if set(s1) != set(s2):
        return False
    # Still need to check counts
    from collections import Counter

    return Counter(s1) == Counter(s2)


# Find characters unique to each string
def unique_chars_each(s1: str, s2: str) -> tuple[list[str], list[str]]:
    """Find characters unique to s1 and unique to s2."""
    set1, set2 = set(s1), set(s2)
    unique_s1 = list(set1 - set2)
    unique_s2 = list(set2 - set1)
    return unique_s1, unique_s2


# ============================================================================
# 9. SET-BASED GROUPING
# ============================================================================
# Group strings by unique character set
def group_by_char_set(strs: list[str]) -> dict[frozenset, list[str]]:
    """Group strings by their unique character set."""
    from collections import defaultdict

    groups = defaultdict(list)
    for s in strs:
        key = frozenset(s)
        groups[key].append(s)
    return dict(groups)


# Group by set of values
def group_by_value_set(items: list[tuple]) -> dict:
    """Group items by set of values."""
    from collections import defaultdict

    groups = defaultdict(list)
    for key, *values in items:
        value_set = frozenset(values)
        groups[value_set].append(key)
    return dict(groups)


# ============================================================================
# 10. SET FOR VALIDATION
# ============================================================================
# Validate sudoku (check rows, columns, boxes)
def is_valid_sudoku(board: list[list[str]]) -> bool:
    """Validate 9x9 sudoku board."""
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == ".":
                continue
            if val in rows[i] or val in cols[j]:
                return False
            box_idx = (i // 3) * 3 + j // 3
            if val in boxes[box_idx]:
                return False
            rows[i].add(val)
            cols[j].add(val)
            boxes[box_idx].add(val)

    return True


# Validate if array contains all elements in range
def contains_all_in_range(nums: list[int], start: int, end: int) -> bool:
    """Check if array contains all elements in range [start, end]."""
    num_set = set(nums)
    return all(i in num_set for i in range(start, end + 1))


# Validate constraints using set
def validate_constraints(items: list, allowed: set) -> bool:
    """Validate that all items are in allowed set."""
    return all(item in allowed for item in items)


# Check if permutation is valid (contains all numbers 1 to n)
def is_valid_permutation(nums: list[int]) -> bool:
    """Check if array is valid permutation of [1, n]."""
    n = len(nums)
    return set(nums) == set(range(1, n + 1))
