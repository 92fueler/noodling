from threading import Lock
from hashlib import sha256

"""
Thread-safe Hash Map

Implement hash map using an array of buckets
Each bucket will be a list of key-value pairs to handle collisions using chaining.
hash -> idx
idx: [(key1, value2), (key2, value2)]

To ensure thread-safety,
- Approach 1: use a global lock
- Approach 2: use fine-grained locking:
    - One Lock per bucket. This allows concurrent access to different buckets
    - while still protecting shared data within each one.
Approach 3: use segment locking
approach 4: use lock striping
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


class StripedHashMap:
    def __init__(self, num_stripes=16, num_buckets=64):
        self.num_stripes = num_stripes
        self.num_buckets = num_buckets
        self.locks = [Lock() for _ in range(num_stripes)]
        self.buckets = [{} for _ in range(num_buckets)]

    def _hash(self, key):
        return int(sha256(str(key).encode()).hexdigest(), 16)

    def _get_stripe_index(self, key_hash):
        return key_hash % self.num_stripes

    def _get_bucket_index(self, key_hash):
        return key_hash % self.num_buckets

    def put(self, key, value):
        h = self._hash(key)
        stripe_idx = self._get_stripe_index(h)
        bucket_idx = self._get_bucket_index(h)

        with self.locks[stripe_idx]:
            self.buckets[bucket_idx][key] = value

    def get(self, key):
        h = self._hash(key)
        stripe_idx = self._get_stripe_index(h)
        bucket_idx = self._get_bucket_index(h)

        with self.locks[stripe_idx]:
            return self.buckets[bucket_idx].get(key)

    def remove(self, key):
        h = self._hash(key)
        stripe_idx = self._get_stripe_index(h)
        bucket_idx = self._get_bucket_index(h)

        with self.locks[stripe_idx]:
            if key in self.buckets[bucket_idx]:
                del self.buckets[bucket_idx][key]


class Segment:
    def __init__(self):
        self.lock = Lock()
        self.data = {}

    def put(self, key, value):
        with self.lock:
            self.data[key] = value

    def get(self, key):
        with self.lock:
            return self.data.get(key)

    def remove(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]


class SegmentLockedHashMap:
    def __init__(self, num_segments=16):
        self.num_segments = num_segments
        self.segments = [Segment() for _ in range(num_segments)]

    def _hash(self, key):
        return int(sha256(str(key).encode()).hexdigest(), 16)

    def _get_segment_index(self, key_hash):
        return key_hash % self.num_segments

    def put(self, key, value):
        h = self._hash(key)
        seg_idx = self._get_segment_index(h)
        self.segments[seg_idx].put(key, value)

    def get(self, key):
        h = self._hash(key)
        seg_idx = self._get_segment_index(h)
        return self.segments[seg_idx].get(key)

    def remove(self, key):
        h = self._hash(key)
        seg_idx = self._get_segment_index(h)
        self.segments[seg_idx].remove(key)
