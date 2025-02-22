from threading import Lock

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    _instance = None
    _lock = Lock()  # Class level lock for thread-safe singleton creation

    def __new__(cls, capacity: int = None):
        with cls._lock:  # Ensure thread-safe singleton creation
            if cls._instance is None:
                if capacity is None:
                    raise ValueError("Capacity must be provided when creating the first instance")
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
            elif capacity is not None and capacity != cls._instance.capacity:
                raise ValueError("Cannot change capacity of existing instance")
            return cls._instance

    def __init__(self, capacity: int = None):
        with self._lock:  # Ensure thread-safe initialization
            if not getattr(self, '_initialized', False):
                if capacity is None:
                    raise ValueError("Capacity must be provided when creating the first instance")
                self.capacity = capacity
                self.cache = {}
                self.instance_lock = Lock()  # Instance level lock for thread-safe operations

                # Initialize dummy head and tail nodes
                self.head = Node()
                self.tail = Node()
                self.head.next = self.tail
                self.tail.prev = self.head
                self._initialized = True

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        with self.instance_lock:
            if key in self.cache:
                node = self.cache[key]
                self._remove(node)
                self._add(node)
                return node.value
            return -1

    def put(self, key: int, value: int) -> None:
        with self.instance_lock:
            if key in self.cache:
                node = self.cache[key]
                self._remove(node)
                node.value = value
                self._add(node)
            else:
                new_node = Node(key, value)
                self.cache[key] = new_node
                self._add(new_node)

                if len(self.cache) > self.capacity:
                    lru_node = self.tail.prev
                    self._remove(lru_node)
                    del self.cache[lru_node.key]