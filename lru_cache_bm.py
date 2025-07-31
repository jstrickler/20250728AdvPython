from timeit import Timer

setup = """
import random
from functools import lru_cache
numbers = [random.randint(1, 10) for _ in range(1000000)]

def doit_without_cache(x):
    return x ** 2

@lru_cache
def doit_with_cache(x):
    return x ** 2
"""

snippet1 = """
for n in numbers:
    doit_without_cache(n)
"""

snippet2 = """
for n in numbers:
    doit_with_cache(n)
doit_with_cache.cache_clear()
"""

t1 = Timer(snippet1, setup=setup)
print(t1.timeit(number=1000))
t2 = Timer(snippet2, setup=setup)
print(t2.timeit(number=1000))
