from typing import Dict, List, Tuple
import bisect

"""
https://leetcode.com/problems/time-based-key-value-store/
Design a time-based key-value data structure that can store multiple values
for the same key at different time stamps and
retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key
with the value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that
set was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the value associated
with the largest timestamp_prev.
If there are no values, it returns "".

Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
"""
"""
Learning notes:
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
"""
class TimeMap:
    """
    Hashmap + tuple + linear search
    - time complexity: O(n) for get and o(1) for set
    - space complexity: O(n) for the db
    """
    def __init__(self):
        self.db: Dict[str, List[Tuple[int, str]]] = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Store the key with the value at the given time timestamp.
        All the timestamps are strictly increasing.
        """
        if key not in self.db:
            self.db[key] = []
        self.db[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.db:
            return ""
        for t, v in reversed(self.db[key]):
            if t <= timestamp:
                return v
        return ""

class TimeMap2:
    """
    Hashmap + hashmap + linear search
    - time complexity: O(1) for get and o(1) for set
    - space complexity: O(n) for the db
    """
    def __init__(self):
        self.db: Dict[str, Dict[int, str]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.db:
            self.db[key] = {}
        self.db[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.db:
            return ""
        for t, v in reversed(self.db[key].items()): # <- This is wrong!
            if t <= timestamp:
                return v
        return ""

class TimeMap3:
    """
    hashmap + sorted list/binary search
    - time complexity: O(logn) for get and o(1) for set
    - space complexity: O(n) for the db
    """
    def __init__(self):
        self.db: Dict[str, List[Tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.db:
            self.db[key] = []
        self.db[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.db:
            return ""
        if timestamp < self.db[key][0][0]:
            return ""
        left, right = 0, len(self.db[key]) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            if self.db[key][mid][0] == timestamp:
                return self.db[key][mid][1]
            if self.db[key][mid][0] < timestamp:
                res = self.db[key][mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res

class TimeMap4:
    """
    hashmap + sorted list/binary search
    - time complexity: O(logn) for get and o(1) for set
    - space complexity: O(n) for the db
    """
    def __init__(self):
        self.db: Dict[str, List[Tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.db:
            self.db[key] = []
        self.db[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.db:
            return ""
        items = self.db[key]
        idx = bisect.bisect_right(items, (timestamp, chr(127)))
        if idx == 0:
            return ""
        return items[idx - 1][1]
