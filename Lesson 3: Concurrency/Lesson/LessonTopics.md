1. Concurrency vs Parallelism
    - Concurrency is multiple tasks.
    - Parallelism is multiple tasks at the same time.
2. Threading vs multiprocessing vs async
    - Threading: Multiple threads within the same process.
    - Multiprocessing: Instances of separate processes, each with its own memory and resources.
    - Async - Single threaded event loop for multitasking.
3. Threading in Python
    - Global Interpreter Lock blocks parallel execution of threads so multitasks, but saves no time. 
    - Best for I/O tasks, API requests, db queries.
    - Bad for CPU heavy operations.
4. Multiprocessing in Python
    - Bypass Global Interpreter Lock by running tasks in separate processes
    - Greate for CPU heavy tasks.
    - Ray remote library.
    - Not great for shared memory tasks, but it can be done.
5. Asyncio in Python
    - Use event loop and coroutines to run tasks concurrently.
    - Good for webscraping, db queries.
    - Bad for CPU heavy tasks.