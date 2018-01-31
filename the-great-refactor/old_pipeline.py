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

SAMPLE = False
NNET = True
REMOTE = True

assert yass.__version__ == '0.4'

# set yass configuration parameters
if SAMPLE:
    config = 'nnet100k' if NNET else 'threshold100k'
else:
    config = 'nnet' if NNET else 'threshold'


config = config+'-remote.yaml' if REMOTE else config+'.yaml'

cfg = yass.Config.from_yaml(config)

pp = Preprocessor(cfg)
score, spike_index_clear, spike_index_collision = pp.process()

score.shape, spike_index_clear.shape, spike_index_collision.shape


mp = Mainprocessor(cfg, score, spike_index_clear, spike_index_collision)
spike_train_clear, spike_index_collision = mp.mainProcess()

spike_train_clear.shape, mp.templates.shape, spike_index_collision.shape


dc = Deconvolution(cfg, np.transpose(mp.templates, [1, 0, 2]),
                   spike_index_collision)
spike_train_col = dc.fullMPMU()

spikeTrain = np.concatenate((spike_train_col, spike_train_clear))
idx_sort = np.argsort(spikeTrain[:, 0])
spikeTrain = spikeTrain[idx_sort]

idx_keep = np.zeros(spikeTrain.shape[0], 'bool')

for k in range(mp.templates.shape[2]):
    idx_c = np.where(spikeTrain[:, 1] == k)[0]
    idx_keep[idx_c[np.concatenate(
        ([True], np.diff(spikeTrain[idx_c, 0]) > 1))]] = 1

spike_train = spikeTrain[idx_keep]

spike_train.shape
