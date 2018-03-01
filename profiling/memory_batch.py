from time import sleep
from yass.batch import BatchProcessor
from memory_profiler import profile
import logging

logging.basicConfig(level=logging.DEBUG)


@profile
def fn():
    # run preprocessor
    bp = BatchProcessor('/Users/edu/desktop/data.bin', dtype='float64',
                        n_channels=10000, data_format='wide',
                        max_memory='200MB', loader='mmap')

    gen = bp.multi_channel()

    for data, _, _ in gen:
        print(data.shape)
        sleep(1)


if __name__ == '__main__':
    fn()
