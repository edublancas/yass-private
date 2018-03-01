import yass
from yass import pipeline
from memory_profiler import profile
import logging

logging.basicConfig(level=logging.INFO)


@profile
def fn():
    yass.set_config('512.yaml')
    cfg = yass.read_config()
    pipeline.run(cfg, clean=True)


if __name__ == '__main__':
    fn()
