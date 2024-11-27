import threading
import time

def task():
    print("Task starting")
    time.sleep(3)  # Simulate I/O-bound operation
    print("Task completed")


start = time.time()

threads = []
for _ in range(5):
    thread = threading.Thread(target=task)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()  # Wait for all threads to finish
print("in", time.time() - start)
print("All tasks are complete.")