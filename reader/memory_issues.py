"""
%load_ext autoreload
%autoreload 2
"""
import logging
from yass.explore import RecordingExplorer

logging.basicConfig(level=logging.INFO)

path_to_data = '/Users/Edu/data/ucl-neuropixel/tmp/whitened.bin'


exp = RecordingExplorer(path_to_data, spike_size=15, waveform_dtype='float16')

times = range(100, 50100)
wfs = exp.read_waveforms(times=times)
