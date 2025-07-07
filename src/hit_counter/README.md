
Hit Counter

### classic problem: 5-minute Hit Counter
- hit(timestamp)
- getHits(timestamp)

Naive Approach:
- store every timestamp in a list, and on each query, scan and count only recent hits.
   Time complexity: o(n) for each query

Optimized queue-based solution:
- Use a queue (or Deque) of timestamps
    - On hit(t), enqueue t
    - On getHits(t), dequeue from front while t <= t - 300
    - return current queue size or a running count
    - each hit enqueue once and dequeued once -> amortized o(1)


Variants & Follow-ups
- different window sizes: e.g. 2-minute or 3,000 ms windows
- Different aggregation: such as moving averages or metrics over sliding windows
-

###


### How to run tests
```bash
uv run pytest hit_counter/test_*.py
```
