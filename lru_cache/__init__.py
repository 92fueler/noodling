"""
LRU Cache implementations including basic and singleton patterns.
"""

from .basic_lru_cache import LRUCache as BasicLRUCache
from .singleton_lru_cache import LRUCache as SingletonLRUCache

__all__ = ['BasicLRUCache', 'SingletonLRUCache']