
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


class MyHashMap:
    def __init__(self):
        self.capacity = 1000
        self.db = [None] * self.capacity

    def _hash(self, key: int) -> int:
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        head = self.db[idx]

        if head is None:
            self.db[idx] = Node(key, value)
            return

        while head:
            if head.key == key:
                head.val = value
                return
            if head.next is None:
                head.next = Node(key, value)
                return
            head = head.next

    def get(self, key: int) -> int:
        idx = self._hash(key)
        head = self.db[idx]

        while head:
            if head.key == key:
                return head.val
            head = head.next

        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        head = self.db[idx]
        prev = None

        while head:
            if head.key == key:
                if prev is None:
                    self.db[idx] = head.next
                else:
                    prev.next = head.next
                return
            prev = head
            head = head.next


class Node:
    def __init__(self, key: int, val: int, next=None):
        self.key = key
        self.val = val
        self.next = next
