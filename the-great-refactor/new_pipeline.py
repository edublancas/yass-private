# batch-processing refactoring
"""
cd /Users/Edu/dev/lab/yass
git checkout dev
cd /Users/Edu/dev/lab/private-yass/the-great-refactor
source activate yass
ipython

%load_ext autoreload
%autoreload 2
"""

import logging

import yass
from yass import preprocess
from yass import process
from yass import deconvolute

SAMPLE = False
NNET = False

assert yass.__version__ == '0.4dev'

# configure logging module to get useful information
logging.basicConfig(level=logging.INFO)

# set yass configuration parameters
if SAMPLE:
    yass.set_config('nnet100k.yaml' if NNET else 'threshold100k.yaml')
else:
    yass.set_config('nnet.yaml' if NNET else 'threshold.yaml')

# run preprocessor
score, spike_index_clear, spike_index_collision = preprocess.run()

score.shape, spike_index_clear.shape, spike_index_collision.shape

# run processor
(spike_train_clear, templates,
 spike_index_collision) = process.run(score, spike_index_clear,
                                      spike_index_collision)

spike_train_clear.shape, templates.shape, spike_index_collision.shape

# run deconvolution
spikes = deconvolute.run(spike_train_clear, templates, spike_index_collision)

spikes.shape
