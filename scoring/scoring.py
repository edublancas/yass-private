import os.path as path
import numpy as np

from yass.explore import RecordingExplorer

e = RecordingExplorer('ej49_data1_set1.bin', 'ej49_geometry1.txt',
                      spike_size=15, neighbor_radius=70, dtype='int16',
                      n_channels=49, data_format='long', mmap=True)

wfs = e.read_waveforms(times=(100, 200, 300))
# (n waveforms, temp features, channels)
wfs.shape

rot_pca = np.load(path.join('new-threshold/rotation.npy'))
rot_net = np.load(path.join('new-nnet/rotation.npy'))

templates = np.load(path.join('new-nnet/templates.npy'))
waveforms = np.load(path.join('new-threshold/waveforms_clear.npy'))

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

# scoring waveforms with net
score_net = np.matmul(rot_net.T, waveforms)
waveforms.shape
score_net.shape

# scoring templates with net
score_templates_net = np.matmul(rot_net.T, templates)
templates.shape
score_templates_net.shape

# this gives the same result, but may be better to enforce certain dimensions
a = np.matmul(rot_net.T, templates)
b = np.matmul(rot_net.T, templates.transpose((2, 1, 0))).transpose((2, 1, 0))
assert a.shape == b.shape
np.testing.assert_array_equal(a, b)

# scoring waveforms with pca
score_pca = np.matmul(rot_pca.T, waveforms.T).T
waveforms.shape
score_pca.shape

# scoring templates with pca
score_templates_pca = np.matmul(rot_pca.T, templates)
templates.shape
score_templates_pca.shape
