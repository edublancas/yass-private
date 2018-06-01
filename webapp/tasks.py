import time
from subprocess import call


def performance_testing():
    # send mail that testing started
    # run performance test
    call(['bash', 'run_performance_testing.sh', 'testing'])
    # send mail with testing results


def example(seconds):
    print('Starting task')
    for i in range(seconds):
        print(i)
        time.sleep(1)
    print('Task completed')
