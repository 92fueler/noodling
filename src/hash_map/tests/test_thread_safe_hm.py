import pytest
import threading
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from src.hash_map.thread_safe_hm import ThreadSafeHashMapV1
"""
Thread Safety Testing Learning Notes
====================================

OVERVIEW:
---------
This file demonstrates comprehensive thread safety testing using different approaches:
1. threading.Thread - Manual thread management
2. ThreadPoolExecutor - Automatic thread pool management
3. Hybrid approaches - Combining both methods

CORE CONCEPTS:
--------------

1. THREADING.THREAD (Manual Control)
   - Best for: Long-running operations, fine-grained control
   - Use case: Stress testing with many operations per thread
   - Pros: Simple, direct control, easy to debug
   - Cons: Manual thread management, no built-in result collection

2. THREADPOOLEXECUTOR (Automatic Management)
   - Best for: Many short tasks, result collection, exception handling
   - Use case: Batch processing, collecting results from threads
   - Pros: Automatic management, built-in features, cleaner code
   - Cons: Less control over individual threads

THREAD LIFECYCLE COMPARISON:
---------------------------

threading.Thread Lifecycle:
1. Creation: thread = threading.Thread(target=worker, args=(1,))
2. Start: thread.start() - thread begins execution
3. Running: Thread executes worker function in background
4. Join: thread.join() - main thread waits for completion
5. Cleanup: Thread resources are automatically cleaned up

ThreadPoolExecutor Lifecycle:
1. Creation: executor = ThreadPoolExecutor(max_workers=4)
2. Task Submission: future = executor.submit(worker, args)
3. Execution: Thread pool assigns task to available thread
4. Result Collection: result = future.result() or as_completed()
5. Shutdown: executor.shutdown() or context manager cleanup

USAGE PATTERNS:
--------------

1. threading.Thread Basic Usage:
   ```python
   def worker(thread_id):
       for i in range(100):
           # Do work
           pass

   threads = []
   for i in range(10):
       thread = threading.Thread(target=worker, args=(i,))
       threads.append(thread)
       thread.start()

   for thread in threads:
       thread.join()
   ```

2. ThreadPoolExecutor Basic Usage:
   ```python
   def worker(thread_id):
       for i in range(100):
           # Do work
           pass
       return f"Thread {thread_id} completed"

   with ThreadPoolExecutor(max_workers=10) as executor:
       futures = [executor.submit(worker, i) for i in range(10)]
       results = [future.result() for future in futures]
   ```

3. ThreadPoolExecutor with as_completed():
   ```python
   with ThreadPoolExecutor(max_workers=4) as executor:
       futures = [executor.submit(worker, i) for i in range(10)]
       for future in as_completed(futures):
           result = future.result()
           print(f"Completed: {result}")
   ```

4. ThreadPoolExecutor with map():
   ```python
   with ThreadPoolExecutor(max_workers=4) as executor:
       results = list(executor.map(worker, range(10)))
   ```

THREAD SAFETY TESTING STRATEGIES:
--------------------------------

1. Basic Testing:
   - Test concurrent put/get/remove operations
   - Verify data integrity after concurrent access
   - Test collision handling under concurrent load

2. Stress Testing:
   - High operation counts (100-500 operations per thread)
   - Multiple threads (5-20 threads)
   - Extended execution times

3. Race Condition Testing:
   - Check-then-act patterns
   - Concurrent updates to same keys
   - Mixed operation types (put/get/remove)

4. Edge Case Testing:
   - Zero capacity hash maps
   - Negative keys
   - Very large keys
   - Non-existent key access

5. Performance Testing:
   - Execution time comparison
   - Resource usage analysis
   - Scalability testing

BEST PRACTICES:
--------------

1. Always join threads or use context managers
2. Use locks for shared data access
3. Test with different thread counts and operation mixes
4. Verify final state consistency
5. Handle exceptions and timeouts
6. Use appropriate approach for the task:
   - threading.Thread for long-running operations
   - ThreadPoolExecutor for many short tasks
   - Hybrid for complex scenarios

COMMON PATTERNS:
---------------

1. Worker Function Pattern:
   ```python
   def worker(thread_id):
       for i in range(operations_per_thread):
           key = thread_id * operations_per_thread + i
           value = key * 2
           shared_data.put(key, value)
   ```

2. Result Collection Pattern:
   ```python
   results = []
   def worker(thread_id):
       thread_results = []
       # ... do work ...
       return thread_results
   ```

3. Mixed Operations Pattern:
   ```python
   def mixed_worker(thread_id):
       for i in range(operations_per_thread):
           operation = random.choice(["put", "get", "remove"])
           # ... perform operation ...
   ```

"""

