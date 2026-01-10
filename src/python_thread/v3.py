import time
from threading import Lock, RLock
from concurrent.futures import ThreadPoolExecutor


"""
Race condition and deadlock
"""

"""
Race condition:
- multiple threads accessing and modifying the same data without synchronization
- the final result depends on the sequence of execution
- the result is unpredictable
"""
# class FakeDatabase:
#     def __init__(self):
#         self.value = 0

#     def update(self, name):
#         print(f"Thread {name} starting update")
#         local_copy = self.value
#         local_copy += 1
#         time.sleep(1)
#         self.value = local_copy

# if __name__ == "__main__":
#     db = FakeDatabase()
#     print(f"Testing update. Starting value is {db.value}")
#     with ThreadPoolExecutor(max_workers=10) as executor:
#         for idx in range(10):
#             executor.submit(db.update, idx)
#     print(f"Testing update. Ending value is {db.value}")

"""
Use lock to avoid race condition
"""
# class FakeDatabaseWithLock:
#     def __init__(self):
#         self.value = 0
#         self.lock = Lock()

#     def update(self, name):
#         print(f"Thread {name} starting update")
#         with self.lock:
#             local_copy = self.value
#             local_copy += 1
#             time.sleep(0.1)
#             self.value = local_copy
#             print(f"Thread {name} about to release lock with value {self.value}")
#         print(f"Thread {name} after release lock")

# if __name__ == "__main__":
#     db = FakeDatabaseWithLock()
#     print(f"Testing update. Starting value is {db.value}")
#     with ThreadPoolExecutor(max_workers=10) as executor:
#         for idx in range(10):
#             executor.submit(db.update, idx)
#     print(f"Testing update. Ending value is {db.value}")

"""
Deadlock:
- multiple threads waiting for each other to release a resource
- the threads are stuck and cannot proceed
"""


class Deadlock:
    def __init__(self):
        self.lock1 = RLock()
        self.lock2 = RLock()

    def thread1(self):
        with self.lock1:
            print("Thread 1 acquired lock1")
            time.sleep(1)
            with self.lock2:
                print("Thread 1 acquired lock2")

    def thread2(self):
        with self.lock2:
            print("Thread 2 acquired lock2")
            time.sleep(1)
            with self.lock1:
                print("Thread 2 acquired lock1")

    def nested_lock(self):
        with self.lock1:
            print("First acquire")
            with self.lock1:
                print("Second acquire (same thread, same lock)")


if __name__ == "__main__":
    deadlock = Deadlock()
    print("Starting deadlock")
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(deadlock.thread1)
        executor.submit(deadlock.thread2)
    deadlock.nested_lock()
