"""
%load_ext autoreload
%autoreload 2
"""
import matplotlib.pyplot as plt
import numpy as np


import logging

import yass
from yass import preprocess
from yass.explore import RecordingExplorer

# configure logging module to get useful information
logging.basicConfig(level=logging.INFO)

# set yass configuration parameters
yass.set_config('config/threshold100k.yaml')
# yass.set_config('config/threshold.yaml')

# run preprocessor
scores, spike_index_clear, spike_index_collision = preprocess.run()

scores.shape
spike_index_clear.shape
spike_index_collision.shape