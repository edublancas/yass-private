import logging

import matplotlib.pyplot as plt

from yass.batch.new import BatchProcessor
from yass.batch import RecordingsReader
from yass.preprocess.filter import butterworth_single_channel


logging.basicConfig(level=logging.DEBUG)


path_to_data = '/hdd/data/peter/ej_latest/data004.dat'
path_to_filtered_data = '/hdd/data/peter/ej_latest/filtered.dat'

# create batch processor for the data
bp = BatchProcessor(path_to_data,
                    dtype='int16', n_channels=512, data_format='long',
                    max_memory='10MB')

# appply a single channel transformation, each batch will be all observations
# from one channel
bp.single_channel_apply(butterworth_single_channel, path_to_filtered_data,
                        force_complete_channel_batch=False,
                        channels='all',
                        low_freq=300, high_factor=0.1,
                        order=3, sampling_freq=30000)

# let's visualize the results
raw = RecordingsReader(path_to_data, dtype='int16',
                       n_channels=512, data_format='long')

# you do not need to specify the format since single_channel_apply
# saves a yaml file with such parameters
filtered = RecordingsReader(path_to_filtered_data)

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(raw[:2000, 0])
ax2.plot(filtered[:2000, 0])
plt.show()
