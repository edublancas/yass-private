"""
Memory profiling. Looks for a config.yaml file in the same folder.

See this for usage:

https://github.com/pythonprofilers/memory_profiler

Run with:

python -m memory_profiler memory.py yass.preprocess.run

or

mprof run memory.py yass.preprocess.run

To plot:

mprof plot
"""
# TODO: modify pipeline.py so you can memory profile it, add one decorator
# per step so you can get the ticks to see where each step starts and ends

from pydoc import locate
import argparse
import logging
import yass
from yass import preprocess
from memory_profiler import profile


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("function", type=str,
                        help="Path to function to profile")
    parser.add_argument("-l", "--logger", type=str, help="Logger level",
                        default="INFO")
    args = parser.parse_args()

    logging.basicConfig(level=getattr(logging, args.logger))
    yass.set_config('config.yaml')

    function = locate(args.function)

    fp=open('{}.log'.format(args.function.replace('.', '_')),'w+')
    to_profile = profile(function, stream=fp)
    to_profile(if_file_exists='overwrite')
    fp.close()
