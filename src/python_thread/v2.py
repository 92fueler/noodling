import threading
import time
from concurrent.futures import ThreadPoolExecutor


def myFunc(name):
    print(f"myFunc started: {name}")
    time.sleep(2)
    print(f"myFunc finished: {name}")
    return True


# if __name__ == "__main__":
#     threads = []
#     for i in range(5):
#         t = threading.Thread(target=myFunc, args=[f"thread {i}"])
#         threads.append(t)
#         t.start()

#     for idx, t in enumerate(threads):
#         print(f"main thread waiting for thread {idx} to finish")
#         t.join()
#         print(f"thread {idx} finished")

#     print("main finished")

"""
concurrent.futures.ThreadPoolExecutor
- a higher level interface for threading
- creates a context manager that can be used to create a pool of threads
- .map() method to apply a function to a list of arguments
"""
# if __name__ == "__main__":
#     with ThreadPoolExecutor(max_workers=5) as executor:
#         executor.map(
#             myFunc, [f'Thread {i}' for i in range(5)]
#         )

#     print("main finished")

"""
launch a group of threads
how to track the progress of the threads
- get the result
- get the errors if any
- get the status of the threads

Using .submit() or .map() to launch a group of threads (don't need to use .start())
The executor manages the threads for you: create, start, reuses threads as needed
"""
if __name__ == "__main__":
    futures = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(5):
            future = executor.submit(myFunc, f"Thread {i}")
            futures.append((i, future))

        for idx, future in futures:
            print(f"Thread {idx} started.")

        # Track progress as threads complete
        for idx, future in futures:
            print(f"Thread {idx} done? {future.done()}")  # likely False at this point

        for idx, future in futures:
            try:
                result = future.result()  # blocks until this thread is done
                print(f"Thread {idx} result: {result}")
            except Exception as e:
                print(f"Thread {idx} raised an error: {e}")

        # Or, process as they complete (order may differ)
        # for future in as_completed([f for _, f in futures]):
        #     idx = [i for i, f in futures if f == future][0]
        #     try:
        #         result = future.result()
        #         print(f"Thread {idx} result: {result}")
        #     except Exception as e:
        #         print(f"Thread {idx} raised an error: {e}")

    print("main finished")
