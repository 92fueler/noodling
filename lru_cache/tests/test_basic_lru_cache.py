from ..basic_lru_cache import LRUCache

def test_basic_operations():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(3) == 3

def test_update_existing():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(1, 2)
    assert cache.get(1) == 2

def test_capacity_limit():
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2

def test_lru_eviction():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)  # makes 1 most recently used
    cache.put(3, 3)  # should evict 2
    assert cache.get(2) == -1
    assert cache.get(1) == 1
    assert cache.get(3) == 3