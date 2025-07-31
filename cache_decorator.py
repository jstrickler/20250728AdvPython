from functools import lru_cache, cache

@lru_cache
def double(x):
    return 2 * x
# double = lru_cache(double)

nums = [800, 80, 1000, 32, 80, 80, 80, 800, 5, 5, 5000,  -3, 8, 18, 255, 400, 5, 5000]

for n in nums:
    print(double(n))

print(double.cache_info())
