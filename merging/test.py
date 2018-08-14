import logging

import yass
from yass import preprocess
# from yass import detect
# from yass import cluster
# from yass import deconvolute

# configure logging module to get useful information
logging.basicConfig(level=logging.INFO)

# set yass configuration parameters
yass.set_config('/home/Edu/dev/private-yass/config/49-lab.yaml')
yass.set_config('/home/Edu/dev/private-yass/config/512-10min-lab.yaml')

%%timeit -n 1 -r 1
_ = preprocess.run(output_directory='merging/',
                   if_file_exists='overwrite')


(spike_index_clear,
 spike_index_all) = detect.run(standarized_path,
                               standarized_params,
                               channel_index,
                               whiten_filter)


spike_train, tmp_loc, templates = cluster.run(spike_index_clear)

spike_train = deconvolute.run(spike_index_all, templates)
