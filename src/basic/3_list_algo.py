"""
List patterns

1. two-pointer technique - opposite ends, fast/slow pointers
2. sliding window - fixed/variable size window
3. binary search - search in sorted array, find insertion point
4. stack patterns - monotonic stack, next greater/smaller element
5. prefix/suffix sums - cumulative sums for range queries
6. merge/divide - merge sorted arrays, divide and conquer
7. swap/partition - partition by condition, swap elements
8. rotation/shift - rotate array, cyclic shift
"""


# ============================================================================
# 1. TWO-POINTER TECHNIQUE
# ============================================================================
# Opposite ends
def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """Two sum in sorted array."""
    left, right = 0, len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []


# Fast/slow pointers (Floyd's cycle detection)
def has_cycle(nums: list[int]) -> bool:
    """Detect cycle using fast/slow pointers."""
    slow = fast = 0
    while fast < len(nums) - 1:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            return True
    return False


# Remove duplicates in-place
def remove_duplicates(nums: list[int]) -> int:
    """Remove duplicates, return new length."""
    if not nums:
        return 0
    write_idx = 1
    for read_idx in range(1, len(nums)):
        if nums[read_idx] != nums[read_idx - 1]:
            nums[write_idx] = nums[read_idx]
            write_idx += 1
    return write_idx


# ============================================================================
# 2. SLIDING WINDOW
# ============================================================================
# Fixed size window
def max_sum_subarray(nums: list[int], k: int) -> int:
    """Maximum sum of subarray of size k."""
    if len(nums) < k:
        return 0
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)
    return max_sum


# Variable size window
def longest_subarray_with_sum(nums: list[int], target: int) -> int:
    """Longest subarray with sum <= target."""
    left = 0
    curr_sum = 0
    max_len = 0
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum > target:
            curr_sum -= nums[left]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


# ============================================================================
# 3. BINARY SEARCH
# ============================================================================
import bisect


# Search in sorted array
def binary_search(nums: list[int], target: int) -> int:
    """Returns index if found, -1 otherwise."""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Find insertion point
bisect.bisect_left([1, 3, 5, 7], 4)  # 2 - insert before 5
bisect.bisect_right([1, 3, 5, 7], 4)  # 2 - insert after 4


# Search in rotated sorted array
def search_rotated(nums: list[int], target: int) -> int:
    """Search in rotated sorted array."""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


# ============================================================================
# 4. STACK PATTERNS
# ============================================================================
# Next greater element
def next_greater_element(nums: list[int]) -> list[int]:
    """Find next greater element for each element."""
    stack = []
    result = [-1] * len(nums)
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result


# Monotonic stack (increasing)
def monotonic_increasing_stack(nums: list[int]):
    """Maintain increasing order in stack."""
    stack = []
    for num in nums:
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)
    return stack


# Valid parentheses / brackets
def is_valid_parentheses(s: str) -> bool:
    """Check if parentheses are valid."""
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack


# ============================================================================
# 5. PREFIX / SUFFIX SUMS
# ============================================================================
# Prefix sum
def prefix_sum(nums: list[int]) -> list[int]:
    """Calculate prefix sums."""
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    return prefix  # [0, nums[0], nums[0]+nums[1], ...]


# Range sum query (O(1) after O(n) preprocessing)
def range_sum(prefix: list[int], left: int, right: int) -> int:
    """Get sum from left to right (inclusive)."""
    return prefix[right + 1] - prefix[left]


# Suffix sum
def suffix_sum(nums: list[int]) -> list[int]:
    """Calculate suffix sums."""
    suffix = [0] * (len(nums) + 1)
    for i in range(len(nums) - 1, -1, -1):
        suffix[i] = suffix[i + 1] + nums[i]
    return suffix


# ============================================================================
# 6. MERGE / DIVIDE
# ============================================================================
# Merge two sorted arrays
def merge_sorted(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """Merge nums2 into nums1 in-place."""
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


# Merge intervals
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Merge overlapping intervals."""
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for curr in intervals[1:]:
        if curr[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], curr[1])
        else:
            merged.append(curr)
    return merged


# ============================================================================
# 7. SWAP / PARTITION
# ============================================================================
# Partition (quick select pattern)
def partition(nums: list[int], left: int, right: int, pivot_idx: int) -> int:
    """Partition array around pivot value."""
    pivot_value = nums[pivot_idx]
    # Move pivot to end
    nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
    # Partition
    store_idx = left
    for i in range(left, right):
        if nums[i] < pivot_value:
            nums[store_idx], nums[i] = nums[i], nums[store_idx]
            store_idx += 1
    # Move pivot to final position
    nums[right], nums[store_idx] = nums[store_idx], nums[right]
    return store_idx


# Move zeros to end
def move_zeros(nums: list[int]) -> None:
    """Move all zeros to end in-place."""
    write_idx = 0
    for read_idx in range(len(nums)):
        if nums[read_idx] != 0:
            nums[write_idx], nums[read_idx] = nums[read_idx], nums[write_idx]
            write_idx += 1


# ============================================================================
# 8. ROTATION / SHIFT
# ============================================================================
# Rotate array to right by k
def rotate_right(nums: list[int], k: int) -> None:
    """Rotate array to right by k positions in-place."""
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]


# Rotate array to left by k
def rotate_left(nums: list[int], k: int) -> None:
    """Rotate array to left by k positions in-place."""
    n = len(nums)
    k = k % n
    nums[:] = nums[k:] + nums[:k]


# Reverse array in range
def reverse_range(nums: list[int], left: int, right: int) -> None:
    """Reverse array in range [left, right]."""
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
