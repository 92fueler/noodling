"""
Auto-timestamp key-value store
- SET(key, value) -> set the value for the key
  and automatically add a timestamp (high precision)
- GET(key) -> returns the latest value (no timestamp arg)
- GET(key, timestamp) -> returns the exact value at the timestamp
- GET_BEFORE(key, timestamp) -> returns the most recent value <= the provided timestamp

Aim for o(1) for the first two get operations

https://joshrosso.com/c/time-based-kv
"""
