"""
Implement a thread-safe in-memory key-value store using timestamp-based concurrency control
- assign each transaction a unique timstamp TS(Ti)
- follows timestamp-ordering rules for reads/writes
- ensures serializability without using locks
"""

"""
Learning notes:
1. threading module provides a way to run multiples operations concurrently
   using threads within the same process.
    - run in parallel (but only one executes Python bytecode at a time due to GIL)

2. GIL is a global interpreter lock that allows only one thread to execute Python bytecode at a time
    - Python's CPython interpreter has a GIL that allows one thread to execute Python code
    at once, even on multi-core systems.

3. mutex: short for mutal execlusion, a locking mechanism used in concurrent programming
    to ensure that only one thread can access a shared resource at a time.

4. CPU-bound tasks (heavy computation) vs I/O-bound tasks (disk/network operations)
    - CPU-bound tasks: tasks that require a lot of CPU processing power, such as
    complex calculations, image processing, or machine learning.

    So multiple threads just take turns, like this:
    [Thread 1] → [Thread 2] → [Thread 1] → ...
    No speedup, no parallelism.
    ✅ Solution: Use multiprocessing instead of threading — processes don't share a GIL.

    - I/O-bound tasks: tasks that require a lot of input/output operations, such as
    reading from a file, making network requests, or writing to a database.
    While a thread is waiting on I/O, the GIL is released, allowing other threads to run.

    [Thread 1 waiting on network] → [Thread 2 reads file] → [Thread 3 writes log]
    ✅ In this case, threading is useful and improves performance via concurrency.

4. threading.Lock is a mutex primitive that can be used to synchronize access to a shared resource
    prevent race conditions and ensure that only one thread can access the resource at a time.
    - lock.acquire(blocking=True, timeout=None) to acquire the lock with a timeout-
      - blocking is a boolean value that indicates whether the thread should block until the lock is acquired
      - timeout is the maximum time to wait for the lock to be acquired
      - if timeout is reached, the thread will raise a TimeoutError
      - if timeout is None, the thread will wait indefinitely until the lock is acquired
    - lock.release() to release the lock
    - lock.locked() to check if the lock is acquired
    - lock.acquire(blocking=True, timeout=None) to acquire the lock with a timeout
5.
6.
7.
8.
9.
10.

"""
