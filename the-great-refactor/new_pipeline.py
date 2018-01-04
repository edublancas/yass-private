# batch-processing refactoring
"""
cd /Users/Edu/dev/lab/yass
git checkout dev
cd /Users/Edu/dev/lab/private-yass/the-great-refactor
source activate yass
ipython
"""
import logging

import yass
from yass import preprocess
from yass import process
from yass import deconvolute

SAMPLE = False

assert yass.__version__ == '0.4dev'

# configure logging module to get useful information
logging.basicConfig(level=logging.DEBUG)

# set yass configuration parameters
if SAMPLE:
    yass.set_config('threshold100k.yaml')
else:
    yass.set_config('threshold.yaml')

# run preprocessor
score, spike_index_clear, spike_index_collision = preprocess.run()

score.shape, spike_index_clear.shape, spike_index_collision.shape

# run processor
spike_train, spikes_left, templates = process.run(score, spike_index_clear,
                                                  spike_index_collision)

spike_train.shape, spikes_left.shape, templates.shape

# run deconvolution
spikes = deconvolute.run(spike_train, spikes_left, templates)

spikes.shape