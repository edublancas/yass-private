"""
cd /ssd/data/eduardo/tmp
source activate yass-stable
ipython
"""
import numpy as np
import yass
from yass import deconvolute

assert yass.__version__ == '0.4'

yass.set_config('config.yaml')

spike_train_clear = np.empty((0, 2))
templates = np.load('templates.npy')
spike_index_collision = np.load('spike_index_collision.npy')[:5000, ]

# master - looks for root/tmp/whiten.bin
res = deconvolute.run(spike_train_clear, templates, spike_index_collision)

res.shape
