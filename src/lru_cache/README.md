# LRU Cache Implementations

This directory contains different implementations of a Least Recently Used (LRU) Cache data structure. Each implementation demonstrates different design patterns and approaches while maintaining the core LRU cache functionality.

## Implementations

### 1. Basic Implementation
Location: `basic_lru_cache.py`

A straightforward implementation of LRU Cache using:
- Double linked list for O(1) node removal and addition
- Hash map for O(1) key-value lookups
- Time complexity: O(1) for both get and put operations
- Space complexity: O(capacity)

Features:
- Simple and efficient implementation
- Uses dummy head and tail nodes for easier edge cases
- No thread safety mechanisms

### 2. Singleton Implementation
Location: `singleton_lru_cache.py`

A thread-safe singleton implementation of LRU Cache that ensures only one cache instance exists in the application.

Features:
- Thread-safe singleton pattern using locks
- Double linked list + hash map data structure
- Two-level locking mechanism:
  - Class-level lock for singleton creation
  - Instance-level lock for cache operations
- Time complexity: O(1) for both get and put operations
- Space complexity: O(capacity)

## Usage Examples

### Basic Implementation
```python
from lru_cache.basic_lru_cache import LRUCache

# Create a cache with capacity 2
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # returns 1
cache.put(3, 3)      # evicts key 2
print(cache.get(2))  # returns -1 (not found)
```

### Singleton Implementation
```python
from lru_cache.singleton_lru_cache import LRUCache

# Create first instance with capacity
cache1 = LRUCache(2)
cache1.put(1, 1)

# Get the same instance
cache2 = LRUCache()  # capacity parameter optional for subsequent instances
print(cache2.get(1))  # returns 1 (same cache instance)
```

## Testing

To run tests for the implementations:
```bash
# From the lru_cache directory
uv run pytest tests/

# Or from the project root
uv run pytest lru_cache/tests/

# Run specific implementation tests
# From lru_cache directory
uv run pytest tests/test_basic_lru_cache.py
uv run pytest tests/test_singleton_lru_cache.py

# Or from project root
uv run pytest lru_cache/tests/test_basic_lru_cache.py
uv run pytest lru_cache/tests/test_singleton_lru_cache.py
```

## Implementation Details

Both implementations use a combination of:
1. **Double Linked List**: For maintaining order of elements
   - Most recently used items at the head
   - Least recently used items at the tail
   - O(1) removal and addition of nodes

2. **Hash Map**: For quick key-value lookups
   - Maps keys to corresponding linked list nodes
   - Provides O(1) access to any cache entry

The main difference is that the singleton implementation adds thread safety and ensures a single cache instance across the application.
