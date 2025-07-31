import os
import psutil
import gc

class MemoryChecker():
    """
    Callable class to get current memory use of program.

    Instances of this class may be called, at which time
    they will return current memory use.
    """

    def __init__(self):
        self.process = psutil.Process(os.getpid())  # Get PID of current process

    def __call__(self):
        return self.process.memory_info().rss  # Return memory use for PID

if __name__ == '__main__':
    import time
    mc = MemoryChecker()
    print(mc())  # can call at any time to get current memory use
    x = [True] * 10_000_000
    print(mc())
    del x
    gc.collect()
    print(mc())
