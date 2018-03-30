from memory_profiler import profile
import time

def test1():
    n = 10000
    a = [1] * n
    time.sleep(1)
    return a

def test2():
    n = 100000
    b = [1] * n
    time.sleep(1)
    return b

if __name__ == "__main__":
    profile(test1)()
    profile(test2)()