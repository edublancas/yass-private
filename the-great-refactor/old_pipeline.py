# version 0.3
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

assert yass.__version__ == '0.3'

cfg = yass.Config.from_yaml('threshold100k.yaml')

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
