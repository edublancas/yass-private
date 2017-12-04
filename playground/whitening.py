import os
import numpy as np
import matplotlib.pyplot as plt

from yass.preprocess import whitening
from yass import geometry

root = '/Users/Edu/data/yass'

path_to_data = os.path.join(root, 'ej49_data1_set1.bin')
path_to_geom = os.path.join(root, 'ej49_geometry1.txt')

n_channels = 49

rec = np.fromfile(path_to_data, dtype='int16').reshape(6000000, n_channels)
rec.shape

geom = geometry.parse(path_to_geom, n_channels)
neighbors = geometry.find_channel_neighbors(geom, radius=70)

Q = whitening.whitening_matrix(rec, neighbors, 15)
Q.shape

whitened = whitening.whitening(rec, Q)
whitened.shape

plt.plot(rec[:10000, 0])
plt.show()

plt.plot(whitened[:10000, 0])
plt.show()
