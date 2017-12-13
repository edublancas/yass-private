"""
%load_ext autoreload
%autoreload 2
"""
import matplotlib.pyplot as plt
import numpy as np


import logging

import yass
from yass import preprocess

# configure logging module to get useful information
logging.basicConfig(level=logging.INFO)

# set yass configuration parameters
yass.set_config('config/threshold100k.yaml')
# yass.set_config('config/threshold.yaml')

# run preprocessor
spike_index, whitened, rotation = preprocess.run()

time, channel = spike_index[1, :]

spike = whitened[time-15:time+16, :]

plt.plot(spike)
plt.show()

spikes = np.stack([spike, spike])
spikes.shape
rotation.shape

# this should be done by the pca matrix function
rot = np.transpose(rotation)
sp = np.transpose(spikes)

reduced = np.transpose(np.matmul(rot, sp), (2, 1, 0))