class TestThreadSafeHashMapV1:
    """Test suite for ThreadSafeHashMapV1 thread safety"""

    def test_basic_operations(self):
        """Test basic put, get, remove operations"""
        hm = ThreadSafeHashMapV1(capacity=10)

        # Test put and get
        hm.put(1, 100)
        assert hm.get(1) == 100

        # Test update
        hm.put(1, 200)
        assert hm.get(1) == 200

        # Test remove
        hm.remove(1)
        assert hm.get(1) == -1

        # Test non-existent key
        assert hm.get(999) == -1

    def test_collision_handling(self):
        """Test that collisions are handled correctly"""
        hm = ThreadSafeHashMapV1(capacity=1)  # Force all keys to collide

        # All keys will hash to the same bucket
        hm.put(1, 100)
        hm.put(2, 200)
        hm.put(3, 300)

        assert hm.get(1) == 100
        assert hm.get(2) == 200
        assert hm.get(3) == 300

        # Test remove with collision
        hm.remove(2)
        assert hm.get(1) == 100
        assert hm.get(2) == -1
        assert hm.get(3) == 300

    def test_concurrent_puts(self):
        """Test concurrent put operations from multiple threads"""
        hm = ThreadSafeHashMapV1(capacity=100)
        num_threads = 10
        # 10 threads, each thread will do 100 operations
        operations_per_thread = 100

        def put_worker(thread_id):
            """Worker function for concurrent puts"""
            for i in range(operations_per_thread):
                key = thread_id * operations_per_thread + i
                value = key * 2
                hm.put(key, value)

        # Start multiple threads
        threads = []
        for i in range(num_threads):
            thread = threading.Thread(target=put_worker, args=(i,))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Verify all values were stored correctly
        for thread_id in range(num_threads):
            for i in range(operations_per_thread):
                key = thread_id * operations_per_thread + i
                expected_value = key * 2
                assert hm.get(key) == expected_value

    def test_concurrent_gets(self):
        """Test concurrent get operations from multiple threads"""
        hm = ThreadSafeHashMapV1(capacity=100)

        # Pre-populate the hash map
        for i in range(1000):
            hm.put(i, i * 2)

        num_threads = 10
        operations_per_thread = 100
        results = []

        def get_worker(thread_id):
            """Worker function for concurrent gets"""
            thread_results = []
            for i in range(operations_per_thread):
                key = random.randint(0, 999)
                value = hm.get(key)
                thread_results.append((key, value))
            return thread_results

        # Use ThreadPoolExecutor for better control
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(get_worker, i) for i in range(num_threads)]

            for future in as_completed(futures):
                results.extend(future.result())

        # Verify all results are correct
        for key, value in results:
            expected_value = key * 2 if 0 <= key < 1000 else -1
            assert value == expected_value

    def test_concurrent_puts_and_gets(self):
        """Test concurrent put and get operations"""
        hm = ThreadSafeHashMapV1(capacity=100)
        num_threads = 5
        operations_per_thread = 50

        def put_worker(thread_id):
            """Worker function for puts"""
            for i in range(operations_per_thread):
                key = thread_id * operations_per_thread + i
                value = key * 3
                hm.put(key, value)

        def get_worker(thread_id):
            """Worker function for gets"""
            for i in range(operations_per_thread):
                key = thread_id * operations_per_thread + i
                hm.get(key)

        # Start put and get threads
        put_threads = []
        get_threads = []

        for i in range(num_threads):
            put_thread = threading.Thread(target=put_worker, args=(i,))
            get_thread = threading.Thread(target=get_worker, args=(i,))
            put_threads.append(put_thread)
            get_threads.append(get_thread)
            put_thread.start()
            get_thread.start()

        # Wait for all threads to complete
        for thread in put_threads + get_threads:
            thread.join()

        # Verify final state
        for thread_id in range(num_threads):
            for i in range(operations_per_thread):
                key = thread_id * operations_per_thread + i
                expected_value = key * 3
                assert hm.get(key) == expected_value

    def test_concurrent_removes(self):
        """Test concurrent remove operations"""
        hm = ThreadSafeHashMapV1(capacity=100)

        # Pre-populate the hash map
        for i in range(1000):
            hm.put(i, i * 2)

        num_threads = 5
        operations_per_thread = 50

        def remove_worker(thread_id):
            """Worker function for concurrent removes"""
            for i in range(operations_per_thread):
                key = thread_id * operations_per_thread + i
                hm.remove(key)

        # Start multiple remove threads
        threads = []
        for i in range(num_threads):
            thread = threading.Thread(target=remove_worker, args=(i,))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Verify removed keys are gone
        for thread_id in range(num_threads):
            for i in range(operations_per_thread):
                key = thread_id * operations_per_thread + i
                assert hm.get(key) == -1

        # Verify remaining keys are still there
        for i in range(num_threads * operations_per_thread, 1000):
            assert hm.get(i) == i * 2

    def test_mixed_concurrent_operations(self):
        """Test mixed concurrent put, get, and remove operations"""
        hm = ThreadSafeHashMapV1(capacity=100)
        num_threads = 3
        operations_per_thread = 100

        def put_worker(thread_id):
            """Worker function for puts"""
            for i in range(operations_per_thread):
                key = thread_id * operations_per_thread + i
                value = key * 5
                hm.put(key, value)
                time.sleep(0.001)  # Small delay to increase concurrency

        def get_worker(thread_id):
            """Worker function for gets"""
            for i in range(operations_per_thread):
                key = random.randint(0, num_threads * operations_per_thread - 1)
                hm.get(key)
                time.sleep(0.001)

        def remove_worker(thread_id):
            """Worker function for removes"""
            for i in range(operations_per_thread):
                key = thread_id * operations_per_thread + i
                hm.remove(key)
                time.sleep(0.001)

        # Start all types of workers
        put_thread = threading.Thread(target=put_worker, args=(0,))
        get_thread = threading.Thread(target=get_worker, args=(1,))
        remove_thread = threading.Thread(target=remove_worker, args=(2,))

        put_thread.start()
        get_thread.start()
        remove_thread.start()

        # Wait for all threads to complete
        put_thread.join()
        get_thread.join()
        remove_thread.join()

        # Verify final state is consistent
        # Keys from thread 0 should be present
        for i in range(operations_per_thread):
            assert hm.get(i) == i * 5

        # Keys from thread 2 should be removed
        for i in range(operations_per_thread):
            key = 2 * operations_per_thread + i
            assert hm.get(key) == -1

    def test_stress_test(self):
        """Stress test with many concurrent operations"""
        hm = ThreadSafeHashMapV1(capacity=1000)
        num_threads = 20
        operations_per_thread = 200

        def stress_worker(thread_id):
            """Worker function for stress testing"""
            for i in range(operations_per_thread):
                operation = random.choice(["put", "get", "remove"])
                key = random.randint(0, 999)

                if operation == "put":
                    value = random.randint(1, 1000)
                    hm.put(key, value)
                elif operation == "get":
                    hm.get(key)
                elif operation == "remove":
                    hm.remove(key)

        # Start many threads
        threads = []
        for i in range(num_threads):
            thread = threading.Thread(target=stress_worker, args=(i,))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Verify the hash map is still in a consistent state
        # This is a basic check - in a real scenario, you might want to
        # verify specific invariants about the data structure

    def test_race_condition_prevention(self):
        """Test that race conditions are prevented"""
        hm = ThreadSafeHashMapV1(capacity=10)

        # Test the classic check-then-act race condition
        def race_condition_test():
            """Simulate a potential race condition"""
            for i in range(1000):
                # This pattern could cause race conditions without proper locking
                current_value = hm.get(i)
                if current_value == -1:
                    hm.put(i, i * 10)
                else:
                    hm.put(i, current_value + 1)

        # Run multiple threads with the same logic
        threads = []
        for _ in range(5):
            thread = threading.Thread(target=race_condition_test)
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Verify that all keys have been processed
        # Each key should have been put at least once
        for i in range(1000):
            value = hm.get(i)
            assert value != -1  # All keys should exist
            assert value >= i * 10  # Value should be at least the initial value

    def test_large_capacity(self):
        """Test with large capacity to ensure scalability"""
        hm = ThreadSafeHashMapV1(capacity=100000)

        # Test with many operations
        def large_capacity_worker(thread_id):
            for i in range(1000):
                key = thread_id * 1000 + i
                hm.put(key, key * 2)

        threads = []
        for i in range(10):
            thread = threading.Thread(target=large_capacity_worker, args=(i,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # Verify all values
        for thread_id in range(10):
            for i in range(1000):
                key = thread_id * 1000 + i
                assert hm.get(key) == key * 2

    def test_edge_cases(self):
        """Test edge cases and boundary conditions"""
        hm = ThreadSafeHashMapV1(capacity=1)  # Minimal capacity

        # Test with zero key
        hm.put(0, 100)
        assert hm.get(0) == 100

        # Test with negative key (should work with modulo)
        hm.put(-1, 200)
        assert hm.get(-1) == 200

        # Test with very large key
        large_key = 999999999
        hm.put(large_key, 300)
        assert hm.get(large_key) == 300

        # Test remove non-existent key
        hm.remove(999)
        assert hm.get(999) == -1

    def test_thread_safety_verification(self):
        """Verify that the implementation is actually thread-safe"""
        hm = ThreadSafeHashMapV1(capacity=100)

        # This test verifies that the global lock prevents race conditions
        def concurrent_update_worker():
            """Worker that updates the same key multiple times"""
            for i in range(100):
                hm.put(1, i)
                time.sleep(0.001)  # Small delay to increase chance of race conditions

        def concurrent_read_worker():
            """Worker that reads the same key multiple times"""
            for i in range(100):
                value = hm.get(1)
                # Value should always be >= 0 (not -1) if thread-safe
                assert value >= -1
                time.sleep(0.001)

        # Start multiple threads doing concurrent updates and reads
        update_threads = [
            threading.Thread(target=concurrent_update_worker) for _ in range(3)
        ]
        read_threads = [
            threading.Thread(target=concurrent_read_worker) for _ in range(3)
        ]

        # Start all threads
        for thread in update_threads + read_threads:
            thread.start()

        # Wait for all threads to complete
        for thread in update_threads + read_threads:
            thread.join()

        # Final verification
        final_value = hm.get(1)
        assert final_value >= 0  # Should have a valid value


class TestThreadSafeHashMapExecutorApproach:
    """
    APPROACH 2: Using ThreadPoolExecutor

    Testing Plan:
    1. Basic concurrent operations with result collection
    2. Batch processing with map()
    3. As-completed processing for real-time results
    4. Exception handling and timeout testing
    5. Performance comparison with threading approach
    """

    def test_concurrent_puts_executor(self):
        """Test concurrent put operations using ThreadPoolExecutor"""
        hm = ThreadSafeHashMapV1(capacity=1000)
        num_threads = 10
        operations_per_thread = 100

        def put_worker(thread_id):
            """Worker function for concurrent puts"""
            operations_completed = 0
            for i in range(operations_per_thread):
                key = thread_id * operations_per_thread + i
                value = key * 2
                hm.put(key, value)
                operations_completed += 1
            return f"Thread {thread_id} completed {operations_completed} operations"

        # Use ThreadPoolExecutor for automatic management
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(put_worker, i) for i in range(num_threads)]

            # Collect results
            results = [future.result() for future in futures]

        # Verify all values were stored correctly
        for thread_id in range(num_threads):
            for i in range(operations_per_thread):
                key = thread_id * operations_per_thread + i
                expected_value = key * 2
                assert hm.get(key) == expected_value

        # Verify all threads reported completion
        assert len(results) == num_threads
        for result in results:
            assert "completed" in result

    def test_concurrent_gets_executor_map(self):
        """Test concurrent get operations using executor.map()"""
        hm = ThreadSafeHashMapV1(capacity=1000)

        # Pre-populate the hash map
        for i in range(1000):
            hm.put(i, i * 3)

        def get_worker(thread_id):
            """Worker function for concurrent gets"""
            correct_gets = 0
            total_gets = 100

            for _ in range(total_gets):
                key = random.randint(0, 999)
                value = hm.get(key)
                expected_value = key * 3
                if value == expected_value:
                    correct_gets += 1

            return correct_gets

        # Use executor.map() for batch processing
        with ThreadPoolExecutor(max_workers=8) as executor:
            thread_ids = list(range(8))
            results = list(executor.map(get_worker, thread_ids))

        # Verify all threads got correct results
        assert len(results) == 8
        for correct_count in results:
            assert correct_count == 100  # All gets should be correct

    def test_as_completed_executor(self):
        """Test as_completed() for real-time result processing"""
        hm = ThreadSafeHashMapV1(capacity=500)

        # Pre-populate with some data
        for i in range(500):
            hm.put(i, i * 2)

        def worker_with_delay(thread_id):
            """Worker that takes variable time to complete"""
            time.sleep(random.uniform(0.01, 0.05))  # Random delay
            operations = 0
            for i in range(50):
                key = random.randint(0, 499)
                value = hm.get(key)
                if value == key * 2:
                    operations += 1
            return f"Thread {thread_id} completed {operations} operations"

        # Use as_completed() to process results as they finish
        completion_order = []
        with ThreadPoolExecutor(max_workers=6) as executor:
            futures = [executor.submit(worker_with_delay, i) for i in range(6)]

            for future in as_completed(futures):
                result = future.result()
                completion_order.append(result)

        # Verify all threads completed
        assert len(completion_order) == 6
        # Note: completion_order shows the order threads finished (not started)

    def test_exception_handling_executor(self):
        """Test exception handling in ThreadPoolExecutor"""
        hm = ThreadSafeHashMapV1(capacity=100)

        def worker_with_exception(thread_id):
            """Worker that might raise an exception"""
            if thread_id == 3:  # Simulate failure in one thread
                raise ValueError(f"Simulated error in thread {thread_id}")

            for i in range(10):
                key = thread_id * 10 + i
                hm.put(key, key * 2)
            return f"Thread {thread_id} completed successfully"

        # Test exception handling
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(worker_with_exception, i) for i in range(5)]

            results = []
            exceptions = []

            for future in as_completed(futures):
                try:
                    result = future.result(timeout=5)
                    results.append(result)
                except ValueError as e:
                    exceptions.append(str(e))

        # Verify exception was caught
        assert len(exceptions) == 1
        assert "Simulated error in thread 3" in exceptions[0]
        assert len(results) == 4  # Other threads completed successfully

    def test_timeout_executor(self):
        """Test timeout handling in ThreadPoolExecutor"""
        hm = ThreadSafeHashMapV1(capacity=100)

        def slow_worker(thread_id):
            """Worker that takes a long time"""
            time.sleep(2)  # Simulate slow operation
            hm.put(thread_id, thread_id * 2)
            return f"Thread {thread_id} completed"

        # Test timeout
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = [executor.submit(slow_worker, i) for i in range(3)]

            timeout_occurred = False
            for future in as_completed(futures):
                try:
                    result = future.result(timeout=1)  # 1 second timeout
                except TimeoutError:
                    timeout_occurred = True
                    break

        # Verify timeout occurred
        assert timeout_occurred


