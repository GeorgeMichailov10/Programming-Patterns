from threading import Thread, Lock

buffer = []
lock = Lock()

def producer():
    global buffer
    for i in range(5):
        with lock:
            buffer.append(i)
            print(f'Produced {i}')

def consumer():
    global buffer
    for i in range(5):
        with lock:
            if buffer:
                item = buffer.pop(0)
                print(f'Consumed {item}')

# Problematic
p = Thread(target=producer)
c = Thread(target=consumer)
c.start()
p.start()

p.join()
c.join()