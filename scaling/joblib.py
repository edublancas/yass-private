import time
from joblib import Parallel, delayed
from math import sqrt

def fn(x):
    time.sleep(x)
    return x

%%timeit
Parallel(n_jobs=1)(delayed(fn)(2) for _ in range(5))


%%timeit
Parallel(n_jobs=4)(delayed(fn)(2) for _ in range(5))
