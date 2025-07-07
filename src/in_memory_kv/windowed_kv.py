"""
Windowed key-value store
Store key-value pairs where each key is valid only within a fixed time window.

- put(String key, long value): records the key-value with the current timestamp
- get(String key): returns the value if it exists and is still within the expiry window
  (e.g. 1 hour)
- getAverage(): returns the average of all values within the non-expired window,
  in o(1) time if possible

https://www.reddit.com/r/ExperiencedDevs/comments/16o0i1p/asked_to_implemented_windowed_key_value_store_for/
"""
