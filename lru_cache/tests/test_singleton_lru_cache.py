import pytest
from ..singleton_lru_cache import LRUCache
import threading
import time

@pytest.fixture(autouse=True)
def reset_singleton():
    """Reset the singleton instance before each test."""
    LRUCache._instance = None
    yield

def test_singleton_pattern():
    cache1 = LRUCache(2)
    cache2 = LRUCache()
    assert cache1 is cache2

def test_basic_operations():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(3) == 3

def test_thread_safety():
    cache = LRUCache(5)

    def worker():
        for i in range(100):
            cache.put(i, i)
            time.sleep(0.001)
            cache.get(i)

    threads = [threading.Thread(target=worker) for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # Verify the last 5 items are in cache
    for i in range(95, 100):
        assert cache.get(i) != -1

def test_singleton_state_persistence():
    cache1 = LRUCache(2)
    cache1.put(1, 1)

    cache2 = LRUCache()  # Get the same instance
    assert cache2.get(1) == 1  # Should have the same data

def test_invalid_initialization():
    with pytest.raises(ValueError):
        LRUCache()  # First instance must have capacity