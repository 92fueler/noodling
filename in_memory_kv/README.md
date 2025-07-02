In-memory Key-Value Store


Your task is to implement a simplified version of an in-memory database. Plan your design according to the level specifications below (current level is in bold):

- Level 1: in-memory database should support basic operations to GET/SET/DELETE records
- Level 2: in-memory database should support scanning a specific record’s fields based on a filter
- Level 3: in-memory database should support TTL (time to live) configurations on database records
- Level 4: in-memory database should support backup and restore functionality

To move to the next level, you need to pass all the tests at this level.

Note:

Each query will only call one database operation. After each query, append the returned value to the resulting array. If the current query doesn’t return anything, append an empty string.

### How to run tests
```bash
uv run pytest in_memory_kv/test_v1.py
```
