"""
Dict patterns

1. frequency counting - count occurrences, character/word frequencies
2. grouping - group items by key/value, anagram grouping
3. two-sum pattern - find pairs, complement search
4. sliding window with dict - track characters/elements in window
5. prefix/suffix tracking - cumulative tracking, subarray sum
6. caching/memoization - memoization pattern, LRU cache
7. union-find tracking - disjoint sets, connected components
"""

from collections import Counter, defaultdict


# ============================================================================
# 1. FREQUENCY COUNTING
# ============================================================================
# Count occurrences
def count_frequency(items: list) -> dict:
    """Count frequency of items."""
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq


# Using Counter
counter = Counter(["a", "b", "a", "c"])  # Counter({'a': 2, 'b': 1, 'c': 1})

# Character frequency in string
char_count = Counter("hello")  # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

# Word frequency in string
words = "hello world hello".split()
word_count = Counter(words)  # Counter({'hello': 2, 'world': 1})


# ============================================================================
# 2. GROUPING
# ============================================================================
# Group by key
def group_by_key(items: list[tuple]) -> dict:
    """Group items by first element."""
    groups = defaultdict(list)
    for key, value in items:
        groups[key].append(value)
    return dict(groups)


# Group by value
def group_by_value(items: list[tuple]) -> dict:
    """Group items by second element."""
    groups = defaultdict(list)
    for key, value in items:
        groups[value].append(key)
    return dict(groups)


# Group anagrams
def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Group strings by anagram."""
    groups = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())


# Group by multiple criteria
def group_by_multiple(items: list[tuple]) -> dict:
    """Group by tuple of keys."""
    groups = defaultdict(list)
    for item in items:
        key = (item[0], item[1])  # group by first two elements
        groups[key].append(item)
    return dict(groups)


# ============================================================================
# 3. TWO-SUM PATTERN
# ============================================================================
# Two sum (find indices)
def two_sum(nums: list[int], target: int) -> list[int]:
    """Find two indices whose values sum to target."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# Two sum (find pairs)
def two_sum_pairs(nums: list[int], target: int) -> list[tuple[int, int]]:
    """Find all pairs that sum to target."""
    seen = {}
    pairs = []
    for num in nums:
        complement = target - num
        if complement in seen and seen[complement] > 0:
            pairs.append((complement, num))
            seen[complement] -= 1
        else:
            seen[num] = seen.get(num, 0) + 1
    return pairs


# Three sum pattern (use with two sum)
def three_sum(nums: list[int], target: int) -> list[list[int]]:
    """Find triplets that sum to target."""
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if curr_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
    return result


# ============================================================================
# 4. SLIDING WINDOW WITH DICT
# ============================================================================
# Longest substring with at most k distinct characters
def longest_substring_k_distinct(s: str, k: int) -> int:
    """Find length of longest substring with at most k distinct chars."""
    char_count = {}
    left = 0
    max_len = 0
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


# Minimum window substring
def min_window(s: str, t: str) -> str:
    """Find minimum window in s containing all characters in t."""
    need = Counter(t)
    window = {}
    left = 0
    valid = 0
    start, min_len = 0, float("inf")

    for right in range(len(s)):
        char = s[right]
        if char in need:
            window[char] = window.get(char, 0) + 1
            if window[char] == need[char]:
                valid += 1

        while valid == len(need):
            if right - left + 1 < min_len:
                start = left
                min_len = right - left + 1

            char = s[left]
            if char in need:
                if window[char] == need[char]:
                    valid -= 1
                window[char] -= 1
            left += 1

    return "" if min_len == float("inf") else s[start : start + min_len]


# ============================================================================
# 5. PREFIX/SUFFIX TRACKING
# ============================================================================
# Subarray sum equals k
def subarray_sum(nums: list[int], k: int) -> int:
    """Count number of subarrays with sum equals k."""
    prefix_sum = {0: 1}  # sum: count
    curr_sum = 0
    count = 0

    for num in nums:
        curr_sum += num
        if curr_sum - k in prefix_sum:
            count += prefix_sum[curr_sum - k]
        prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

    return count


# Longest subarray with sum k
def longest_subarray_sum(nums: list[int], k: int) -> int:
    """Find length of longest subarray with sum k."""
    prefix_sum = {0: -1}  # sum: first index
    curr_sum = 0
    max_len = 0

    for i, num in enumerate(nums):
        curr_sum += num
        if curr_sum - k in prefix_sum:
            max_len = max(max_len, i - prefix_sum[curr_sum - k])
        if curr_sum not in prefix_sum:
            prefix_sum[curr_sum] = i

    return max_len


# ============================================================================
# 6. CACHING / MEMOIZATION
# ============================================================================
# Simple memoization
def memoize(func):
    """Decorator for memoization."""
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


# Using functools.lru_cache
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    """Fibonacci with memoization."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Manual memoization for dynamic programming
def dp_with_memo(nums: list[int]) -> int:
    """Example DP with memoization."""
    memo = {}

    def dp(i: int) -> int:
        if i in memo:
            return memo[i]
        if i >= len(nums):
            return 0
        memo[i] = max(dp(i + 1), nums[i] + dp(i + 2))
        return memo[i]

    return dp(0)


# ============================================================================
# 7. UNION-FIND TRACKING
# ============================================================================
# Disjoint set tracking
class UnionFind:
    """Union-Find data structure."""

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


# Connected components
def find_components(edges: list[tuple]) -> dict:
    """Find connected components using dict."""
    uf = UnionFind()
    for x, y in edges:
        uf.union(x, y)

    components = defaultdict(list)
    for node in uf.parent:
        components[uf.find(node)].append(node)
    return dict(components)
