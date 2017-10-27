import numpy as np
import matplotlib.pyplot as plt

ch = np.load('channel_positions.npy')
n_ch, _ = ch.shape

d = np.fromfile('rawDataSample.bin', dtype='int16')

n_obs = len(d)

d = d.reshape((385, 1800000))

plt.plot(d[0, :5000])
plt.show()


sample = d[:10, :10000].T
sample.tofile('sample.bin')

np.save('channels.npy', ch[:10, :])

plt.plot(sample[:, 0])
plt.show()
