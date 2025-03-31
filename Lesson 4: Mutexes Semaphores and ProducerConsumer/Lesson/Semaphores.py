import threading
import time
import random

buffer = []
buffer_size = 5

# Semaphores
empty = threading.Semaphore(buffer_size)        # Starting allowed passthroughs = buffer_size = 5
full = threading.Semaphore(0)                   # Starting allowed passthroughs = 0
mutex = threading.Lock()                          # Protects global resource so only one thread can access at a time

def producer():
    global buffer
    for i in range(5):
        empty.acquire()                          # Checks that there is space (empty count > 0). If 0, waits for signal (via empty.release()) to continue
        with mutex:                              # Acquire lock
            buffer.append(i)
            print(f'Produced {i}')
        full.release()                           # .release() function signals from semaphore (in this case to indicate that something has been produced)
        time.sleep(random.random())              # To simulate unpredicatbility

def consumer():
    global buffer
    for i in range(5):
        full.acquire()                           # If count in full semaphore = 0, we wait here until we get a signal (done through full.release which would incrmement the count by 1)
        with mutex:                              # Acquire mutex lock
            item = buffer.pop(0)
            print(f'Consumed {item}')
        empty.release()                          # Signal to the empty semaphore that the buffer may now be empty/decrement the count of items in the buffer (kept in empty count) by 1
        time.sleep(random.random())


p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)
p.start()
c.start()
p.join()
c.join()