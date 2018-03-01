import numpy as np
import matplotlib.pyplot as plt

data[:, 0]

bp_arr = BatchProcessor(PATH_TO_DATA, PARAMS['dtype'], PARAMS['n_channels'],
                        PARAMS['data_format'], '100KB',
                        buffer_size=CONFIG.spikeSize,
                        loader='array')

bp_py = BatchProcessor(PATH_TO_DATA, PARAMS['dtype'], PARAMS['n_channels'],
                        PARAMS['data_format'], '100KB',
                        buffer_size=CONFIG.spikeSize,
                        loader='python')


for b in bp_arr.single_channel():
    print(b)


for b in bp_py.single_channel():
    print(b)


d = np.fromfile('ej49_data1_set1.bin', dtype='int16')

plt.plot(d[:200])
plt.show()


a = d.reshape(6000000, 49)


plt.plot(a[:1000, 0])
plt.show()

plt.plot(a[0, :1000])
plt.show()

b = d.reshape(49, 6000000)
