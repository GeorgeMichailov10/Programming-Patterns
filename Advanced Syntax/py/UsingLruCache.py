from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# LRU Cache works as a dp array on your behalf freeing memory as needed and can be capped in size for what will be recalculated and what will be used.