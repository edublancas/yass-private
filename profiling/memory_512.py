from yass import pipeline
from memory_profiler import profile
import logging

logging.basicConfig(level=logging.INFO)


@profile
def fn():
    pipeline.run('512.yaml', clean=True)


if __name__ == '__main__':
    fn()
