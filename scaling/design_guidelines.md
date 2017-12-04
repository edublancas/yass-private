# Design guidelines

* Writing parallel code is hard, so we will leverage data structure to write embarrasingly functions
* Write functions that operate on the smallest and independent subset of data possible (e.g. one complete channel, partial observations from a single channel, a temporal chunk from neighboring channels, temporal chunk from all channels)
* `BatchProcessor` will split the data into subsets, it is trivial to process them serially (it is already implemented), just feed data into the functions, save results and continue with the next batch
* But we know want to run operations in parallel: split the data into batches, this time batches will be smaller than in the first case since we will spawn n processes (one for each core), group batches into groups of n, they will run in parallel, process each group serially
* With such architecture, scaling up to multiple nodes won't be difficult since we can split the data and process them in parallel in each node

Example:
    1. Batches are: [a, b, c, d, e]
    2. Running on two core computer, group batches:  [[a, b], [c, d] [e]]
    3. [a, b] run in parallel, then [c, d] and finally [e]

Scaling up the previous example to three nodes would involve repeating step 1 and 2 an then distributing [a, b], [c,d] and [e] in possibly different nodes.
