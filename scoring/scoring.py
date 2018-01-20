import os.path as path
import numpy as np

rot_pca = np.load(path.join('tmp-new-threshold/rotation.npy'))
rot_net = np.load(path.join('tmp-new-nnet/rotation.npy'))

templates = np.load(path.join('tmp-new-nnet/templates.npy'))
waveforms = np.load(path.join('tmp-new-threshold/waveforms_clear.npy'))

# (temp features, reduced features, channels)
rot_pca.shape

# (temp features, reduced features)
rot_net.shape

# (channels, temp features, n templates) - this is ok
templates.shape

# (n waveforms, temp features, channels) - we should transpose this
# to be consistent with waveforms - need to change explorer,
# however, this make sense for np.matmul as it threats 3D arrays as stacked
# matrices in the last two indexes
waveforms.shape

# scoring with net
score_net = np.matmul(rot_net.T, waveforms)

waveforms.shape
score_net.shape

# scoring with pca
rot_ = np.transpose(rot_pca)
sp = np.transpose(waveforms)

rot_.shape
sp.shape

# compute scores for every spike
score_pca = np.transpose(np.matmul(rot_, sp), (2, 1, 0))
score_pca.shape
