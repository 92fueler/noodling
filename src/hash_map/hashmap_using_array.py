from typing import List, Tuple

"""
https://leetcode.com/problems/design-hashmap/description/

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.

- void put(int key, int value) inserts a (key, value) pair into the HashMap.
If the key already exists in the map, update the corresponding value.

- int get(int key) returns the value to which the specified key is mapped,
or -1 if this map contains no mapping for the key.

- void remove(key) removes the key and its corresponding value
if the map contains the mapping for the
"""
"""
Learning notes:
1. hash map collision -> chaining: linked list or array
2. hash function:
    - hash(key) -> index
    - hash(key) = key % len(hash_map)
"""


# using array for chaining
class MyHashMap:
    def __init__(self):
        self.capacity: int = 1000
        self.db: List[List[Tuple[int, int]]] = [None] * self.capacity

    def _hash(self, key: int) -> int:
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)

        if self.db[index] is None:
            self.db[index] = []  # <-- IMPORTANT

        for i, (k, _) in enumerate(self.db[index]):
            if k == key:
                self.db[index][i] = (key, value)
                return

        self.db[index].append((key, value))

    def get(self, key: int) -> int:
        index = self._hash(key)

        if self.db[index] is None:
            return -1

        for k, v in self.db[index]:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)

        if self.db[index] is None:
            return

        for i, (k, _) in enumerate(self.db[index]):
            if k == key:
                del self.db[index][i]
                return
