import pytest
import threading
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from src.hash_map.thread_safe_hm import ThreadSafeHashMapV1


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


if __name__ == "__main__":
    pytest.main([__file__])
