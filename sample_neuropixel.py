import os.path as path

import numpy as np

from yass.preprocess import butterworth, standarize
from yass.batch.pipeline import BatchPipeline, PipedTransformation

PATH_TO_DATA = path.join(path.expanduser('~'), 'data/ucl-neuropixel')

ch = np.load(path.join(PATH_TO_DATA, 'channel_positions.npy'))
n_ch, _ = ch.shape

d = np.fromfile(path.join(PATH_TO_DATA, 'rawDataSample.bin'), dtype='int16')
d = d.reshape((385, 1800000))

sample = d[:10, :10000].T
sample.tofile('data/neuropixel.bin')

np.save('data/neuropixel_channels.npy', ch[:10, :])

pipeline = BatchPipeline('data/neuropixel.bin', dtype='int16',
                         n_channels=10, data_format='long',
                         max_memory='500MB',
                         output_path='data/')

butterworth_op = PipedTransformation(butterworth, 'filtered.bin',
                                     mode='single_channel_one_batch',
                                     cast_dtype='float32',
                                     keep=True, low_freq=300, high_factor=0.1,
                                     order=3, sampling_freq=30000)

standarize_op = PipedTransformation(standarize, 'standarized.bin',
                                    cast_dtype='float32',
                                    mode='single_channel_one_batch',
                                    keep=True, sampling_freq=30000)

pipeline.add([butterworth_op, standarize_op])

pipeline.run()
