"""
Memory profiling for entire pipeline, looks for a config.yaml file in the
same folder.

See this for usage:

https://github.com/pythonprofilers/memory_profiler

Run with:

mprof run pipeline.py
"""
from yass import pipeline
from memory_profiler import profile


@profile
def main():
    pipeline.run('config.yaml', clean=True, logger_level='DEBUG')


if __name__ == '__main__':
    main()
