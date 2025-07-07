In-memory Key-Value Store

- should support basic operations to GET/SET/DELETE records
- should support scanning a specific record’s fields based on a filter
  - prefix filter
  - arbitray filter

Timestamps are guaranteed to be stricly increasing as operations as executed
- should SET with the given timestamp
- should GET the most recent value <= the provided timestamp
- should support TTL (time to live) configurations on database records (ttl = 0 -> always be available)
    - SET_AT
    - DELETE_AT
    - GET_AT
    - SCAN_AT
- should support backup and restore functionality


Auto-timestamp (aim for o(1) for the first two GETs)
- should SET the value for the key with automatically add a timestamp (high-precision)
- should GET the latest value (no timestamp arg)
- should GET(key, timestamp) the exact value at the timestamp
- should GET_BEFORE(key, timestamp) the most recent value <= the provided timestamp

concurrency-controlled
- handle concurrent access, ensure thread safety
related concept: timestamp-based concurrency control (e.g. read/write timestamps to enforce ordering)

### How to run tests
```bash
uv run pytest in_memory_kv/test_*.py
```
