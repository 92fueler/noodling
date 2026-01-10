"""
Concepts:
1. CPU: piece of hardware that can execute instructions
2. OS: handles the scheduling of when the CPU can be used
3. process: a program as it is being executed
4. thread: a single sequence of instructions within a process
5. multiprocessing: running multiple processes at the same time
6. multithreading: running multiple threads at the same time
7. concurrency: the ability of multiple tasks to run in parallel
8. parallelism: the ability of multiple tasks to run at the same time
9. blocking: when a thread is waiting for a resource to be available
10. non-blocking: when a thread is not waiting for a resource to be available
"""

import time
import threading


def myFunc():
    """
    a single-thread application gets blocked
    """
    print("myFunc started")
    time.sleep(1)  # simulate the blocking
    print("myFunc finished")
    return True


def myFunc2(name):
    print(f"myFunc2 started {name}")
    time.sleep(10)
    print(f"myFunc2 finished {name}")
    return True


"""
main can be finished before the thread is finished

In compute science, a daemon is a process that runs in the background.
Python threading has a more specific meaning for daemon.
A daemon thread will shut down immediately when the program exits.

If a program is running Threads that are not daemons, the program will wait for them to finish before exiting.
If a program is running Threads that are daemons, the program will exit even if the threads are not finished.
"""
if __name__ == "__main__":
    print("main started")
    # myFunc()
    t = threading.Thread(target=myFunc2, args=["realpython"])
    # launch thread
    t.start()
    myFunc()
    print("main finished")

"""
A daemon thread with t.join() will wait for the thread to finish before exiting
"""
# if __name__ == "__main__":
#     print("main started")
#     # myFunc()
#     t = threading.Thread(target=myFunc2, args=["realpython"], daemon=True)
#     # launch thread
#     t.start()
#     myFunc()
#     t.join()
#     print("main finished")
