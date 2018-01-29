"""
%load_ext autoreload
%autoreload 2
"""
import numpy as np
import logging
from yass.explore import RecordingExplorer

logging.basicConfig(level=logging.INFO)

path_to_data = '/Users/Edu/data/yass/ej49_data1_set1.bin'
path_to_geom = '/Users/Edu/data/yass/ej49_geometry1.txt'

r = RecordingExplorer(path_to_data, path_to_geom, spike_size=15,
                      neighbor_radius=70, dtype='int16', n_channels=49,
                      data_format='long')

wf = r.read_waveform(time=50)
np.argmax(np.max(wf, axis=0), axis=0)
wf = r.read_waveform(time=100)
np.argmax(np.max(wf, axis=0), axis=0)

wfs = r.read_waveforms(times=[50, 100])
np.argmax(np.max(wfs, axis=1), axis=1)
