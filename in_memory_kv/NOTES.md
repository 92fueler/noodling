1. reversed() is a built-in function that returns a reversed iterator.
   - time complexity: O(1) and space complexity: O(1)
   - vs. list[::-1] -> creates a new list Time: o(n) and Space: o(n)
   - vs. list.reverse() -> in-place reverse Time: o(n) and Space: o(1)

2. reversed(self.db[key].items()) -> This doesn't guarantee the order of the timestamps
   unless timestamps are inserted in sorted order and no timestamps are skipped.
   Even then, it's unsafe.
3. Always use while left <= right in classic binary search
   if you’re not locking down on left == right manually after the loop.
4. from sortedcontainers import SortedDict (not built-in Python module)
5. bisect module
   - bisect.bisect_left(a, x)
   - bisect.bisect_right(a, x)
   - bisect.bisect(a, x) -> default is bisect_right
   - bisect.insort_left(a, x)
   - bisect.insort_right(a, x)
   - bisect.insort(a, x) -> default is insort_right

    arr = [1, 2, 2, 3]
    bisect.bisect_left(arr, 2)   # 1 — insert before first 2
    bisect.bisect_right(arr, 2)  # 3 — insert after last 2
6. chr(127) is the last ASCII character
7. bisect.bisect_right(a, x) returns the insertion index in a sorted list a
    it's a sorted list, but here is a list of tuples like [(timestamp, value), ...]
    so, we need to compare against a tuple of the same form.
    Tuples compare lexicographically, so
    - (3, 'z') < (4, 'a') True
    - (3, 'z') < (3, 'zz') True
    So use the maximum possible string chr(127) to make sure
    it goes after all existing values with the same timestamp.
    - (3, 'z') < (3, chr(127)) True
    - (3, 'z') < (3, chr(127)) True
