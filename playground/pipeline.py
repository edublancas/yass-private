"""
%load_ext autoreload
%autoreload 2
"""

import logging

import yass
from yass import preprocess

# configure logging module to get useful information
logging.basicConfig(level=logging.INFO)

# set yass configuration parameters
yass.set_config('config/threshold100k.yaml')
# yass.set_config('config/threshold.yaml')

# run preprocessor
spikes, suff_stats, spikes_per_channel, rotation = preprocess.run()
