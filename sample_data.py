"""Sample data
"""

import numpy as np


d = np.fromfile('/users/Edu/data/yass/ej49_data1_set1.bin', dtype='int16')
d = d.reshape(6000000, 49)

d[:1000, 0:7].tofile('sample_data/sample_1k.bin')
d[:10000, 0:7].tofile('sample_data/sample_10k.bin')
d[:100000, 0:7].tofile('sample_data/sample_100k.bin')

d[:, 0:7].tofile('/users/Edu/data/yass/7ch.bin')
