"""
cd /Users/Edu/dev/lab/private-yass/the-great-refactor
# conda create --name yass-stable python=3.6 -y
source activate yass-stable
# pip install yass-algorithm ipython
ipython
"""
import numpy as np

import yass
from yass.preprocessing import Preprocessor
from yass.mainprocess import Mainprocessor
from yass.deconvolute import Deconvolution

SAMPLE = True
NNET = False
REMOTE = True

assert yass.__version__ == '0.3'

# set yass configuration parameters
if SAMPLE:
    config = 'nnet100k' if NNET else 'threshold100k'
else:
    config = 'nnet' if NNET else 'threshold'


config = config+'-remote.yaml' if REMOTE else config+'.yaml'

cfg = yass.Config.from_yaml

pp = Preprocessor(cfg)
score, spike_index_clear, spike_index_collision = pp.process()

score.shape, spike_index_clear.shape, spike_index_collision.shape


mp = Mainprocessor(cfg, score, spike_index_clear, spike_index_collision)
spike_train_clear, spike_index_collision = mp.mainProcess()

spike_train_clear.shape, spike_index_collision.shape


dc = Deconvolution(cfg, np.transpose(mp.templates, [1, 0, 2]),
                   spike_index_collision)
spike_train = dc.fullMPMU()

spike_train.shape

import os.path as path

path_to_spike_train = path.join(cfg.data.root_folder, 'tmp/spike_train.npy')
np.save(path_to_spike_train, spike_train)

path_to_middle_spike_train = path.join(cfg.data.root_folder, 'tmp/middle_spike_train.npy')
idx = np.logical_and(spike_train[:, 0] > 20, spike_train[:, 0] < 5999980)
middle_spike_train = spike_train[idx, :]
np.save(path_to_middle_spike_train, middle_spike_train)
