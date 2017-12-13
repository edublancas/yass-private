# batch-processing refactoring
"""
cd /Users/Edu/dev/lab/yass
git checkout batch-processing
cd /Users/Edu/dev/lab/private-yass/the-great-refactor
source activate yass
ipython
"""
import logging

import yass
from yass import preprocess
from yass import process
from yass import deconvolute

assert yass.__version__ == '0.4dev'

# configure logging module to get useful information
logging.basicConfig(level=logging.INFO)

# set yass configuration parameters
yass.set_config('threshold100k.yaml')

# run preprocessor
score, clr_idx, spt = preprocess.run()

# run processor
spike_train, spikes_left, templates = process.run(score, clr_idx, spt)

# run deconvolution
spikes = deconvolute.run(spike_train, spikes_left, templates)

spikes.shape
