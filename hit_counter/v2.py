from collections import deque

"""
Group hits by timestamp - optimizing duplicates

If bursts are common (multiple hits at the same time), instead of enqueuing each duplicates,
- use pairs [timestamp, count] to represent the hits
- on hit(t), update the count for the timestamp t
- on getHits(t), dequeue outdated pairs and subtract their counts from the running total
"""


class HitCounter:
    def __init__(self):
        self.queue = deque()
        self.total = 0

    def hit(self, timestamp: int) -> None:
        last_timestamp, count = self.queue[-1] if self.queue else (0, 0)
        if last_timestamp == timestamp:
            self.queue[-1] = (timestamp, count + 1)
        else:
            self.queue.append((timestamp, 1))
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        while self.queue and self.queue[0][0] <= timestamp - 300:
            timestamp, count = self.queue.popleft()
            self.total -= count
        return self.total
