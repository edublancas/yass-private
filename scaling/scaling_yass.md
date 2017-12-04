# Scaling YASS to big datasets

Now that we have a verions of YASS that works I want to focus on changing the codebase so that we can scale up to thousands of channels.

The idea is to have *simple* processing functions that take small inputs, process the data and return a result. The new batch processor will be responsible of splitting the data into chunks and repeatedly calling the transformation functions. Once we have that architecture we can trivially parallelize and scale up YASS.

The main limitation for this is that many functions have their own batch processing logic, this is a typical function in YASS:

```python
def transform_data(rec):
  obs, channels = rec.shape
  transformed = []

  for a_channel in range(channels):
    transformed_channel = do_stuff(rec, a_channel)
    transformed.append(transformed_channel)
  
  return transformed
```

The problem with such functions is that there is no way to scale up the code, since each channel gets processed serially.

What we want is to have something like this:

```python
def single_channel_transform(single_channel_data):
  transformed = do_stuff(single_channel_data, a_channel)
  return transformed

processor = BatchProcessor(cores=8, function=single_channel_transform, data=data)
transformed = processor.run()
```

In the example above `single_channel_transform` operates in the smalles input possible and `BatchProcessor` is responsible for splitting the data and calling `single_channel_transform` repeatedly by feeding data from a single channel, since each call is compeltely independent we can run them at the same time! (at the cost of using more memory)

There are functions that split the data in different ways, the objective is to make all these functions operate in the smalles input possible, then the `BatchProcessor` will be responsible for splitting the data in the right way.

**Removing batch logic from several functions**

****

There is a lot of batch processing logic in several functions, from what I've seen, some process one channel at a time in for loops and others take temporal chunks from several channels and feed it into the for loops. 

What we need to do is to remove that logic since that should be responsibility of the batch processor (take a function and split the data so that it gets processed in batches), the functions should be as simple as possible (i.e. functions that apply transformations over single channels should assume the input is already data from a single channel and the functions that expect temporal chunks should assume that the input is already a small chunk)

This way we can trivially parallelize operations by only modifying the batch processor (instead of modifying the code in each function)

Here is the summary of the preprocess modules that need to be updated.

****

**Whitening functions (preprocess/filter.py)**

There are a lot of whitening functions and don't know which ones are used and which ones are not. Can you please clean up this file and remove the ones that are not used? From what I've seen only localized_whitening_matrix, whitening_matrix are being used (don't know the difference between those two), whitening_score is also being used.

Seems like these functions operate over single channels so I need you to provide me with single channel versions for the functions you are using.

**Neural network module**

Missing documentation:

neural_network.detect.nn_detection - missing

preprocess.detect.threshold_detection - check it's accurate and fill missing sections

Remove the batch logic from here, make the functions be able to operate in a single batch, then I will take care of sending the appropriate batches

**Score module**

****

As in the whitening module there are many functions, don't know which ones are being used. Same thing about batch logic, needs to be removed

We also need to refactor get_score_pca and remove the logic about loading the whiten data as binary file, it's better to loading directly from the memory map to make the code cleaner.

\---