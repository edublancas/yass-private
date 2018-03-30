"""
Memory profiling for the pupeline, looks for a config.yaml file in the
same folder.

See this for usage:

https://github.com/pythonprofilers/memory_profiler

Run with:

mprof run pipeline.py
"""
import logging
import argparse
import mock
from memory_profiler import profile
import yass
from yass import preprocess, detect, cluster, templates, deconvolute


if __name__ == '__main__':
    # configure logging module to get useful information
    logging.basicConfig(level=logging.DEBUG)

    # set yass configuration parameters
    yass.set_config('config.yaml')

    (standarized_path, standarized_params, channel_index,
     whiten_filter) = preprocess.run()

    (score, spike_index_clear,
     spike_index_all) = profile(detect.run)(standarized_path,
                                   standarized_params,
                                   channel_index,
                                   whiten_filter)

    spike_train_clear = profile(cluster.run)(score, spike_index_clear)

    templates = profile(templates.run)(spike_train_clear)

    spike_train = profile(deconvolute.run)(spike_index_all, templates)
