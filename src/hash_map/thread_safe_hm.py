from threading import Lock

"""
Thread-safe Hash Map

Implement hash map using an array of buckets
Each bucket will be a list of key-value pairs to handle collisions using chaining.
hash -> idx
idx: [(key1, value2), (key2, value2)]

To ensure thread-safety,
approach 1: use a global lock
approach 2: use fine-grained locking:
One Lock per bucket. This allows concurrent access to different buckets
while still protecting shared data within each one.
"""


class ThreadSafeHashMapV1:
    def __init__(self, capacity=10000):
        self.capacity = capacity
        self.db = [None] * self.capacity
        self.lock = Lock()

    def _hash(self, key):
        return key % self.capacity

    def put(self, key: int, value: int):
        with self.lock:
            index = self._hash(key)
            if self.db[index] is None:
                self.db[index] = []
            for i, (k, _) in enumerate(self.db[index]):
                if k == key:
                    self.db[index][i] = (key, value)
                    return
            self.db[index].append((key, value))

    def get(self, key) -> int:
        with self.lock:
            index = self._hash(key)
            if self.db[index] is None:
                return -1
            for _, (k, v) in enumerate(self.db[index]):
                if k == key:
                    return v
            return -1

    def remove(self, key: int) -> None:
        with self.lock:
            index = self._hash(key)
            if self.db[index] is None:
                return
            for i, (k, v) in enumerate(self.db[index]):
                if k == key:
                    del self.db[index][i]
                    return
