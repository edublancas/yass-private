"""
https://roman-kh.github.io/numpy-multicore/
"""
import numpy as np
size = 10000
a = np.random.random_sample((size, size))
b = np.random.random_sample((size, size))
n = np.dot(a,b)
