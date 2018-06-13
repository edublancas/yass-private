"""
https://keras.io/getting-started/sequential-model-guide/
"""

from keras.models import Sequential
from keras.layers import LSTM, Dense, Conv2D
import numpy as np

data_dim = 16
timesteps = 8
num_classes = 10
batch_size = 32

x_train = None
n_data, window_size, n_channels = x_train.shape
K1, K2 = n_filters
input_shape = (window_size, n_channels)

# Expected input batch shape: (batch_size, timesteps, data_dim)
# Note that we have to provide the full batch_input_shape since the network is stateful.
# the sample of index i in batch k is the follow-up for the sample i in batch k-1.
model = Sequential()


model.add(Conv2D(filters=[window_size, 1, 1, K1], kernel_size=(3, 3),
                 padding='valid', activation='relu', use_bias=True,
                 input_shape=input_shape))

model.add(Conv2D(filters=[1, 1, K1, K2], kernel_size=(3, 3),
                 padding='same', activation='relu', use_bias=True))

model.add(Conv2D(filters=[1, n_channels, K2, 1], kernel_size=(3, 3),
                 padding='valid', activation='relu', use_bias=True))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# Generate dummy training data
x_train = np.random.random((batch_size * 10, timesteps, data_dim))
y_train = np.random.random((batch_size * 10, num_classes))

# Generate dummy validation data
x_val = np.random.random((batch_size * 3, timesteps, data_dim))
y_val = np.random.random((batch_size * 3, num_classes))

model.fit(x_train, y_train,
          batch_size=batch_size, epochs=5, shuffle=False,
          validation_data=(x_val, y_val))
