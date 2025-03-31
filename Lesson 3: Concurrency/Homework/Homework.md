Given the following scenarios, explain which method is best for each scenario and explain why.

1. A web scraper needs to send HTTP requests to multiple websites and process the results as they arrive. The workload is mostly waiting for network responses.

Async, because you can still do other stuff while waiting for the network responses

2. You need to perform a lot of calculations on large arrays.

Multiprocessing, because it speeds up CPU heavy tasks, while threading and async aren't good for taking large loads.


3. You are building a real-time chat server that needs to handle thousands of simultaneous client connections. However, each connection is mostly idle, waiting for messages.

Async


4. Training a computation heavy ML model.

Multiprocessing, for the same reason as #2.


5. Interacting with an external API, processing the data, and storing the results in a db.

Threading, because it works within same process, so there will be shared state, memory, and resources
Correct: Async, then single/multi threaded/processed, then async again