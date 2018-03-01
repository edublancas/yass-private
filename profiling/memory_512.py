from yass import pipeline
from memory_profiler import profile


@profile
def fn():
    pipeline.run('512.yaml', clean=True, logger_level='DEBUG')


if __name__ == '__main__':
    fn()
