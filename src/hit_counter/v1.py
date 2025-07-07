from collections import deque

"""
https://leetcode.com/problems/design-hit-counter/description/

Design a hit counter which counts the number of hits received in the past 5 minutes
(i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity),
and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
"""
"""
Learning notes:
1. deque is a double-ended queue, which can be used to implement a queue
    - deque.popleft() is o(1) for the first element
    - deque.append() is o(1) for the last element
    - deque.appendleft() is o(1) for the first element
    - deque.pop() is o(1) for the last element
    - deque.popleft() is o(1) for the first element

"""


class HitCounter:
    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # remove hits older than 5 minutes
        self.hits = [t for t in self.hits if t > timestamp - 300]
        return len(self.hits)


class HitCounterV2:
    """
    Optimized solution:
    - use a queue to store hits, and remove hits older than 5 minutes
    - time complexity: o(1) for each hit, o(k) for each query
    - space complexity: o(k)
    """

    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        # remove expired hits
        while self.queue and self.queue[0] <= timestamp - 300:
            self.queue.popleft()
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # remove expired hits
        while self.queue and self.queue[0] <= timestamp - 300:
            self.queue.popleft()
        return len(self.queue)
