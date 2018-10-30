"""
gcloud compute scp spike-sorter:~/private-yass/denoiser/runs \
    ~/Desktop/runs --zone us-east1-c --recurse
"""

import papermill as pm
from dstools.params.grid import make_grid


p = dict(USE_TOEPLITZ=True,
         CHANNEL=0,
         MAX_PTP_FOR_COVARIANCE_ESTIMATION=40)

def run_with_params(p):
    name = ('runs/toeplitz-{}-channel-{}-maxptp-{}.ipynb'
            .format(p['USE_TOEPLITZ'], p['CHANNEL'],
                    p['MAX_PTP_FOR_COVARIANCE_ESTIMATION']))

    _ = pm.execute_notebook('linear-denoiser-toeplitz.ipynb',
                        name, parameters=p)



grid = make_grid(dict(USE_TOEPLITZ=[True, False],
                      CHANNEL=[0],
                      MAX_PTP_FOR_COVARIANCE_ESTIMATION=[20, 40, 200]))


for p in grid:
    run_with_params(p)

