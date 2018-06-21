"""
Tasks
"""

from subprocess import PIPE, run
import mail


def performance_testing(git_hash):
    """Run performance testing on a given git hash
    """
    # send mail that testing started
    mail.send('Started performance testing ({})'.format(git_hash), 'started')

    # run performance test
    command = ['bash', 'test.sh', git_hash]
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    # print(result.returncode, result.stdout, result.stderr)

    # send mail with testing results
    if result.returncode:
        mail.send('Failed performance testing ({})'.format(git_hash),
                  result.stdout)
    else:
        mail.send('Sucess performance testing ({})'.format(git_hash),
                  result.stdout)
