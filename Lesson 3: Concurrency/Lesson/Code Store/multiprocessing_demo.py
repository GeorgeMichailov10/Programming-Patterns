import ray
import time

@ray.remote(num_cpus=1)
def worker(pid):
    for i in range(99999999):
        continue
    return f"{pid} completed"

start = time.time()
futures = [worker.remote(pid) for pid in range(4)]
results = ray.get(futures)
print(f"Execution time: {time.time() - start:.2f} seconds")

start = time.time()
for i in range(4):
    for j in range(99999999):
        continue
print(f"Execution time: {time.time() - start:.2f} seconds")

# Play around with large counting value. Delay comes from the instantiation of ray


