1. `dict.update()` a build-in method to update the dictionary with the key-value pairs
2. two dicts comparison can use `==` operator, why:
    - dictionary is unordered, so equality doesn't depend on the order of the key-value pairs
    - `==` operator checks if
        - both objects are objects
        - they have the same keys
        - for each key, the values are the same
3. KeyError is a built-in exception in Python that is raised
    when a key is not found in a dictionary.
    ```python
    try:
        # code that may raise KeyError
    except KeyError:
        # code to handle KeyError
    except Exception as e:
        # code to handle other exceptions
    ```
4. if return type is type A or type B, use Union[A, B]
5. `pytest.mark.parametrize` is a decorator that allows you to run the same test
    with different parameters.
6. `super().__init__()` is a way to call the constructor of the parent class.
7. how to represent "never expires" in a way that makes comparisons simple and consistent
    ```python
    expiry = float('inf') if ttl == 0 else timestamp + ttl
    ```
8. `reversed()` is a built-in function that returns a reversed iterator.
   - time complexity: O(1) and space complexity: O(1)
   - vs. `list[::-1]` -> creates a new list Time: o(n) and Space: o(n)
   - vs. `list.reverse()` -> in-place reverse Time: o(n) and Space: o(1)
9. `reversed(self.db[key].items())` -> This doesn't guarantee the order of the timestamps
   unless timestamps are inserted in sorted order and no timestamps are skipped.
   Even then, it's unsafe.
10. Always use while left <= right in classic binary search
   if you’re not locking down on left == right manually after the loop.
11. from sortedcontainers import SortedDict (not built-in Python module)
12. bisect module
   - bisect.bisect_left(a, x)
   - bisect.bisect_right(a, x)
   - bisect.bisect(a, x) -> default is bisect_right
   - bisect.insort_left(a, x)
   - bisect.insort_right(a, x)
   - bisect.insort(a, x) -> default is insort_right
    ```python
    arr = [1, 2, 2, 3]
    bisect.bisect_left(arr, 2)   # 1 — insert before first 2
    bisect.bisect_right(arr, 2)  # 3 — insert after last 2
    ```
13. chr(127) is the last ASCII character
14. bisect.bisect_right(a, x) returns the insertion index in a sorted list a
    it's a sorted list, but here is a list of tuples like [(timestamp, value), ...]
    so, we need to compare against a tuple of the same form.
    Tuples compare lexicographically, so
    - (3, 'z') < (4, 'a') True
    - (3, 'z') < (3, 'zz') True
    So use the maximum possible string chr(127) to make sure
    it goes after all existing values with the same timestamp.
    - (3, 'z') < (3, chr(127)) True
    - (3, 'z') < (3, chr(127)) True
15. deque is a double-ended queue, which can be used to implement a queue
    - deque.popleft() is o(1) for the first element
    - deque.append() is o(1) for the last element
    - deque.appendleft() is o(1) for the first element
    - deque.pop() is o(1) for the last element
    - deque.popleft() is o(1) for the first element
