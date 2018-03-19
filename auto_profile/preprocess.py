"""
Memory profiling for preprocess step, looks for a config.yaml file in the
same folder.

See this for usage:

https://github.com/pythonprofilers/memory_profiler

Run with:

mprof run pipeline.py
"""
import logging
import yass
from yass import preprocess
from memory_profiler import profile


@profile
def main():
    logging.basicConfig(level=logging.DEBUG)
    yass.set_config('config.yaml')
    preprocess.run(if_file_exists='overwrite')


if __name__ == '__main__':
    main()
