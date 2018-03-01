from memory_profiler import profile


import logging

import yass
from yass import preprocess

# configure logging module to get useful information
logging.basicConfig(level=logging.INFO)

# set yass configuration parameters
yass.set_config('config.yaml')


@profile
def my_func():
    # run preprocessor
    (standarized_path, standarized_params, channel_index,
     whiten_filter) = preprocess.run(if_file_exists='overwrite')


if __name__ == '__main__':
    my_func()
