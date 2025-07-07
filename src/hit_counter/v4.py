"""
Implement a hit counter that supports multiple threads concurrently
- use a lock to synchronize access to the hit count
"""

import threading


class HitCounter:
    def __init__(self):
        self.hits = 0
        self.lock = threading.Lock()

    def hit(self):
        with self.lock:
            self.hits += 1

    def get_hits(self):
        with self.lock:
            return self.hits