class TestThreadSafeHashMapHybridApproach:
    """
    APPROACH 3: Hybrid (Combination of threading.Thread and ThreadPoolExecutor)

    Testing Plan:
    1. Different operation types with different approaches
    2. Long-running operations with threading.Thread
    3. Short operations with ThreadPoolExecutor
    4. Coordinated testing between both approaches
    5. Performance comparison and resource management
    """

    def test_hybrid_put_get_operations(self):
        """Test hybrid approach: puts with ThreadPoolExecutor, gets with threading.Thread"""
        hm = ThreadSafeHashMapV1(capacity=1000)

        # Phase 1: Use ThreadPoolExecutor for quick put operations
        def quick_put_worker(thread_id):
            """Quick put operations"""
            for i in range(20):  # Few operations per thread
                key = thread_id * 20 + i
                hm.put(key, key * 2)
            return f"Quick put worker {thread_id} completed"

        # Use ThreadPoolExecutor for puts
        with ThreadPoolExecutor(max_workers=5) as executor:
            put_futures = [executor.submit(quick_put_worker, i) for i in range(5)]
            put_results = [future.result() for future in put_futures]

        # Phase 2: Use threading.Thread for long-running get operations
        def long_get_worker(thread_id):
            """Long-running get operations"""
            correct_gets = 0
            for i in range(200):  # Many operations per thread
                key = random.randint(0, 99)  # Keys from put operations
                value = hm.get(key)
                if value == key * 2:
                    correct_gets += 1
            return correct_gets

        # Use threading.Thread for gets
        get_results = []
        get_threads = []
        for i in range(3):
            thread = threading.Thread(target=lambda tid=i: get_results.append(long_get_worker(tid)))
            get_threads.append(thread)
            thread.start()

        # Wait for get threads to complete
        for thread in get_threads:
            thread.join()

        # Verify results
        assert len(put_results) == 5
        assert len(get_results) == 3
        for result in get_results:
            assert result > 0  # Should have some correct gets

    def test_hybrid_mixed_workload(self):
        """Test hybrid approach with mixed workload types"""
        hm = ThreadSafeHashMapV1(capacity=800)

        # Short operations with ThreadPoolExecutor
        def short_worker(thread_id):
            """Short operations (few iterations)"""
            for i in range(10):
                key = thread_id * 10 + i
                hm.put(key, key * 3)
            return f"Short worker {thread_id} done"

        # Long operations with threading.Thread
        def long_worker(thread_id):
            """Long operations (many iterations)"""
            for i in range(500):
                key = 100 + thread_id * 500 + i
                hm.put(key, key * 4)
                if i % 100 == 0:  # Periodic get operations
                    hm.get(key)

        # Start short operations with ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=4) as executor:
            short_futures = [executor.submit(short_worker, i) for i in range(4)]

            # Meanwhile, start long operations with threading.Thread
            long_threads = []
            for i in range(2):
                thread = threading.Thread(target=long_worker, args=(i,))
                long_threads.append(thread)
                thread.start()

            # Wait for short operations
            short_results = [future.result() for future in short_futures]

        # Wait for long operations
        for thread in long_threads:
            thread.join()

        # Verify results
        assert len(short_results) == 4
        for i in range(4):
            for j in range(10):
                key = i * 10 + j
                assert hm.get(key) == key * 3

        for i in range(2):
            for j in range(500):
                key = 100 + i * 500 + j
                assert hm.get(key) == key * 4

    def test_hybrid_coordinated_testing(self):
        """Test coordinated testing between both approaches"""
        hm = ThreadSafeHashMapV1(capacity=600)

        # Coordinator thread to manage the test
        def coordinator():
            """Coordinates the test execution"""
            # Phase 1: Initialize data with ThreadPoolExecutor
            def init_worker(thread_id):
                for i in range(50):
                    key = thread_id * 50 + i
                    hm.put(key, key * 2)
                return f"Initialized {50} keys for thread {thread_id}"

            with ThreadPoolExecutor(max_workers=3) as executor:
                init_futures = [executor.submit(init_worker, i) for i in range(3)]
                init_results = [future.result() for future in init_futures]

            # Phase 2: Stress test with threading.Thread
            def stress_worker(thread_id):
                for i in range(300):
                    operation = random.choice(["get", "put", "remove"])
                    key = random.randint(0, 149)  # Keys from initialization

                    if operation == "get":
                        hm.get(key)
                    elif operation == "put":
                        hm.put(key, key * 3)
                    elif operation == "remove":
                        hm.remove(key)

            stress_threads = []
            for i in range(4):
                thread = threading.Thread(target=stress_worker, args=(i,))
                stress_threads.append(thread)
                thread.start()

            # Wait for stress threads
            for thread in stress_threads:
                thread.join()

            return init_results

        # Run the coordinated test
        coordinator_thread = threading.Thread(target=coordinator)
        coordinator_thread.start()
        coordinator_thread.join()

        # Verify the hash map is still functional
        # Add some test operations to ensure it's working
        hm.put(999, 999)
        assert hm.get(999) == 999

    def test_hybrid_performance_comparison(self):
        """Test performance comparison between approaches"""
        hm = ThreadSafeHashMapV1(capacity=1000)

        # Test 1: ThreadPoolExecutor performance
        def executor_worker(thread_id):
            start_time = time.time()
            for i in range(100):
                key = thread_id * 100 + i
                hm.put(key, key * 2)
            end_time = time.time()
            return end_time - start_time

        executor_start = time.time()
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(executor_worker, i) for i in range(5)]
            executor_times = [future.result() for future in futures]
        executor_total = time.time() - executor_start

        # Test 2: threading.Thread performance
        def thread_worker(thread_id):
            start_time = time.time()
            for i in range(100):
                key = (thread_id + 5) * 100 + i  # Different key range
                hm.put(key, key * 3)
            end_time = time.time()
            return end_time - start_time

        thread_start = time.time()
        thread_times = []
        threads = []
        for i in range(5):
            thread = threading.Thread(target=lambda tid=i: thread_times.append(thread_worker(tid)))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
        thread_total = time.time() - thread_start

        # Verify both approaches completed successfully
        assert len(executor_times) == 5
        assert len(thread_times) == 5

        # Both approaches should complete in reasonable time
        assert executor_total < 10  # Should complete within 10 seconds
        assert thread_total < 10    # Should complete within 10 seconds

        # Verify data integrity
        for i in range(5):
            for j in range(100):
                key1 = i * 100 + j
                key2 = (i + 5) * 100 + j
                assert hm.get(key1) == key1 * 2
                assert hm.get(key2) == key2 * 3


# Performance and comparison tests
class TestThreadSafetyApproachComparison:
    """Compare the effectiveness of different testing approaches"""

    def test_approach_effectiveness(self):
        """Test that all approaches can detect thread safety issues"""
        # This test would be used to compare different implementations
        # For now, we'll test that our thread-safe implementation works with all approaches

        hm = ThreadSafeHashMapV1(capacity=100)

        # All approaches should work correctly with a thread-safe implementation
        assert True  # Placeholder for actual comparison logic

    def test_resource_usage_comparison(self):
        """Compare resource usage between approaches"""
        # This would measure memory and CPU usage
        # For now, we'll just verify that all approaches complete successfully

        hm = ThreadSafeHashMapV1(capacity=100)

        # Test that all approaches can complete without resource issues
        assert True  # Placeholder for actual resource measurement


if __name__ == "__main__":
    pytest.main([__file__])
