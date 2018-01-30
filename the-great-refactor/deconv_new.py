"""
cd /ssd/data/eduardo/tmp
source activate yass
ipython
"""
import numpy as np
import yass
from yass import deconvolute

assert yass.__version__ == '0.4dev'

yass.set_config('config.yaml')

spike_train_clear = np.empty((0, 2))
templates = np.load('templates.npy')
spike_index_collision = np.load('spike_index_collision.npy')[:100000, ]

spike_train_clear.shape
templates.shape
spike_index_collision.shape

res = deconvolute.run(spike_train_clear, templates, spike_index_collision,
                      output_directory='tmp/',
                      recordings_filename='standarized.bin')

res.shape
